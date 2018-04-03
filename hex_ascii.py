#!/usr/bin/python3

import argparse

def return_decode(string):
        print("[*] %s => %s") % (string, string.decode("hex"))

def return_encode(string):
        print("[*] %s => %s") % (string, string.encode("hex"))

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decode", help="The string will be decoded from hex")
parser.add_argument("-e", "--encode", help="The string will be encoded to hex")

args = parser.parse_args()

if args.decode:
	return_decode(args.decode)

if args.encode:
	return_encode(args.encode)
