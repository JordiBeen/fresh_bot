import praw

def init_post():
    app_account_code = '1ybYEh8DSkdWj9Ph3WqxlCdqLgs'
    app_refresh_token = '50227942-kUCyxbRIYn4GsxwJC93mOdOpkVQ'

    r = praw.Reddit('OAuth testing example by u/TheFreshBot ver 0.1')
    r.set_oauth_app_info(client_id='GoQp4XK8LGYGgA',
                         client_secret='dSmmkic1q-dI8cexdWhUNFLo24w',
                         redirect_uri='http://127.0.0.1:65010/authorize_callback')
    r.refresh_access_information(app_refresh_token)
    r.submit(subreddit='HipHopHeads', title='Test', text='Test')
