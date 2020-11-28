import requests
import random
import string
import time
import json
import pycurl
from io import BytesIO

IPv4_URL = 'https://ipv4.ipleak.net/?mode=json'
IPv6_URL = 'https://ipv6.ipleak.net/?mode=json'
DNS_URL = 'https://%s.ipleak.net/dnsdetect/'
IP_INFO_URL = 'https://ipleak.net/?mode=json&ip=%s'

def test_ipv4(maxTime,maxTests):
    return test_ips(maxTime,maxTests,get_ipv4)

def test_ipv6(maxTime,maxTests):
    return test_ips(maxTime,maxTests,get_ipv6)


def test_ips(maxTime,maxTests,ipvX):
    ips = []
    data = []
    startTime = time.time()
    for i in range(maxTests):
        if  time.time() - startTime > maxTime:
            break
        ip_entry = ipvX()
        if not len(ip_entry) == 0:
            if not ip_entry["ip"] in ips:
                ips.append(ip_entry["ip"])
                data.append(ip_entry)
    return data


def get_ipv4():
    res = requests.get(IPv4_URL)
    return res.json()

def get_ipv6():
    try:
        b_obj = BytesIO()
        crl = pycurl.Curl()

        # Set URL value
        crl.setopt(crl.URL, IPv6_URL)

        # Write bytes that are utf-8 encoded
        crl.setopt(crl.WRITEDATA, b_obj)

        # Perform a file transfer
        crl.perform()

        # End curl session
        crl.close()

        # Get the content stored in the BytesIO object (in byte characters)
        get_body = b_obj.getvalue()
        return json.loads(get_body.decode('utf8'))
    except pycurl.error:
        return ""



def test_dns(maxTime,maxTests):
    startTime = time.time()
    arr = []
    for i in range(maxTests):
        if  time.time() - startTime > maxTime:
            break
        randomString = get_random_alphanumeric_string(40)
        res = requests.get(DNS_URL % (randomString)).text
        if not res in arr:
            arr.append(get_ip_info(res))
    return arr

def get_ip_info(ip):
    return requests.get(IP_INFO_URL % ip).json()


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
