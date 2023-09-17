# https://docs.python.org/3/howto/argparse.html#argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("echo", help="echo the string you passed into the program")
# parser.add_argument(
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
#     "square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbose", help="increase output verbosity", action="store_true")
# parser.add_argument(
#     "-v", "--verbosity", type=int, help="increase output verbosity", choices=[0, 1, 2])
parser.add_argument(
    "-v", "--verbosity", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()
# print(args.echo)
answer = args.x**args.y
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else :
#     print(answer)
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)
# if args.verbosity >= 2:
#     print(f"{args.x} to the power {args.y} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.x}^{args.y} == {answer}")
# else:
#     print(answer)
if args.verbosity >= 3:
    print(f"Running '{__file__}")
if args.verbosity >= 2:
    print(f"{args.x} to the power {args.y} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.x}^{args.y} == {answer}")
else:
    print(answer)
