import requests

def get_data():
    url = "https://api.cricapi.com/v1/series_info"
    params = {
  "apikey": "d8d8ad0a-46fa-4b21-b97c-719e7b56342a",
  "id": "49fc7a37-da67-435e-bf5f-00da233e9ff4"
}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def get_matching_id(match_list, target_id):
    for match in match_list:
        if match.get('id') == target_id:
            return match
    return None




print(get_matching_id(get_data()['data']['matchList'], '445e4eac-2a9c-4810-afd4-77197aeed7c3'))
# {
#   "apikey": "d8d8ad0a-46fa-4b21-b97c-719e7b56342a",
#   "id": "445e4eac-2a9c-4810-afd4-77197aeed7c3"
# }