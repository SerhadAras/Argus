#!/usr/bin/python

import sys
from modules.flow import Flow
from modules.logger import getLogger

def main(target: str, type: str):
    """
    Main method
    """
    logger = getLogger("checklist")
    flow = Flow(logger)
    results = flow.run({
        "target": target,
        "type": type
    })

    print(results)

    if results is None:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[2], sys.argv[1])
