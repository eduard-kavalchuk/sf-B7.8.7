import requests
import favicon
import os

URL = 'https://www.python.org/'
DIR = '/tmp/favicon'
FILENAME = 'favicon'

if __name__ == '__main__':
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    
    icons = favicon.get(URL)
    icon = icons[0]
    response = requests.get(icon.url, stream=True)
    
    with open(os.path.join(DIR, f'{FILENAME}.{icon.format}'), 'wb') as image:
        for chunk in response.iter_content(1024):
            image.write(chunk)
