import requests
import os
import json
import shutil
import time

import pandas as pd

bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/1.1/users/lookup.json"

users_ = pd.read_csv("users_data.csv", index_col=0)
user_id_list = list(users_["user_id"])
user_id_str_list = [str(userid) for userid in user_id_list]
# since twitter can only take max 100 users per request
user_id_str_list1 = user_id_str_list[:100]
user_id_str_list2 = user_id_str_list[100:200]
user_id_str_list3 = user_id_str_list[200:300]
user_id_str_list4 = user_id_str_list[300:400]
user_id_str_list5 = user_id_str_list[400:]

all_user_partitions = [user_id_str_list1,user_id_str_list2,user_id_str_list3,user_id_str_list4,user_id_str_list5]


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

    for idx, user_list in enumerate(all_user_partitions):
        user_strings = ",".join(user_list)
        query_params = {"user_id": user_strings}
        json_response = connect_to_endpoint(search_url, query_params)
        filename = 'more_users_data{}.json'.format(idx)
        with open(filename, 'w') as f:
            json.dump(json_response, f)
        time.sleep(5)

if __name__ == "__main__":
    main()
