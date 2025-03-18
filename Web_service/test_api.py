import requests

def get_data(match_id):
    url = "https://api.cricapi.com/v1/match_info"
    params = {
  "apikey": "d8d8ad0a-46fa-4b21-b97c-719e7b56342a",
  "id": f"{match_id}"
}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def get_matching_id(match_list, target_id):
    for match in match_list:
        if match.get('id') == target_id:
            return match
    return None


print(get_data('cacf2d34-41b8-41dd-91ed-5183d880084c'))



# print(get_matching_id(get_data()['data']['matchList'], 'cacf2d34-41b8-41dd-91ed-5183d880084c'))