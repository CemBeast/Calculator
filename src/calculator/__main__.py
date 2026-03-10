import argparse

from calculator.core import add


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add two integers")
    add_parser.add_argument("left", type=int)
    add_parser.add_argument("right", type=int)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        print(add(args.left, args.right))
        return 0

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
