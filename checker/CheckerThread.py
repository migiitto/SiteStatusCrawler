import json
import threading
import time

from checker.checker import check


class CheckerThread(threading.Thread):
    def __init__(self, tid, name, producer, site):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.name = name
        self.producer = producer
        self.site = site
        self.kill = False
    def run(self):
        print("Started thread with id ", self.threadID)
        run_checker_function(self, self.producer, self.site)

    def killThread(self):
        self.kill = True

def run_checker_function(thread, producer, site):
    while not thread.kill:
        print("Sent status check to sitestatus_check topic", site)
        stats = check(site)
        producer.send("sitestatus_check", stats)
        time.sleep(site.period)
    return