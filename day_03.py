import json

# run get_top_tracks.py first

data = None
with open('top_tracks.json', 'r') as f:
    data = json.loads(f.read())

summer_words = None
with open('summer.txt', 'r') as f:
    summer_words = set([c.strip().lower() for c in f.readlines()])

for track in data['toptracks']['track']:
    orig_title = track['name']
    title = orig_title.lower().strip()
    artist = track['artist']['name']
    for word in title.split():
        if word in summer_words:
            print("'{}' - {} ({})".format(track['name'], artist, word))
            break
