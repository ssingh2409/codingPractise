# Q: How to transpose a list/array entry, in a dataframe column, into multiple rows

import pandas as pd
data = {
    'id':[1, 2],
    'name':['sha', 'sin'],
    'add' : ['add1', ['addr2', 'addr3']]
}

df = pd.DataFrame(data)
#output
#	id	name	add
#	0	1	sha	add1
#	1	2	sin	[addr2, addr3]

del_lst = []

for row in df.iterrows():
    if type(row[1][2]) == list:
        del_lst.append(row[0])
        temp_dict = {'id' : [],'name':[], 'add' : []}
    
        for i in row[1][2]:
            temp_dict['id'].append(row[1][0])
            temp_dict['name'].append(row[1][1])
            temp_dict['add'].append(i)
        
        temp_df = pd.DataFrame(temp_dict)
        df = pd.concat([df, temp_df], ignore_index=True)

df = df.drop(del_lst)
#output
#	id	name	add
#	0	1	sha	add1
#	2	2	sin	addr2
#	3	2	sin	addr3
