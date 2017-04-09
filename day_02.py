import json

# run get_top_tracks.py first

data = None
with open('top_tracks.json', 'r') as f:
    data = json.loads(f.read())

# load the colour list grabbed from simple english wikipedia
# https://simple.wikipedia.org/wiki/List_of_colors?veaction=edit&section=1
numbers = None
with open('numbers.txt', 'r') as f:
    numbers = set([c.strip().lower() for c in f.readlines()])

for track in data['toptracks']['track']:
    orig_title = track['name']
    title = orig_title.lower().strip()
    artist = track['artist']['name']
    for word in title.split():
        if word in numbers:
            print("'{}' - {} ({})".format(track['name'], artist, word))
            break
