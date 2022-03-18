import sys
import os

import yaml
import json

from subprocess import Popen, PIPE

class Flow:
    """A flow executor class
    """
    def __init__(self):
        self.load()

    def load(self):
        """Load the flow file (flow.yml).
        """
        with open("flow.yml", "r", encoding="utf-8") as stream:
            self.flow = yaml.safe_load(stream)

    def getName(self) -> str:
        """Get the name of the this flow.

        Returns:
            str: The name of the flow.
        """
        return self.flow['name']

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

        print(f"Starting flow {self.flow['name']} with {stages} stages.")

        for i in range(stages):
            stage = self.flow['stages'][i]

            print(f"Executing stage {i + 1}/{stages}: {stage['name']}")

            # Check if there are checks in the stage
            if stage['checks'] is None or len(stage['checks']) == 0:
                continue

            checks = []

            # Run all checks in stage
            for check in stage['checks']:
                checks.append(Popen([sys.executable, os.path.join(os.getcwd(), check), domain], stdout=PIPE, encoding="utf-8", env=env))

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
                    print("JSON Format error!")
                    print(f"Output: {output}")

        return results
