__author__ = 'kodiers'

def change_zone_file(filepath, username):
    '''
    :param filepath: path to zone file
    :param username: username(hostname)
    :return: no results return
    Function change dnszone file and restart bind
    '''
    dnsfile = open(filepath, 'a')
    zone = "\n" + username + " IN	A	62.75.238.85"
    dnsfile.write(zone)
    dnsfile.close()
    # TODO: add how to restart dns server
    # TODO: change serial number
