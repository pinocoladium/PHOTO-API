
list_photos = [{'likes': 24, 'date': '15.11.18', 'size': 'w', 'url_photos': 'https://sun9-11.userapi.com/impf/KQ61RzLaAoWCe2Iov1mqCNK3I9LMYtFvBD1lZg/BOR3j84iocY.jpg?size=960x1280&quality=96&sign=f9a58a021cb922e74b8cf08cbefb190d&c_uniq_tag=zPUNxHMfmDIRyo8C1wgyKAclE6np4zpSSjSe91EpRJg&type=album'}, {'likes': 27, 'date': '01.10.19', 'size': 'w', 
'url_photos': 'https://sun3-8.userapi.com/impf/c855532/v855532794/1103ca/P8tZLDntiJM.jpg?size=591x1280&quality=96&sign=e6bcddb042572b4f42a3932f6fb8ccb4&c_uniq_tag=z2Fy4PwEGhXqXlI1O0jWxHSkM-RA0T97SQxhUQJvSO8&type=album'}]

token = 'y0_AgAAAAA23PStAADLWwAAAADWnMBUPpjadqN8TiKHkrwI9Ki9SrSyca8'

import requests

class Yandex:
    
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, name_folder):
        urn = 'v1/disk/resources/'
        url = self.url + urn
        params = {'path': name_folder}
        response = requests.put(url, headers=self.get_headers(), params=params)

    def upload_from_vk(self, list_photos, name_folder='photos vk'):
            urn = 'v1/disk/resources/upload/'
            url = self.url + urn
            self.create_folder(name_folder)
            for el in list_photos:
                url_photos = el['url_photos']
                file_name = el['likes']
                params = {'path': f'/{name_folder}/{file_name}', 'url': url_photos}
                response = requests.post(url, headers=self.get_headers(), params=params)
            return response


# token = input('To connect, enter your OAuth token: ')
yan = Yandex(token)
yan.upload_from_vk(list_photos)
