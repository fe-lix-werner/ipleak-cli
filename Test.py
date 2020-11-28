import TorGuardTorrentIPChecker
import IPLeak
from halo import Halo
import time
import threading

green = '\033[92m'
red = '\033[91m'
end = '\033[0m'

ipv4 = []
ipv6 = []
dns = []
torrent_ips = []

def check_for_small_leak():
    spinner = Halo(text='Gathering IP-Adresses', spinner='dots')
    spinner.start()
    ipv4leak = threading.Thread(target=update_ipv4, args=(5,100))
    ipv6leak = threading.Thread(target=update_ipv6, args=(5,100))
    ip_torrent_leak = threading.Thread(target=update_torrent_ip, args=[5])

    ipv4leak.start()
    ipv6leak.start()
    ip_torrent_leak.start()

    ipv4leak.join()
    update_spinner(ipv4,spinner,"ipv4")

    ipv6leak.join()
    update_spinner(ipv6,spinner,"ipv6")

    ip_torrent_leak.join()
    update_spinner(torrent_ips,spinner,"torrent ip")

    spinner.stop()
    time.sleep(5)
    spinner.succeed("Successfully retrieved addresses")


def update_spinner(data,spinner,string):
    if len(data) > 0:
        spinner.succeed("Successfully retrieved %s addresses" % string)
        spinner.start()
    else:
        spinner.fail("Could not retrieve any %s addresses" % string)
        spinner.start()


def update_ipv4(maxTime,maxTests):
    ipv4.clear()
    entries = IPLeak.test_ipv4(maxTime,maxTests)
    for entry in entries:
        ipv4.append(entry)

def update_ipv6(maxTime,maxTests):
    ipv6.clear()
    entries = IPLeak.test_ipv6(maxTime,maxTests)
    for entry in entries:
        ipv6.append(entry)

def update_torrent_ip(maxTime):
    torrent_ips.clear()
    entries = TorGuardTorrentIPChecker.check_torrent_leak(maxTime)
    for entry in entries:
        torrent_ips.append(entry)

if __name__ == "__main__":
    check_for_small_leak()
