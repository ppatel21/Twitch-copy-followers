import requests
import argparse
import json

oauth_token = ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('login_name')
    parser.add_argument('oauth_token')

    args = parser.parse_args()

    login_name = args.login_name
    login_id = getLoginId(login_name)
    global oauth_token
    oauth_token = args.oauth_token
    
    print("Login id : {}".format(login_id))

    data = getFollowingAll(login_id)
    print("data : {} ... len: {}".format(data, len(data)))

    target_ids = list(map(lambda x: x["to_id"], data))

    for target_id in target_ids:
        unfollowWithUserId(target_id)
        pass

def followWithUserId(user_id):
    payload = [{
    "variables":{"input":{"disableNotifications":False,"targetID":"{}".format(user_id)}},"extensions":{},"operationName":"FollowButton_FollowUser","query":"mutation FollowButton_FollowUser($input: FollowUserInput!) {\n  followUser(input: $input) {\n    follow {\n      disableNotifications\n      __typename\n    }\n    __typename\n  }\n}\n"
  }]

    response = useGqlPost(payload)

    print("FollowWithUserId response: {}".format(response))

def unfollowWithUserId(user_id):
    payload = [{"variables":{"input":{"targetID":"{}".format(user_id)}},"extensions":{},"operationName":"FollowButton_UnfollowUser","query":"mutation FollowButton_UnfollowUser($input: UnfollowUserInput!) {\n  unfollowUser(input: $input) {\n    follow {\n      disableNotifications\n      __typename\n    }\n    __typename\n  }\n}\n"}]

    response = useGqlPost(payload)

    print("UnfollowWithUserId response: {}".format(response))

def useGqlPost(payload):
    headers = {
        "Authorization": "OAuth {}".format(oauth_token)
    }
    r = requests.post('https://gql.twitch.tv/gql', data=json.dumps(payload), headers=headers)
    response = r.json()
    
    return response

def getLoginId(login_name):
    user_info = getUsers(login_name)
    output = user_info["data"][0]["id"]
    return output

def getUsers(login_name):
    headers = getAuthHeader()
    r = requests.get('https://api.twitch.tv/helix/users?login={}&scope=user:read:email'.format(login_name), headers=headers)
    output = r.json()
    print("getUsers output : {}".format(output))
    return output
    
def getClientId():
    output = ""
    with open("client_id.txt") as f:
        output = f.read() 

    # Strip, else `\n` gets appended and the Twitch API responds with error.
    output = output.strip()
    return output

def getAuthHeader():
    client_id = getClientId()
    headers = { "Client-ID": client_id }
    return headers

def getFollowing(login_id):
    headers = getAuthHeader()
    r = requests.get('https://api.twitch.tv/helix/users/follows?from_id={}'.format(login_id), headers=headers)
    output = r.json()
    print("getFollowing output : {}".format(output))
    return output

def getFollowingAll(login_id):
    headers = getAuthHeader()
    data = []

    cursor = ""
    while(True):
        r = requests.get('https://api.twitch.tv/helix/users/follows?from_id={}&after={}'.format(login_id, cursor), headers=headers)
        response = r.json()
        cursor = response["pagination"]["cursor"]
        
        if len(response["data"]) == 0:
            break 
    
        data += response["data"]

    return data

if __name__=="__main__":
    main()
