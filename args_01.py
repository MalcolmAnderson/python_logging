# https://docs.python.org/3/howto/argparse.html#argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("echo", help="echo the string you passed into the program")
parser.add_argument(
    "square", help="display a square of a given number", type=int)

args = parser.parse_args()
# print(args.echo)
print(args.square**2)
