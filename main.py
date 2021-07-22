import requests
while True:
    print('url')
    url = str(input())
    print('name')
    name = str(input())

    img = requests.get(url)
    img_option = open(name + '.jpg', 'wb')
    img_option.write(img.content)
    img_option.close()
