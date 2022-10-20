import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = ''

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers = headers, params = params)
        source_getted = response.json()

        href = source_getted.get("href", "")
        result = requests.put(href, data = open(filename, 'rb'))
        return result

if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    print(uploader.upload('test01.txt', path_to_file))
