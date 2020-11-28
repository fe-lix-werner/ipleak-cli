import requests
import hashlib
import time
import json
import os, sys, subprocess

TORGUARD_URL = 'https://torguard.net/checkmytorrentipaddress.php?ajax&hash=%s'
TORGUARD_MAGNET = "magnet:?xt=urn:btih:{0}&dn=checkmyiptorrent+Tracking+Link&tr=http%3A%2F%2F34.204.227.31%2F"

def check_torrent_leak(timeToWait):
    randomHash = hashlib.sha1(os.urandom(32)).hexdigest()
    open_magnet(TORGUARD_MAGNET.format(randomHash))
    time.sleep(timeToWait)
    return getTorrentIps(TORGUARD_URL % randomHash)

def getTorrentIps(url):
    response = requests.get(url)
    ipAsJSON = response.json()
    ips =[]
    if len(ipAsJSON) == 0:
        return ips
    data = ipAsJSON["hits"]
    for entry in data:
       ip = entry["addr"]
       if not ip in ips:
           ips.append(ip)
    return ips

def open_magnet(magnet):
    """Open magnet according to os."""
    if sys.platform.startswith('linux'):
        subprocess.Popen(['xdg-open', magnet],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif sys.platform.startswith('win32'):
        os.starFile(magnet)
    elif sys.platform.startswith('cygwin'):
        os.startfile(magnet)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', magnet],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.Popen(['xdg-open', magnet],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
