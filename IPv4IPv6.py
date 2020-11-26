import requests
import pycurl
from io import BytesIO

IPv4_API = "http://v4.ipv6-test.com/api/myip.php"
IPv6_API = 'http://v6.ipv6-test.com/api/myip.php'

def get_IPv4():
    result = requests.get(IPv4_API)
    return result.text

def get_IPv6():
    b_obj = BytesIO()
    crl = pycurl.Curl()

    # Set URL value
    crl.setopt(crl.URL, IPv6_API)

    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer
    crl.perform()

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters)
    get_body = b_obj.getvalue()
    return get_body.decode('utf8')

# checks the ip 10 times and gives back an array of found ips
def check_IPv4Leak():
    ips = []
    count = 0
    while count < 10:
        ip = get_IPv4()
        if not ip in ips:
            ips.append(ip)
        count += 1
    return ips

# checks the ipv6 adress 10 times and gives back an array of found ips
def check_IPv6Leak():
    ips = []
    count = 0
    while count < 10:
        ip = get_IPv6()
        if not ip in ips:
            ips.append(ip)
            print("adding ip: " + ip )
        count += 1
    return ips

