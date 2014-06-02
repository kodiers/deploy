__author__ = 'kodiers'
import fileinput
import datetime

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
    # This code doesn't work
    # dnsfile = open(filepath)
    # lines = dnsfile.readlines()
    # for line in fileinput.input(filepath, inplace=True):
    #     if '; Serial' in line:
    #         serial = datetime.datetime.now()
    #         line = line.replace('2014042116	; Serial', serial.strftime("%s"))
    # fileinput.close()