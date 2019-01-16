# Functions and properties shared between modules
import requests
import socket
import time
import re

def ipfromhost(target):
    return socket.gethostbyname(target)

def hostfromip(target):
    return socket.gethostbyaddr(target)

def isip(target):
    regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    return regex.match(target) is not None

def extract_domain(target):
    API_URL = 'https://tldextract.appspot.com/api/extract?url={}'
    response = requests.get(API_URL.format(target))
    if response.status_code != 200:
        print('Got status {} from TLDExtract.'.format(response.status_code))
        return 1
    data = response.json()

    domain = ""
    if data['subdomain']:
        domain = data['subdomain'] + '.'
    domain += data['domain']
    if data['suffix']:
        domain += '.' + data['suffix']

    return domain


def sleep(amt):
    time.sleep(amt)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'