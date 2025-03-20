from flask import Flask, render_template, request
import psycopg2 as pg
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from datetime import datetime
import pytz


app = Flask(__name__)

############################################################################################################################
## DB CONNECTION BLOCK
############################################################################################################################

## Function to connect to the database
def connect_to_db():
    conn = pg.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='admin',
        port=5432
    )
    return conn


############################################################################################################################
## API CONNECTION BLOCK
############################################################################################################################
def get_api_match_data(api_id):
    url = "https://api.cricapi.com/v1/match_info"
    params = {
        "apikey": "d8d8ad0a-46fa-4b21-b97c-719e7b56342a",
        "id": f"{api_id}"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


############################################################################################################################
## DB FUNCTIONS BLOCK
############################################################################################################################

## Function to get upcoming matches
def upcoming_matches():
    conn = connect_to_db()
    cur = conn.cursor()

    query = '''
    with min_dt as (
        select min(match_dt) min_dt from ipl.d_matches where winner is null and odds is null
    )    
    SELECT 
        m.id, t1.team_name , t2.team_name, m.match_dt 
    FROM 
        ipl.d_matches m 
        join ipl.d_teams t1 on m.team_1 = t1.id 
        join ipl.d_teams t2 on m.team_2 = t2.id
        join min_dt md on m.match_dt = md.min_dt
    '''
    cur.execute(query)
    matches = cur.fetchall()

    conn.close()

    return matches


## Function to get leaderboard
def leaderboard():
    conn = connect_to_db()
    cur = conn.cursor()

    query = '''
    select * 
    from 
        (
        SELECT dense_rank() over(order by net_amount desc)rnk, full_name, net_amount FROM ipl.d_users
        )z
    order by rnk, full_name'''
    cur.execute(query)
    leaders = cur.fetchall()

    conn.close()

    return leaders


## Function to check if the user is an admin
def is_admin(user):
    # Function to check if the user is an admin
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"SELECT user_id FROM ipl.user_credentials WHERE user_id = '{user}'"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    return True if result[0]=='admin' else False


## Function to get the latest match id
def get_latest_match_id():
    conn = connect_to_db()
    cur = conn.cursor()
    query = "select min(id) from ipl.d_matches where odds is null"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    return result[0]


## Function to get the recent match history
def get_recent_match_history():
    conn = connect_to_db()
    cur = conn.cursor()
    query = '''
    select 
        m.match_dt,
        d1.team_name || ' vs ' || d2.team_name,
        d3.team_name winner,
        case 
            when winner = team_1 then split_part(odds, '/', 1)::float
            else split_part(odds, '/', 2)::float
        end win_amount,
        m.id
    from 
        ipl.d_matches m
    join ipl.d_teams d1
        on m.team_1 = d1.id
    join ipl.d_teams d2
        on m.team_2 = d2.id
    join ipl.d_teams d3
        on m.winner = d3.id
    where 
        m.winner is not null
    order by m.match_dt desc
    limit 5
    '''
    cur.execute(query)
    history = cur.fetchall()
    conn.close()
    return history


## Function to get the user id
def get_user_id(user):
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"SELECT id FROM ipl.d_users WHERE user_id = '{user}'"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    
    return result[0]


## Function to get the team id
def get_team_id(team):
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"SELECT id FROM ipl.d_teams WHERE team_name = '{team}'"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    
    return result[0]


## Function to get activ matches
def get_active_matches():
    conn = connect_to_db()
    cur = conn.cursor()
    query = '''
    select 
        m.id, t1.team_name ||' vs '|| t2.team_name, m.odds, m.api_id, case when current_timestamp at time zone 'Asia/Kolkata' + interval '3.5 hours' > toss_time then true else false end
    from
        ipl.d_matches m
        join ipl.d_teams t1 on m.team_1 = t1.id
        join ipl.d_teams t2 on m.team_2 = t2.id
    where
        m.odds is not null
        and m.winner is null
'''
    cur.execute(query)
    matches = cur.fetchall()
    conn.close()
    return matches


def check_toss_time():
    conn = connect_to_db()
    cur = conn.cursor()
    query = f'''
    select id, case when current_timestamp at time zone 'Asia/Kolkata' > toss_time then true else false end toss_update, api_id, toss_time from ipl.d_matches where id = (select min(id) from ipl.d_matches where odds is null)
    '''
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    return result[0], result[1], result[2], result[3]


############################################################################################################################
## RENDER FUNCTIONS BLOCK
############################################################################################################################

## Function to render the home page with optional user and message parameters
def render_homepage(user=None, message=None):
    matches = upcoming_matches()
    leaders = leaderboard()
    history = get_recent_match_history()
    active_matches = get_active_matches()

    if message:
        return render_template('home.html', matches=matches, user=user, message=message, leaders=leaders, history=history, active_matches=active_matches)
    elif user:
        return render_template('home.html', matches=matches, user=user, leaders=leaders, history=history, active_matches=active_matches)
    else:
        return render_template('home.html', matches=matches, leaders=leaders, history=history, active_matches=active_matches)


## Function to render the User Profile page with optional user and message parameters
def render_user_profile(user, welcomemessage=None):
    matches = upcoming_matches()
    user_id = get_user_id(user)
    match_list = ','.join(str(i[0]) for i in matches)
    
    conn = connect_to_db()
    cur = conn.cursor()
    
    query_hist = f'''
        Select match_dt, "v/s", bet_on, winner, odds, "Win/Loss" from ipl.v_match_details where id = {user_id}'''
    cur.execute(query_hist)
    prev_matches = cur.fetchall()

    query_latest = f'''
        with cte as (
            select match_id, user_id, max(update_ts) upd
            from ipl.f_bets
            where user_id = {user_id} and match_id in ({match_list})
            group by 1,2
        )
        Select
            d1.team_name || ' vs ' || d2.team_name, d3.team_name, c.bet_amount
            from ipl.f_bets a
            join cte b on a.match_id = b.match_id and a.user_id = b.user_id and a.update_ts = b.upd
            join ipl.d_matches c on a.match_id = c.id
            join ipl.d_teams d1 on c.team_1 = d1.id
            join ipl.d_teams d2 on c.team_2 = d2.id
            join ipl.d_teams d3 on a.bet_on = d3.id'''
    cur.execute(query_latest)
    curr_vote = cur.fetchall()

    standings_query = f'''
        select rnk, net_amount
        from 
            (
            SELECT dense_rank() over(order by net_amount desc)rnk, user_id, net_amount FROM ipl.d_users
            )z
        where user_id = '{user}'
        '''
    cur.execute(standings_query)
    standing = cur.fetchone()

    conn.close()

    if welcomemessage:
        return render_template('user_profile.html', user=user, matches=matches, prev_matches=prev_matches, curr_vote=curr_vote, standing=standing, welcomemessage=welcomemessage)
    else:
        return render_template('user_profile.html', user=user, matches=matches, prev_matches=prev_matches, curr_vote=curr_vote, standing=standing)


############################################################################################################################
## HOME PAGE
############################################################################################################################
@app.route('/', methods=['POST','GET'])
def hello():
    user = request.form.get('user')
    
    if user: return render_homepage(user=user)
    else: return render_homepage()


###########################################################################################################################
## LOGIN AND SIGNUP
###########################################################################################################################
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/userhome', methods=['POST'])
def userhome():
    usr = request.form['user']
    pwd = request.form['pass']

    conn = connect_to_db()
    cur = conn.cursor()
    
    query = f"SELECT * FROM ipl.user_credentials WHERE user_id = '{usr}' AND pwd = '{pwd}'"
    cur.execute(query)
    result = cur.fetchone()
    if not result: return render_template('login.html', error='Invalid username or password')

    is_validated = result[5]
    u_name = result[2]
    conn.close()

    if not is_validated: return render_template('login.html', error='User validation pending. Please contact admin to activate your account.')
    else: return render_user_profile(user=usr, welcomemessage=f'Welcome {u_name}!')


@app.route('/signup', methods=['POST'])
def signup():
    userid = request.form['userid']
    username = request.form['username']
    pwd = request.form['pass']
    repeat_pass = request.form['repeat_pass']
    email = request.form['email']

    if pwd != repeat_pass:
        return 'Passwords do not match'

    conn = connect_to_db()
    cur = conn.cursor()

    validation_query = f'''
    SELECT user_id, user_email FROM ipl.user_credentials WHERE user_id = '{userid}' OR user_email = 'email'
    '''
    cur.execute(validation_query)
    row = cur.fetchone()

    if row:
        if row[0] == userid:
            return f'UserID {userid} already exists. Please select a different UserID'
        if row[1] == email:
            return f'Email {email} already exists. Please try with another email.'

    insert_query = f'''
    INSERT INTO ipl.user_credentials (user_id, user_name, pwd, user_email, active) 
    VALUES ('{userid}', '{username}', '{pwd}', '{email}', False)
    '''
    cur.execute(insert_query)
    conn.commit()
    conn.close()

    return f'Welcome {username}!! Your signup is successful'


#############################################################################################################################
## FIXTURES AND RESULTS
#############################################################################################################################
@app.route('/fix_n_rslts', methods=['POST'])
def fix_n_rslts():
    user = request.form['user']
    conn = connect_to_db()
    cur = conn.cursor()
    
    query = '''SELECT 
                    m.id, m.match_dt, t1.team_name , t2.team_name, m.odds, t3.team_name, m.bet_amount 
                FROM ipl.d_matches m 
                join ipl.d_teams t1 on m.team_1 = t1.id 
                join ipl.d_teams t2 on m.team_2 = t2.id
                left join ipl.d_teams t3 on m.winner = t3.id 
                order by m.id'''
    cur.execute(query)
    matches = cur.fetchall()
    
    conn.close()
    
    if user: return render_template('fix_n_rslts.html', matches=matches, user=user)
    else: return render_template('fix_n_rslts.html', matches=matches)
    

#############################################################################################################################
## BET HISTORY
#############################################################################################################################
@app.route('/bet_hist', methods=['POST'])
def bet_history():
    user = request.form['user']
    conn = connect_to_db()
    cur = conn.cursor()
    
    query = '''
    with cte as (
        select dm.id match_id, du.id user_id from ipl.d_matches dm
        cross join ipl.d_users du 
        where dm.id in (select distinct match_id from ipl.v_match_details)
    )
    , user_detail as (
    select
        cte.match_id, cte.user_id, coalesce("Win/Loss"::text , 'dnp') match_result
    from 
        cte  
        left join ipl.v_match_details v on v.match_id = cte.match_id and v.id = cte.user_id
    )
    select match_id,
        max(case when user_id = 1 then match_result else null end) "test1_name",
        max(case when user_id = 2 then match_result else null end) "test2_name",
        max(case when user_id = 3 then match_result else null end) "test3_name"
    from 
        user_detail
    group by 1
    order by match_id
    '''
    cur.execute(query)
    bets = cur.fetchall()
    
    conn.close()
    
    if user: return render_template('bet_history.html', bets=bets, user=user)
    else: return render_template('bet_history.html', bets=bets)
    

#############################################################################################################################
## VOTE
#############################################################################################################################
@app.route('/vote', methods=['POST'])
def vote():
    match_id = request.form['match_id']
    team = request.form['team']
    user = request.form['user']
    user_id = get_user_id(user)
    team_id = get_team_id(team)

    conn = connect_to_db()
    cur = conn.cursor()
    check_query = f"SELECT case when current_timestamp at time zone 'Asia/Kolkata' > toss_time then true else false end FROM ipl.d_matches WHERE match_id = {match_id}"
    cur.execute(check_query)
    result = cur.fetchone()
    if result[0]: 
        conn.close()
        return render_user_profile(user=user, welcomemessage='Sorry, the toss time has passed for this match. You cannot vote now.')

    insert_query = f"INSERT INTO ipl.f_bets (user_id, match_id, bet_on, update_ts) VALUES ({user_id}, '{match_id}', {team_id}, current_timestamp at time zone 'Asia/Kolkata')"
    cur.execute(insert_query)
    conn.commit()
    
    conn.close()

    return render_homepage(user=user, message='Vote recorded successfully!')


@app.route('/navigate_to_vote', methods=['POST'])
def navigate_to_vote():
    user = request.form['user']

    if user: return render_user_profile(user=user)
    else: return render_template('login.html', error='Please login to vote')
    

#############################################################################################################################
## USER PROFILE
#############################################################################################################################
@app.route('/user_profile', methods=['POST'])
def user_profile():
    user = request.form['user']
    if is_admin(user): return render_template('admin.html')
    else: return render_user_profile(user=user)


@app.route('/logout', methods=['POST'])
def logout():
    return render_homepage()


#############################################################################################################################
## MATCH DETAILS
#############################################################################################################################
@app.route('/match_details/<int:match_id>', methods=['GET'])
def match_details(match_id):
    conn = connect_to_db()
    cur = conn.cursor()

    query = f'''with cte as (
        select 
            match_dt, "v/s",bet_on,winner,odds,"Win/Loss", id 
        from ipl.v_match_details vw 
        WHERE match_id = {match_id}
        )
        select 
            coalesce(b.match_dt, (select max(match_dt) from cte)) match_dt,
            a.full_name,
            coalesce(b."v/s", (select max("v/s") from cte)) "v/s",
            coalesce(b.bet_on, '<<dnp>>') bet_on,
            coalesce(b.winner, (select max(winner) from cte)) winner,
            coalesce(b.odds, (select max(odds) from cte)) odds,
            coalesce(b."Win/Loss", -50) "Win/Loss"
        from 
            ipl.d_users a 
        left join
            cte b
            on a.id = b.id
        order by a.full_name'''
    
    cur.execute(query) 
    match = cur.fetchall()

    conn.close()

    if match:
        return render_template('match_details.html', matches=match)
    else:
        return "Match not found", 404


@app.route('/bet_details/<int:match_id>', methods=['GET'])
def bet_details(match_id):
    conn = connect_to_db()
    cur = conn.cursor()

    query = f'''
        with cte as (
                select 
                    user_id, max(update_ts) upd
                from 
                    ipl.f_bets 
                where 
                    match_id = {match_id}
                group by 1
            )
            , bets as (
                select
                    a.user_id, a.bet_on 
                from 
                    ipl.f_bets a
                    join cte b on a.user_id = b.user_id and a.update_ts = b.upd
                where 
                    match_id = {match_id}
            )
            , all_users as (
                select 
                    a.id, a.full_name, b.bet_on
                from 
                    ipl.d_users a
                    left join bets b on a.id = b.user_id
            )
            select a.full_name, coalesce(b.team_name, '<<dnp>>') team, 
            (select t1.team_name ||' v/s '||t2.team_name from ipl.d_matches a join ipl.d_teams t1 on a.team_1 = t1.id join ipl.d_teams t2 on a.team_2 = t2.id where a.id = {match_id}),
            (select odds from ipl.d_matches where id = {match_id}),
            (select match_dt from ipl.d_matches where id = {match_id}) dt 
            from all_users a
            left join ipl.d_teams b on a.bet_on = b.id
            order by a.full_name  
    '''
    cur.execute(query) 
    bets = cur.fetchall()

    conn.close()

    if bets:
        return render_template('bet_details.html', bets=bets)
    else:
        return "Match not found", 404


#############################################################################################################################
## ADMIN ROLE
#############################################################################################################################
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = connect_to_db()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        match_id = request.form.get('match_id')
        winner = request.form.get('winner')
        
        if action == 'update':
            query_upd_match = f"UPDATE ipl.d_matches SET winner = (select id from ipl.d_teams where team_name = '{winner}') WHERE id = {match_id}"
            cur.execute(query_upd_match)

            query_upd_winner = f'''
                with cte as (
                    select user_id, max(update_ts) upd 
                    from ipl.f_bets where match_id = {match_id} group by 1
                )
                ,user_votes as (
                    select a.user_id, bet_on 
                    from ipl.f_bets a
                    join cte b on a.user_id = b.user_id and a.update_ts = b.upd
                    where a.match_id = {match_id}
                )
                ,winner_amount as (
                    select a.user_id,
                    case 
                        when winner = team_1 then split_part(odds, '/', 1)::float
                        else split_part(odds, '/', 2)::float
                    end win_amount
                    from user_votes a
                    join ipl.d_matches b on a.bet_on = b.winner and b.id = {match_id}
                )
                , final_amount as (
                    select 
                        du.id, 
                        case 
                            when fm.user_id is not null then win_amount 
                            when fm.user_id is null then 0 - (select bet_amount from ipl.d_matches where id = {match_id})
                        end net
                    from 
                        ipl.d_users du 
                    left join
                        winner_amount fm on du.id = fm.user_id
                )
                update ipl.d_users a
                set net_amount = net_amount + b.net
                from final_amount b
                where a.id = b.id
            '''
            cur.execute(query_upd_winner)
        
        conn.commit()

    query = '''SELECT 
                m.id, m.match_dt, t1.team_name, t2.team_name, m.odds, m.bet_amount 
            FROM ipl.d_matches m 
            JOIN ipl.d_teams t1 ON m.team_1 = t1.id 
            JOIN ipl.d_teams t2 ON m.team_2 = t2.id 
            where 
                m.winner is null 
                --and odds is not null 
            ORDER BY m.id'''
    
    cur.execute(query)
    matches = cur.fetchall()

    conn.close()

    return render_template('admin.html', matches=matches)


#############################################################################################################################
## ODDS UPDATE
#############################################################################################################################
def odd_update():
    match_id, cutoff, api_id, toss_time = check_toss_time()

    if cutoff:
        # api_result = get_api_match_data(api_id)
        # toss_time_gmt = api_result['dateTimeGMT']
        # gmt = pytz.timezone('GMT')
        # ist = pytz.timezone('Asia/Kolkata')
        # toss_time = datetime.strptime(toss_time_gmt, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=gmt).astimezone(ist)


        toss_done = True #if api_result['matchStarted'] else False

        if toss_done:
            conn = connect_to_db()
            cur = conn.cursor()

            query = f'''
                with cte as (
                    select 
                        user_id, max(update_ts) upd
                    from 
                        ipl.f_bets s
                    where 
                        match_id = {match_id}
                        and update_ts <= {toss_time}
                    group by 1
                )
                , bets as (
                    select
                        a.user_id, a.bet_on 
                    from 
                        ipl.f_bets a
                        join cte b on a.user_id = b.user_id and a.update_ts = b.upd
                    where 
                        match_id = {match_id} 
                )
                , all_users as (
                    select 
                        a.id, a.full_name, b.bet_on 
                    from 
                        ipl.d_users a
                        left join bets b on a.id = b.user_id
                )
                , team_bets as (
                    select 
                        bet_on, ((sum(count(1)) over()) - count(1))/count(1) factor
                    from 
                        all_users
                    group by 1
                )
                update ipl.d_matches a
                set odds = coalesce((select (factor*a.bet_amount)::int from team_bets b where b.bet_on = a.team_1),0)||'/'||coalesce((select (factor*a.bet_amount)::int from team_bets b where b.bet_on = a.team_2),0)
                where 
                    a.id = {match_id}  
            '''
            cur.execute(query)
            
            conn.commit()
            conn.close()


#############################################################################################################################
## WINNER UPDATE
#############################################################################################################################
def winner_update():
    active_matches = get_active_matches()
    for match in active_matches:
        match_id = match[0]
        api_id = match[3]
        match_over_check = True if match[4] else False
        if match_over_check:
            api_result = get_api_match_data(api_id)
            match_over = True if api_result['matchEnded'] else False

            if match_over:
                winner = api_result['matchWinner']
                # toss_time_gmt = api_result['dateTimeGMT']
                # gmt = pytz.timezone('GMT')
                # ist = pytz.timezone('Asia/Kolkata')
                # toss_time = datetime.strptime(toss_time_gmt, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=gmt).astimezone(ist)
                
                conn = connect_to_db()
                cur = conn.cursor()

                query = f"UPDATE ipl.d_matches SET winner = (select id from ipl.d_teams where team_name = '{winner}') WHERE id = {match_id}"
                cur.execute(query)

                query_upd_winner = f'''
                    with cte as (
                        select user_id, max(update_ts) upd 
                        from ipl.f_bets where match_id = {match_id} and update_ts <= (select toss_time from ipl.d_matches where id = {match_id})
                        group by 1
                    )
                    ,user_votes as (
                        select a.user_id, bet_on 
                        from ipl.f_bets a
                        join cte b on a.user_id = b.user_id and a.update_ts = b.upd
                        where a.match_id = {match_id}
                    )
                    ,winner_amount as (
                        select a.user_id,
                        case 
                            when winner = team_1 then split_part(odds, '/', 1)::float
                            else split_part(odds, '/', 2)::float
                        end win_amount
                        from user_votes a
                        join ipl.d_matches b on a.bet_on = b.winner and b.id = {match_id}
                    )
                    , final_amount as (
                        select 
                            du.id, 
                            case 
                                when fm.user_id is not null then win_amount 
                                when fm.user_id is null then 0 - (select bet_amount from ipl.d_matches where id = {match_id})
                            end net
                        from 
                            ipl.d_users du 
                        left join
                            winner_amount fm on du.id = fm.user_id
                    )
                    update ipl.d_users a
                    set net_amount = net_amount + b.net
                    from final_amount b
                    where a.id = b.id
                '''

                cur.execute(query_upd_winner)
                conn.commit()
                conn.close()


# Function to start the scheduler
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(odd_update, 'interval', seconds=10)
    scheduler.add_job(winner_update, 'interval', hours=1)
    scheduler.start()

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

##########
## MAIN ##
##########
if __name__ == '__main__':
    start_scheduler()
    app.run(debug=False, use_reloader=True)