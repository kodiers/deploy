__author__ = 'kodiers'
__version__ = '0.1 beta'
FILEPATH = "/Users/kodiers/Desktop/PythonProjects/deploy/files/it-national.com" # path to zone file( shoul be in global settings
TEMPFILE = "/Users/kodiers/Desktop/PythonProjects/deploy/files/temp_it-national.com" # Temporary file for write
import datetime
import os

def change_zone_file(filepath, username):
    '''
    :param filepath: path to zone file
    :param username: username(hostname)
    :return: no results return
    Function change dnszone file and restart bind
    '''
    # Append new site in dns zone
    dnsfile = open(filepath, 'a')
    zone = "\n" + username + "\tIN\tA\t62.75.238.85"
    dnsfile.write(zone)
    dnsfile.close()
    # TODO: test restart dns server
    dnsfile = open(filepath, 'r')
    writefile = open(TEMPFILE, 'w')
    lines = dnsfile.readlines()
    # Change serial
    for line in lines:
        if '; Serial' in line:
            serial = datetime.datetime.now().strftime("%s")
            newstr = '\t\t\t ' + serial + '\t; Serial\n'
            line = line.replace(line, newstr)
        writefile.write(line)
    writefile.close()
    dnsfile.close()
    # replace files
    os.remove(filepath)
    os.rename(TEMPFILE, filepath)
    #os.system('service bind9 restart')    # commented for local machine
