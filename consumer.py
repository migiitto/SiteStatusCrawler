import json
import time
import datetime

from kafka import KafkaConsumer

from checker.CheckerConf import CheckerConf
from config import SECURITY_PROTOCOL, BOOTSTRAP_SERVERS, SSL_CERT, SSL_KEY, SSL_CA
from sites.sites import insert_record

consumer = KafkaConsumer("sitestatus_check",
                         bootstrap_servers=BOOTSTRAP_SERVERS,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_certfile=SSL_CERT,
                         ssl_keyfile=SSL_KEY,
                         ssl_cafile=SSL_CA,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

while True:
    print("Checking consumer")
    for result in consumer:
        print("Got result", result)
        unpacked = result.value
        insert_record(
            CheckerConf.fromJSON(unpacked[0]),
            unpacked[1],
            unpacked[2],
            unpacked[3],
            datetime.datetime.fromisoformat(unpacked[4])
        )
    time.sleep(10)