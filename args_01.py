# https://docs.python.org/3/howto/argparse.html#argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("echo", help="echo the string you passed into the program")

args = parser.parse_args()
print(args.echo)
