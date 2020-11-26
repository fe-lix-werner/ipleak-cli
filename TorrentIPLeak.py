import requests
import hashlib
import time
import json
import webbrowser
import os, sys, subprocess
from halo import Halo

TORGUARD_URL = "https://torguard.net/checkmytorrentipaddress.php?ajax&hash="
TORGUARD_MAGNET = "magnet:?xt=urn:btih:<HASH>&dn=checkmyiptorrent+Tracking+Link&tr=http%3A%2F%2F34.204.227.31%2F"


class TorrentIpLeak:

    def __init__(self):
        randomHash = hashlib.sha1(os.urandom(32)).hexdigest()
        self.tURL = TORGUARD_URL + randomHash
        tMagnet = TORGUARD_MAGNET.replace("<HASH>",randomHash)
        self.open_magnet(tMagnet)
        self.ips = []
        self.get_standard_ip()

    def getTorrentIps(self):
        response = requests.get(self.tURL)
        ipAsJSON = response.json()
        ips =[]
        data = ipAsJSON["hits"]
        for foundip in data:
            ips.append([foundip["timestamp"],foundip["addr"]])
        return ips

    def open_magnet(self,magnet):
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


    def updateIps(self):
        data = self.getTorrentIps()
        nIps = []
        for d in data:
            if not d in self.ips:
                self.ips.append(d)
                nIps.append(d)
        return nIps
