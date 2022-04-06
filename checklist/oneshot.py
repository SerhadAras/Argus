#!/usr/bin/python

import sys
from modules.flow import Flow
from modules.logger import getLogger

def main(domain):
    """
    Main method
    """
    logger = getLogger("checklist")
    flow = Flow(logger)
    results = flow.run(domain)

    print(results)

    if results is None:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1])
