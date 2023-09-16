# https://docs.python.org/3/howto/argparse.html#argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("echo", help="echo the string you passed into the program")
parser.add_argument(
    "square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbose", help="increase output verbosity", action="store_true")
# parser.add_argument(
#     "-v", "--verbosity", type=int, help="increase output verbosity", choices=[0, 1, 2])
parser.add_argument(
    "-v", "--verbosity", help="increase output verbosity", action="count")

args = parser.parse_args()
# print(args.echo)
answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else :
#     print(answer)
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
