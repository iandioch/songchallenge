#!/usr/bin/python3

import json, urllib.request, os.path

def get_json_web(url):
    try:
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'python-urllib2; ceres/last.fm (github.com/iandioch/ceres)'
            }
        )
        bytedata= urllib.request.urlopen(req).read()
        strdata = bytes.decode(bytedata)
        return json.loads(strdata)
    except Exception as e:
        print(e)
        return None

def get_json_file(path):
    if os.path.isfile(path):
        with open(path, 'r') as data:
            try:
                return json.load(data)
            except Exception as e:
                print(e)
                return None
    else:
        print('No such file found')
        return None
