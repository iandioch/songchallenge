import json

# run get_top_tracks.py first

data = None
with open('track_bpms.json', 'r') as f:
    data = json.loads(f.read())

for track in data:
    title = track['title']
    artist = track['artist']
    bpm = track['bpm']
    print("'{}' - {} ({} bpm)".format(title, artist, bpm))
