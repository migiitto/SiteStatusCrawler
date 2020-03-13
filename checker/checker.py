import requests
import time
import re
import logging

from sites.sites import insert_record

logger = logging.getLogger("checker")
"""
The website checker should perform the checks periodically and collect the
HTTP response time, error code returned, as well as optionally checking the
returned page contents for a regexp pattern that is expected to be found on the
page.
"""


def validate_response(response, pattern):
    try:
        return re.match(pattern, response.text)
    except re.error:
        logger.exception("Error parsing regex")
        return False # Returning validation "error" regex fails, error could be handled better



def check(conf):
    valid = None
    with requests.session() as session:
        try:
            start = time.time()
            response = session.get(conf.url) #TODO: check if this is lazy
            end = time.time()
            if conf.regex is not None:
                valid = validate_response(response, conf.regex)
            insert_record(conf, response.status_code, end-start, valid)
        except requests.exceptions.ConnectTimeout:
            # Timed out
            insert_record(conf, -1, end - start, None)
        except Exception as e:
            print("Unhandled exception in checking site:", conf, e)
