import argparse
from pathlib import Path
from auto.utils import AutoUtils

from auto.cli_action import AutoCLIAction


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", type=AutoCLIAction, choices=list(AutoCLIAction)
    )
    parser.add_argument(
        "targetpath", type=Path
    )
    args = parser.parse_args()

    match args.action:
        case AutoCLIAction.Clean:
            AutoUtils.clean(args.targetpath)
        case _:
            raise ValueError(f"action {args.action} not found")


if __name__ == "__main__":
    main()
