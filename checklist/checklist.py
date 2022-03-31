import sys
import os
import time
import signal
from modules.flow import Flow
from modules import jobs
from modules.logger import getLogger

TIMEOUT = 5
CURRENT_JOB = None

flow = None
running = True

def main():
    """
    The main method.
    """
    global flow

    logger = getLogger("checklist")
    logger.info("starting service")
    flow = Flow(logger)
    logger.info(f"loaded flow {flow.getName}", flow.getName())

    while running:
        try:
            logger.info("requesting job")
            time.sleep(2)
            CURRENT_JOB = jobs.requestJob(flow.getName())

            if CURRENT_JOB is None:
                time.sleep(TIMEOUT)
                continue

            logger.info(f"running job: {CURRENT_JOB}", flow.getName())
            results = flow.run(CURRENT_JOB['domain'])

            if results is None:
                logger.info("Pushing back running job.", flow.getName())
                jobs.pushBack(CURRENT_JOB)
                logger.info("Pushed back running job.", flow.getName())
                logger.info("Shutting down.", flow.getName())
                return

            CURRENT_JOB['checks'] = results

            jobs.pushResults(CURRENT_JOB)
        except Exception as error:
            logger.error(f"an exception has occured: {error}", flow.getName())
            time.sleep(TIMEOUT)


def shutdown(sig, frame):
    """
    shutdown service
    """
    running = False
    flow.stop()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    if os.environ.get("TIMEOUT") is not None:
        TIMEOUT = int(os.environ.get("TIMEOUT"))

    main()
