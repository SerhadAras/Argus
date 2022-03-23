import os
import time
from modules.flow import Flow
from modules import jobs
from modules.logger import getLogger

TIMEOUT = 5

def main():
    """
    The main method.
    """
    logger = getLogger("checklist")
    logger.info("starting service")
    flow = Flow()
    logger.info(f"loaded flow {flow.getName}", flow.getName)

    while True:
        try:
            logger.info("requesting job")
            job = jobs.requestJob(flow.getName())

            if job is None:
                logger.info("no job found")
                time.sleep(TIMEOUT)
                continue

            logger.info(f"running job: {job}", flow.getName())
            results = flow.run(job['domain'])
            job['checks'] = results

            jobs.pushResults(job)
        except Exception:
            logger.error("an exception has occured", flow.getName())
            time.sleep(TIMEOUT)

if __name__ == "__main__":

    if os.environ.get("TIMEOUT") is not None:
        TIMEOUT = int(os.environ.get("TIMEOUT"))

    main()
