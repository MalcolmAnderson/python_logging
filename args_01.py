# https://docs.python.org/3/howto/argparse.html#argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("echo", help="echo the string you passed into the program")
parser.add_argument(
    "square", type=int, help="display a square of a given number")
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()
# print(args.echo)
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)
