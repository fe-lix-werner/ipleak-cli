import threading
import IPLeak

from halo import Halo


CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CEND      = '\33[0m'
CBLUE2   = '\33[94m'

ipv4 = []
ipv6 = []
dns = []
torrent_ips = []

def check_for_small_leak():
    print("\n\n")

    spinner = Halo(text='Gathering IP-Adresses', spinner='dots')
    spinner.start()
    ipv4leak = threading.Thread(target=update_ipv4, args=(20,50))
    ipv6leak = threading.Thread(target=update_ipv6, args=(20,50))
    ip_torrent_leak = threading.Thread(target=update_torrent_ip, args=[30])
    dns_server_leak = threading.Thread(target=update_dns, args=(30,1000))

    ipv4leak.start()
    ipv6leak.start()
    ip_torrent_leak.start()
    dns_server_leak.start()

    ipv4leak.join()
    update_spinner(ipv4,spinner,"ipv4")

    ipv6leak.join()
    update_spinner(ipv6,spinner,"ipv6")

    ip_torrent_leak.join()
    update_spinner(torrent_ips,spinner,"torrent ip")

    dns_server_leak.join()
    update_spinner(dns,spinner,"dns server")

    spinner.stop()
    print("\n\nRESULTS")
    print_ipv4_results()

    if len(ipv6) > 0:
        print_ipv6_results()

    print_dns_results()

    if len(torrent_ips) > 0:
        print_torrent_results()

    print("\n\n")

def print_ipv4_results():
    print("\n\t" + CBLUE2 + "Discovered IPv4 Adresses\n" + CEND)
    print_ips(ipv4)
    if (len(ipv4) > 1):
        print("\t\t" + CRED2 + "!!!WARNING YOU IPv4 might be leeking!!!" + CEND)

def print_ipv6_results():
    print("\n\t" + CBLUE2 + "Discovered IPv6 Adresses\n" + CEND)
    print_ips(ipv6)
    print("\n\t\t" + CRED2 + "!!!WARNING YOU IPv6 might be leeking!!!" + CEND)

def print_dns_results():
    print("\n\t" + CBLUE2 + "Discovered DNS Server Adresses \n" + CEND)
    print_ips(dns)

def print_torrent_results():
    print("\n\t" + CBLUE2 + "Discovered Torrent IP Adresses \n" + CEND)
    print_ips(torrent_ips)
    if len(torrent_ips) > 1:
        print("\n\t\t" + CRED2 + "!!!WARNING Torrent IP might be leeking!!!" + CEND)

def print_ips(ips):
    for entry in ips:
        ip = entry['ip']
        country = entry['country_name']
        region = entry['region_name']
        city = entry['city_name']
        res = ", ".join([city,region,country])
        print("\t\t\t" + CGREEN2 + ip + " from "+ res + CEND)


def update_spinner(data,spinner,string):
    if len(data) > 0:
        spinner.succeed("Successfully retrieved %s addresses" % string)
        spinner.start()
    else:
        spinner.fail("Could not retrieve any %s addresses" % string)
        spinner.start()

def update_dns(maxTime,maxTests):
    dns.clear()
    entries = IPLeak.test_dns(maxTime,maxTests)
    for entry in entries:
        dns.append(entry)

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
    entries = IPLeak.test_torrent_ip(maxTime)
    for entry in entries:
        torrent_ips.append(entry)

if __name__ == "__main__":
    check_for_small_leak()
