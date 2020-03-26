# Twitch copy followers

Simply copy your followers to another account easily.

## Usage

To see list of your 'source' account: `python main source_account_name`.

You need to have the `client_id` of the Twitch app made for this 'source' account. Follow the instruction in `client_id.txt.README` to obtain the `client_id`.

To copy followers: `python main source_account_name oauth_token_from_browser --follow` to follow all people followed by your 'source' account with your second account.

Obtain the `oauth_token_from_browser` following the [next][#getting-oauth-token] section. You need this to start following, or copying the follower list of the first account into your second account.

## Getting OAuth token

Your oauth\_token can be retrieved by logging into Twitch with your second account, press F12, go to `Network` tab (this is for chrome btw. Similar options should exist in other browsers?) then search for `gql` ... thingy (request-response pair? packet?). Then another panel appears with Headers, Preview, Response, Cookies, Timing and stuff. In "Headers", scroll down to "Request Headers", search for `Authorization: OAuth random_string`.

Here, use the `random_string`, not `OAuth random_string`. This thing seems to keep changing everytime you log in. Refer to `OAuth2` or something for more information.

## Please

Please be civil with this script.
