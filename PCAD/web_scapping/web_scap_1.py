import requests

url1 = 'https://automatetheboringstuff.com/files/rj.txt'
url2 = 'https://automatetheboringstuff.com/files/dummy.txt'


def getdata():
    res = requests.get(url2)
    try:
        res.raise_for_status()
        print(res.text[0:100])
    except Exception as exc:
        print('There was a problem: %s' % (exc))


if __name__ == '__main__':
    getdata()
