from TorrentIPLeak import TorrentIpLeak as tLeak
import IPv4IPv6 as ipLeak
from halo import Halo
import time

green = '\033[92m'
red = '\033[91m'


def checkIpLeak():
    ipv4s = []
    spinner = Halo(text='Looking for IPv4 Adresses', spinner='dots')
    spinner.start()
    ipv4s = iLeak.check_IPv4Leak()
    spinner.stop()
    print(ipv4s)

def checkIpsEvery5Seconds(tl):
        count = 0
        spinner = Halo(text='Looking for new entries', spinner='dots')
        spinner.start()
        while count < 5:
            time.sleep(5)
            count +=1
            updatedIps = tl.updateIps()
            spinner.stop()
            if len(updatedIps) > 0:
                if (len(updatedIps) == 1):
                    print("Found " +str(len(updatedIps)) +" new entry:")
                else:
                    print("Found " +str(len(updatedIps)) +" new entries:")
                for entry in updatedIps:
                    color = ""
                    if entry[1] == tl.standard_ip:
                        color = green
                    else:
                        color = red
                    print(time.ctime(int(entry[0])) + ":\t\t" + color + entry[1] + '\033[0m')
            spinner.start()
        spinner.stop()
        print("The leak test has finished.")
        leaking = 1
        for ip in tl.ips:
            if not ip == tl.standard_ip:
                leaking = 0
        if leaking:
            print(red+"!!!\tYOUR TORRENT IP SEEMS TO BE LEEKING\t!!!"+ '\033[0m')
        else:
            print(green+ "EVERYTHING SEEMS TO BE ALRIGHT"+ '\033[0m')


if __name__ == "__main__":
    #tl = tLeak()
    #checkIpsEvery5Seconds(tl)
    il = ipLeak()
    checkIpLeak(il)

