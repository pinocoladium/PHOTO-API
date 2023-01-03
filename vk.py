import requests
import json

class Vk:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {'access_token': token, 'v': version}
    def get_photos(self, id, count=5):
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {'album_id': 'profile', 'owner_id': id, 'extended': 1, 'count': count}
        res = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        print(res)
        if "error" in res.keys():
            print('Error')
            return
        elif "error" in res.keys() and int(res["error"]["error_code"]) == 30:
            print('This profile is private. Information is not available')
            return
        elif int(res["response"]["count"]) == 0:
            print('Photo not found. Profile has no photo')
            return 
        else:
            print(f'Found {res["response"]["count"]} photos')
            print('Getting information about a photo....')
        list_photos = []
        for el in (res['response']['items']):
            likes = el['likes']['count']
            s = el['date']
            import time
            date = time.strftime('%d.%m.%y', time.gmtime(s))
            for el_size in el['sizes']:
                if el_size['type']==  'w':
                    size = el_size['type']
                    url_photos = el_size['url']
                    list_photos.append({'likes': likes, 'date': date, 'size': size, 'url_photos': url_photos})
                    print('Photo information received....')
        return list_photos



