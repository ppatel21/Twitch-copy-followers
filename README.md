# Twitch copy followers

Everyone recognizes me whenever I chat in a stream 😎 taking all the spotlight 😎. So I needed a second account to prevent that, let me chat like a twitch chat while not disrupting the stream I'm watching.

## Usage

Usage: `python main your_login_name your_second_id_oauth_token` then `--follow` to follow all people you are following in the account with `your_login_name` from your second account.

## Getting OAuth token

Your oauth\_token can be retrieved by logging into Twitch with your second account, press F12, go to `Network` tab (this is for chrome btw. Similar options should exist in other browsers?) then search for `gql` ... thingy (request-response pair? packet?). Then another panel appears with Headers, Preview, Response, Cookies, Timing and stuff. In "Headers", scroll down to "Request Headers", search for `Authorization: OAuth random_string`.

Here, use the `random_string`, not `OAuth random_string`. This thing seems to keep changing everytime you log in. Refer to `OAuth2` or something for more information.

## Please

Don't use this for creepy purpose. I hesitated to publish this because there must be creepy people ... if they ... if anyone finds this repository.

For non-creepy purposes, I would really follower SYNCER instead of copying manually so that things are a lot easier.
