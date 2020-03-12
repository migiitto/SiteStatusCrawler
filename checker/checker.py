import requests
import time
import re
import logging

logger = logging.getLogger("checker")
"""
The website checker should perform the checks periodically and collect the
HTTP response time, error code returned, as well as optionally checking the
returned page contents for a regexp pattern that is expected to be found on the
page.
"""


def validate_response(response, pattern):
    try:
        re.match(pattern, response.text)
    except re.error:
        logger.exception("Error parsing regex")



def check(conf):
    with requests.session() as session:
        try:
            start = time.time()
            response = session.get(conf.url) #TODO: check if this is lazy
            end = time.time()
            if conf.regex is not None:
                validate_response(response, conf.regex)

        except requests.exceptions.ConnectTimeout:
            # Timed out
            pass
        except ValueError:
            # Did not pass validation
            pass