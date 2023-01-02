import requests
import json
from pprint import pprint

token = '8aa7262f8aa7262f8aa7262f8389b5336188aa78aa7262fe916c858ae144bda9b06dcdd'
id = 226089495

class VK:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {'access_token': token, 'v': version}

    def get_photos(self, id, count=5):
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {'album_id': 'profile', 'owner_id': id, 'extended': 1, 'count': count}
        res = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        print(f'Found {res["response"]["count"]} photos')
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
        return print(list_photos)


# with open ('info_file.json', 'wt',  encoding='utf-8') as file_json:
#             json.dump(res, file_json, indent=4)

vk_client = VK(token, '5.131')
m = vk_client.get_photos(id)


