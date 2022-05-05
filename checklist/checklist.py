import os
import sys
import time
import signal
import threading

from modules.flow import Flow
from modules import jobs
from modules.logger import getLogger

TIMEOUT = 5
CURRENT_JOB = None

ADVERT_TIMEOUT = threading.Event()
JOB_TIMEOUT = threading.Event()

logger = getLogger("checklist")

flow = None
running = True

def advert():
    """
    Advert thread
    """
    global flow
    global running

    while running:
        try:
            jobs.advertise(flow.getFlowAdvertisment())
        finally:
            ADVERT_TIMEOUT.wait(5)

def main():
    """
    The main method.
    """
    global flow
    global logger
    global running

    logger.info("starting service")
    flow = Flow(logger)
    logger.info(f"loaded flow {flow.getName()}", flow.getName())

    threading.Thread(target=advert).start()

    while running:
        try:
            logger.info("requesting job")
            CURRENT_JOB = jobs.requestJob(flow.getName())

            if CURRENT_JOB is None:
                JOB_TIMEOUT.wait(TIMEOUT)
                continue

            logger.info(f"running job: {CURRENT_JOB}", flow.getName())
            results = flow.run(CURRENT_JOB)

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
            JOB_TIMEOUT.wait(TIMEOUT)

    logger.info("Checklist has finished.", flow.getName())


def shutdown(sig, frame):
    """
    shutdown service
    """
    global running
    global logger
    global flow

    logger.info("Stopping checklist.", flow.getName())

    running = False

    # Stop timeouts
    ADVERT_TIMEOUT.set()
    JOB_TIMEOUT.set()

    # Stop running job
    flow.stop()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    if os.environ.get("TIMEOUT") is not None:
        TIMEOUT = int(os.environ.get("TIMEOUT"))

    main()
