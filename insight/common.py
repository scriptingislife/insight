# Functions and properties shared between modules
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