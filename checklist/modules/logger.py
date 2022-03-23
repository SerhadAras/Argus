import json
import sys
import json_logging
import logging

class CustomLogging(json_logging.JSONLogFormatter):
    """
    Class to customise json logging
    """
    def format(self, record):
        """"
        all the properties displayed when logging
        """

        if len(record.args) > 0:
            json_customized_log_object = ({
                "level": record.levelname,
                "service": record.name,
                "message": record.msg,
                "timestamp": record.created,     #in UNIX time
                "flow": record.args[0]
            })
        else:
            json_customized_log_object = ({
                "level": record.levelname,
                "service": record.name,
                "message": record.msg,
                "timestamp": record.created,     #in UNIX time
            })
        return json.dumps(json_customized_log_object)

def getLogger(name):
    """"
    return logger
    """
    json_logging.init_non_web(custom_formatter= CustomLogging, enable_json = True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    return logger
