import praw
from .settings import reddit_conf


def init_post(new_track_data):
    app_refresh_token = reddit_conf.get('app_refresh_token')
    client_id = reddit_conf.get('client_id')
    client_secret = reddit_conf.get('client_secret')
    redirect_uri = reddit_conf.get('redirect_uri')

    subreddit = 'HipHopHeads'
    title = new_track_data.get('title')
    url = new_track_data.get('url')

    print('Initialize new reddit class')
    r = praw.Reddit('OAuth testing example by u/TheFreshBot ver 0.1')
    print('Setting oauth app info')
    r.set_oauth_app_info(client_id=client_id,
                         client_secret=client_secret,
                         redirect_uri=redirect_uri)
    print('Setting refresh access information')
    r.refresh_access_information(app_refresh_token)
    print('Submitting new post:')
    print(title)
    print(url)
    r.submit(subreddit=subreddit, title=title, text=None, url=url)
    print('New post successfully submitted.')
