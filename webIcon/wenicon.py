import requests
import favicon

icons = favicon.get('https://www.baidu.com/')
icon = icons[0]

response = requests.get(icon.url, stream=True)
with open('./python-favicon.{}'.format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)