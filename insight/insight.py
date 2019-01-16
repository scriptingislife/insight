#
#
#
#
#
import yaml
import argparse
import socket
import os

import censys
import greynoise
import shodan
import talos
import urlscan
import crtsh

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='the ip address or domain to look up')
    parser.add_argument('--censys', '-c', action='store_true')
    parser.add_argument('--subdomains', '-d', action='store_true')
    parser.add_argument('--greynoise', '-g', action='store_true')
    parser.add_argument('--shodan', '-s', action='store_true')
    parser.add_argument('--talos', '-t', action='store_true')
    parser.add_argument('--urlscan', '-u', action='store_true')
    args = parser.parse_args()
    
    target = args.target
    #try:
        #target = socket.gethostbyname(args.target)
    #except socket.gaierror:
    #    target = args.target

    conf = None
    for cfile in '.insight', 'insight.yml':
        for loc in os.path.expanduser("~"), os.curdir, os.environ.get("INSIGHT_CONF"):
            try:
                with open(os.path.join(loc, cfile), 'r') as f:
                    conf = yaml.safe_load(f)
            except (IOError, AttributeError, TypeError):
                pass

    if args.censys:
        censys.lookup(target, conf['censys_uid'], conf['censys_secret'])
    if args.greynoise:
        greynoise.lookup(target)
    if args.shodan:
        shodan.lookup(target, conf['shodan_key'])
    if args.talos:
        talos.lookup(target)
        talos.whois(target)
    if args.urlscan:
        urlscan.lookup(target)
    if args.subdomains:
        crtsh.lookup(target)

    # Default operation
    if not any([args.censys, args.greynoise, args.shodan, args.talos, args.urlscan, args.subdomains]):
        try:
            censys.lookup(target, conf['censys_uid'], conf['censys_secret'])
        except TypeError:
            print("Couldn't find Insight configuration file. Skipping Censys...")
        greynoise.lookup(target)
        try:
            shodan.lookup(target, conf['shodan_key'])
        except TypeError:
            print("Couldn't find Insight configuration file. Skipping Shodan...")
        talos.lookup(target)
        urlscan.lookup(target)
        crtsh.lookup(target)

    

if __name__ == '__main__':
    main()