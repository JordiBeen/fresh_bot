import soundcloud
import json

from .post_to_reddit import init_post


def init_detection():
    print('Init detection (detect_changes.py)')
    # create client object with app credentials
    client = soundcloud.Client(client_id='d686e2432fee0aa8b4ad664f3c037231',
                               client_secret='75d22267f06aa492d3928e36a5c2e745',
                               redirect_uri='https://soundcloud.com/freshboterror')

    with open('data/tracks.json') as data_file:
            saved_tracks = json.load(data_file)

    artists = [
        {
            'name': 'kanyewest',
            'user_id': '174006135'
        },
        {
            'name': 'octobersveryown',
            'user_id': '1078461'
        },
        {
            'name': 'lilb',
            'user_id': '109965622'
        },
        {
            'name': 'theweeknd',
            'user_id': '3274725'
        },
        {
            'name': 'macklemore',
            'user_id': '557633'
        },
        {
            'name': 'logic',
            'user_id': '56873359'
        }

    ]

    for artist in artists:
        new_track = client.get('/users/{}/tracks'.format(artist.get('user_id')),limit=1)[0]

        if str(new_track.id) not in saved_tracks['data']:
            save_new_track(new_track, saved_tracks)

def save_new_track(track, saved_tracks):

    new_track_dict = {'artist': track.user.get('username'), 'title': track.title}

    saved_tracks['data'][track.id] = new_track_dict

    with open('data/tracks.json', 'w') as data_file:
        json.dump(saved_tracks, data_file)

    new_track_data = {
        'title': track.user.get('username') + ' - ' + track.title,
        'url': track.permalink_url
         }

    init_post(new_track_data)
