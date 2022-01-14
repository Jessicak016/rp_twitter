import requests
import os
import json
import shutil
import time

import pandas as pd

# export BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAGa3VQEAAAAACzHyjCVsC%2BSlFC31hDnSqgdbBJg%3DH90EUhjsrMdGKRLVLYd9nGaw6P6uQq48pKBdQL6jeAg3a0GGIq'

# export BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAGa3VQEAAAAA%2F%2FuK7ccCrE1evvXxZX5DX18F3fA%3Dh3sjwom4Iuqav8PWmfvvdU3AG5MjBrhExA3eUAtUAmcgDVf5Fx'

bearer_token = os.environ.get("BEARER_TOKEN")

# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate
# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py

# https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators
# search_url = "https://api.twitter.com/1.1/search/tweets.json"
search_url = "https://api.twitter.com/1.1/tweets/search/fullarchive/RJlastyear.json"


query_params1 = {
'query': '#RelapsingPolychondritis',
'result_type': 'recent',
'tweet.fields': 'id,text,author_id,created_at,entities,in_reply_to_user_id,public_metrics',
'expansions': 'author_id', # enable object children
'user.fields': 'username,name,public_metrics',
'max_results': 100, 'next': {}}

query_params = {
'query': '#RelapsingPolychondritis OR #relapsingpolychondritis', 'maxResults': '100', 'next_token': {},
"fromDate": "201609110000", "toDate": "201709120000"}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r

def connect_to_endpoint(url, params, next_token=None):

    if (next_token is not None):
        params['next'] = next_token
        #url = "https://api.twitter.com/2/tweets/search/all?&next_token={}".format(next_token)
    else:
        pass

    response = requests.request("GET", url, auth=bearer_oauth, params=params)

    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    count = 0
    flag = True

    json_responses_list = []

    json_response = connect_to_endpoint(search_url, query_params)
    filename = 'rp_data2.json'

    with open(filename, 'w') as f:
        json.dump(json_response, f)

def main2():
    count = 0
    flag = True
    file_count = 0
    json_responses_list = []
    json_response = connect_to_endpoint(search_url, query_params)
    # if "previous_token" in json_response:
        # print("---first request results in previous_token--")
        # token = json_response["meta"]["previous_token"]
        # json_response = connect_to_endpoint(url, query_params, token)

    output_file_name =  "tweet_data_page{}.json".format(file_count)
    with open(output_file_name, "w") as f:
        json.dump(json_response, f)
    while "next" in json_response.keys():
        if type(json_response["next"]) == str:
            next_token = json_response["next"]
            file_count += 1
            json_response = connect_to_endpoint(search_url, query_params, next_token)
            output_file_name =  "tweets/tweet_data_page{}.json".format(file_count)
            with open(output_file_name, "w") as f:
                json.dump(json_response, f)
            time.sleep(1)
    print('Finished')




    # try:
        # while json_response["meta"]["next_token"]:


    # except:



if __name__ == "__main__":
    main2()
