#
# TODO: 1 character arguments for each service
#
#
#
#
import yaml
import argparse
import socket

import censys
import greynoise
import shodan
import talos
import urlscan

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='the ip address or domain to look up')
    parser.add_argument('--censys', '-c', action='store_true')
    parser.add_argument('--greynoise', '-g', action='store_true')
    parser.add_argument('--shodan', '-s', action='store_true')
    parser.add_argument('--talos', '-t', action='store_true')
    parser.add_argument('--urlscan', '-u', action='store_true')
    args = parser.parse_args()
    
    target = socket.gethostbyname(args.target)
    target = args.target

    with open('insight.yml', 'r') as f:
        conf = yaml.safe_load(f)
    
    if args.censys:
        censys.lookup(target, conf['censys_uid'], conf['censys_secret'])
    if args.greynoise:
        greynoise.lookup(target)
    if args.shodan:
        shodan.lookup(target, conf['shodan_key'])
    if args.talos:
        talos.lookup(target)
    if args.urlscan:
        urlscan.lookup(target)

    # Default operation
    if not any([args.censys, args.greynoise, args.shodan, args.talos, args.urlscan]):
        censys.lookup(target, conf['censys_uid'], conf['censys_secret'])
        greynoise.lookup(target)
        shodan.lookup(target, conf['shodan_key'])
        talos.lookup(target)
        urlscan.lookup(target)

    

if __name__ == '__main__':
    main()