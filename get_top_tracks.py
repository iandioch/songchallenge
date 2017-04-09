#!/usr/bin/python3

from loadjson import get_json_web, get_json_file
import json, datetime

NUM_TRACKS = 500

if __name__ == '__main__':
    config_data = get_json_file('config.hidden.json')
    if config_data is None:
        print('Unable to load config_data')
    username = config_data['username']
    api_key = config_data['api_key']
    
    recent_track_url = 'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=%s&api_key=%s&format=json&limit=%d' % (username, api_key, NUM_TRACKS)
    full_data = get_json_web(recent_track_url)
    if full_data is None:
        print('Unable to load data from API')
    with open('top_tracks.json', 'w+') as outfile:
        outfile.write(json.dumps(full_data, indent=4))
