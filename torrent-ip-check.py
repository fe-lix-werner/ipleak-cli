import requests
import hashlib
import time
import json
import webbrowser

TORGUARD_URL = "https://torguard.net/checkmytorrentipaddress.php?ajax&hash="
TORGUARD_MAGNET = "magnet:?xt=urn:btih:<HASH>&dn=checkmyiptorrent+Tracking+Link&tr=http%3A%2F%2F34.204.227.31%2F"

class TorrentIpLeak:

    def TorrentIpLeak(self, updateTime):
        randomHash = hashlib.sha1(os.urandom(32)).hexdigest()
        self.tURL = TORGUARD_URL + randomHash
        self.tMagnet = TORGUARD_MAGNET.replace("<HASH>",randomHash)
        self.updateTime = updateTime

    def getTorrentIps(self):
        fullllmagnet = "qbittorrent \"" + tm + "\" &"
        os.system(fullmagnet)
        time.sleep(20)
        respone = requests.get(requestURL + rhash)
        return respone.json()

    def openTorrentClient(self):
        webbrowser.open("\""+ self.tMagnet +"\"")

    def formatTorrentIps(self, ipJson):
        ips =[]
        data = ipJson["hits"]
        for foundip in data:
            ips.append(foundip["addr"])
        return ips

    def check_torrent_leak():
        print("Your current IP Adress is " + getCurrentIP())
        foundIps = formatTorrentIps(getTorrentIps())
        ips = "\n".join(foundIps)
        lenght = len(foundIps)
        print("Found " + str(lenght) + " Torrent Ips.")
        print(ips)

check_torrent_leak()
