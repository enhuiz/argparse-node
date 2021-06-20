import sys

from argparse_node import ArgumentParserNode
from anytree import RenderTree

from . import show
from . import wohs
from . import sub_example


def add_argument(parser):
    parser.add_argument("--verbose", action="store_true")
    return [show, wohs, sub_example]


def main():
    parser = ArgumentParserNode(sys.modules[__name__])
    args = parser.parse_args()
    if args.verbose:
        print(RenderTree(parser))
    parser.start(args)


if __name__ == "__main__":
    main()
