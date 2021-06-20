def add_argument(parser):
    parser.add_argument("content")


def start(args):
    print(f"Example {args.content}")
