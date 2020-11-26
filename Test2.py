import RandomStringGenerator
import requests

arr = []

for i in range(1000):
    print("Test numero " + str(i))
    stri = RandomStringGenerator.get_random_alphanumeric_string(40)
    url = 'https://' + stri+'.ipleak.net/dnsdetect/'
    res = requests.get(url).text
    if not res in arr:
        arr.append(res)
        print(res)


