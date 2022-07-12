import json
import time 
import dotenv
dotenv.load_dotenv('.env')

import os
import urllib.request

def main():
    WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
    API_URL = 'https://itunes.apple.com/lookup'
    APP_ID = os.environ.get('APP_ID')
    QUERY = '?id=' + str(APP_ID)
    CURRENT_VERSION = os.environ.get('CURRENT_VERSION')

    with urllib.request.urlopen(API_URL + QUERY) as res:
        data = json.loads(res.read())
    version = data['results'][0]['version']

    if version > CURRENT_VERSION:
        print('update arrive!')
        text = '\n'.join([
            'new version app arrive !',
            f'https://apps.apple.com/jp/app/id{APP_ID}'
        ])
        req = urllib.request.Request(
            WEBHOOK_URL,
            json.dumps({'content': text}).encode(),
            {'Content-Type': 'application/json', "User-Agent": "curl/7.64.1"}
        )
        with urllib.request.urlopen(req) as res:
            print(res)
    else:
        print('no update there')

if __name__ == '__main__':
    main()
    time.sleep(300)