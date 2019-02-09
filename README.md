# Twitch copy followers

Everyone recognizes me whenever I chat in a stream 😎 taking all the spotlight 😎. So I needed a second account to prevent that. This allowed let me to chat like the dude without being disrupted while enjoying the stream.

## Usage

Usage: `python main your_login_name oauth_token_from_browser` then `--follow` to follow all people you are following in the account with `your_login_name` from your second account.

Please follow the instruction in `client_id.txt.README` to obtain the `client_id`. You need this to get the follower list of your 'first' account

Obtain the `oauth_token_from_browser` following the [next][#getting-oauth-token] section. You need this to start following, or copying the follower list of the first account into your second account.

## Getting OAuth token

Your oauth\_token can be retrieved by logging into Twitch with your second account, press F12, go to `Network` tab (this is for chrome btw. Similar options should exist in other browsers?) then search for `gql` ... thingy (request-response pair? packet?). Then another panel appears with Headers, Preview, Response, Cookies, Timing and stuff. In "Headers", scroll down to "Request Headers", search for `Authorization: OAuth random_string`.

Here, use the `random_string`, not `OAuth random_string`. This thing seems to keep changing everytime you log in. Refer to `OAuth2` or something for more information.

## Please

Please be civil with this script.
