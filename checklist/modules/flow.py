import sys
import os
import time

import yaml
import json

from subprocess import Popen, PIPE
from modules.logger import getLogger

class Flow:
    """A flow executor class
    """

    def __init__(self, logger):
        self.running = True

        self.logger = logger
        self.logger.info("loading flow")

        self.load()

    def load(self):
        """Load the flow file (flow.yml).
        """
        self.logger.info("loading flow file")
        with open("flow.yml", "r", encoding="utf-8") as stream:
            self.flow = yaml.safe_load(stream)

    def getName(self) -> str:
        """Get the name of the this flow.

        Returns:
            str: The name of the flow.
        """
        return self.flow['name']

    def stop(self):
        """
        Stop service
        """
        self.running = False

    def run(self, domain: str) -> list:
        """Run the flow on a specific domain.

        Args:
            domain (str): The domain to execute the flow on.

        Returns:
            list: A list of results from the indivdual checks.
        """
        stages = len(self.flow['stages'])

        results = []
        env = {}

        self.logger.info(f"Starting flow with {stages} stages.", self.getName())

        for i in range(stages):
            stage = self.flow['stages'][i]

            self.logger.info(f"Executing stage {i + 1}/{stages}: {stage['name']}", self.flow['name'])

            # Check if there are checks in the stage
            if stage['checks'] is None or len(stage['checks']) == 0:
                self.logger.info("no checks in the stage", self.flow['name'])
                continue

            checks = []

            # Run all checks in stage
            for check in stage['checks']:
                checks.append(Popen([sys.executable, os.path.join(os.getcwd(), check), domain], stdout=PIPE, encoding="utf-8", env=env))

            busy = True

            while busy and self.running:
                busy = False

                for check in checks:
                    busy = busy or check.poll() is None

                if busy and self.running:
                    time.sleep(0.01)

            if not self.running:
                self.logger.info("Killing sub processes.", self.flow['name'])
                for check in checks:
                    check.kill()

                self.logger.info("Killed all sub process, returning.", self.flow['name'])
                return None

            for check in checks:
                output, err = check.communicate()

                try:
                    res = json.loads(output)

                    # If not a list create a list from the result
                    if isinstance(res, list):
                        reslist = res
                    else:
                        reslist = [ res ]

                    for result in reslist:

                        # Add all results to the global results list
                        if "score" in result:
                            results.append(result)

                        # Register output for later stages
                        if "output" in result:
                            for key in result['output']:
                                env[key] = result['output'][key]

                except json.decoder.JSONDecodeError as err:
                    # JSON Decoding error logging
                    self.logger.error(f"JSON Format error: {err}", self.getName())
                    self.logger.error(f"Output: {output}", self.getName())
                except Exception as error:
                    self.logger.error(f"an exception has occured: {error}", self.getName())

        return results
