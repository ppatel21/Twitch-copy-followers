import requests
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('login_name')

    args = parser.parse_args()

    login_name = args.login_name
    login_id = getLoginId(login_name)
    
    print("Login id : {}".format(login_id))

def getLoginId(login_name):
    user_info = getUsers(login_name)
    output = user_info["id"]
    return output

def getUsers(login_name):
    client_id = getClientId()
    headers = { "Client-ID": client_id }
    r = requests.get('https://api.twitch.tv/helix/users?login={}'.format(login_name), headers=headers)
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

if __name__=="__main__":
    main()
