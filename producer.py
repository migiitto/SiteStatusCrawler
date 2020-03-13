import datetime
import json
import signal
import sys
import threading
import time

from kafka import KafkaProducer, KafkaConsumer

from checker.CheckerConf import CheckerConf
from checker.CheckerThread import CheckerThread
from checker.checker import check
from config import BOOTSTRAP_SERVERS, SECURITY_PROTOCOL, SSL_CA, SSL_CERT, SSL_KEY
from sites.sites import get_sites, insert_record

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_certfile=SSL_CERT,
                         ssl_keyfile=SSL_KEY,
                         ssl_cafile=SSL_CA,
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

threads = []

def main():
    sites = get_sites()
    for s in sites:
        threads.append(CheckerThread(s.id, s.name, producer, s))
    for t in threads:
        t.start()



def signal_handler(sig, frame):
    global threads
    print('You pressed Ctrl+C, Please wait while threads are finishing.\n')
    for t in threads:
        print("Sent kill signal to thread:", t)
        t.killThread()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        try:
            time.sleep(1)
        except Exception:
            pass
