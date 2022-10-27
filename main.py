import requests
import favicon
import argparse, os
import sys

def check_path(path):
    if os.path.isdir(path):
        return path
    else:
        print(f'{path}: No such directory.')
        sys.exit(1)

def check_url(url):
    try:
        requests.get(url)
        return url
    except:
        print(f'{url}: Unknown URL.')
        sys.exit(1)

def check_name(name):
    if name is None:
        print('Name for output file was not specified')
        sys.exit(1)
    return name

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=check_url, required=True)
    parser.add_argument('--dst', type=check_path, default='.')
    parser.add_argument('--name', type=check_name, required=True)
    args = parser.parse_args()

    icons = favicon.get(args.src)
    icon = icons[0]
    response = requests.get(icon.url, stream=True)

    path = os.path.join(args.dst, args.name)
    with open(f'{path}.{icon.format}', 'wb') as image:
        for chunk in response.iter_content(1024):
            image.write(chunk)
