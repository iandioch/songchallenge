from urllib.parse import quote_plus
from loadjson import get_json_web
import json

BPM_NUM = 250

data = None
with open('top_tracks.json', 'r') as f:
    data = json.load(f)

tracks = []
for track in data['toptracks']['track']:
    tracks.append(track)
    if len(tracks) == BPM_NUM:
        break

config = None
with open('config.json', 'r') as f:
    config = json.load(f)

api_key = config['getsongbpm_api_key']

track_ids = []
for track in tracks:
    title = track['name']
    artist = track['artist']['name']

    track_id_url = 'https://api.getsongbpm.com/search/?api_key={}&type=song&lookup={}'.format(api_key, quote_plus(title))
    full_data = get_json_web(track_id_url)
    if full_data is None:
        print('Unable to load data from API')
        continue

    full_data = full_data['search']
    if 'error' in full_data:
        print('Error:', full_data['error'], 'for', title)
    else:
        _id = None
        for ans in full_data:
            if ans['name'].lower() == artist.lower():
                _id = ans['id']
                break
        if _id is None:
            print('Found no match for', title, 'by', artist)
        else:
            track_bpm_url = 'https://api.getsongbpm.com/song/?api_key={}&id={}'.format(api_key, _id)
            bpm_data = get_json_web(track_bpm_url)
            if bpm_data is None:
                print('bpm_data is None')
                continue
            bpm_data = bpm_data['song']
            bpm_str = bpm_data['tempo']
            if bpm_str is None:
                continue
            track_ids.append({
                'artist': artist,
                'title': title,
                'id': _id,
                'bpm': int(bpm_str)
            })

track_ids.sort(key=lambda x:x['bpm'], reverse=True)
with open('track_bpms.json', 'w+') as f:
    f.write(json.dumps(track_ids, indent=4))
