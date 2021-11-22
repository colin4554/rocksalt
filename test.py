import requests


def main():
    url = 'http://127.0.0.1:8000/car-rec/'
    files = {'image': open('IMG_2503.JPG', 'rb')}
    response = requests.post(url, files=files)

    # response = requests.get(url)
    print(response)

if __name__ == '__main__':
    main()