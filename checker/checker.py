import datetime

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
        a = re.findall(pattern, response)
        if len(a):
            return True
        return False
    except re.error:
        logger.exception("Error parsing regex")
        return False # Returning validation "error" regex fails, error could be handled better



def check(conf):
    valid = None
    with requests.session() as session:
        try:
            start = time.time()
            response = session.get(conf.url, timeout=60)
            end = time.time()
            if conf.regex is not None:
                valid = validate_response(response.text, conf.regex)
            return [conf.toJSON(), response.status_code, end-start, valid, datetime.datetime.now().isoformat()]
        except requests.exceptions.ConnectTimeout:
            # Timed out
            return [conf.toJSON(), -1, -1, None, datetime.datetime.now().isoformat()]
        except Exception as e:
            print("Unhandled exception in checking site:", conf, e)
            return [conf.toJSON(), -2, -2, None, datetime.datetime.now().isoformat()]
