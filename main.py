import json
import time
from kafka import KafkaProducer, KafkaConsumer

from checker.checker import check
from config import BOOTSTRAP_SERVERS, SECURITY_PROTOCOL, SSL_CA, SSL_CERT, SSL_KEY
from sites.sites import get_sites
"""
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_certfile=SSL_CERT,
                         ssl_keyfile=SSL_KEY,
                         ssl_cafile=SSL_CA,
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

consumer = KafkaConsumer("testtopic",
                         bootstrap_servers=BOOTSTRAP_SERVERS,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_certfile=SSL_CERT,
                         ssl_keyfile=SSL_KEY,
                         ssl_cafile=SSL_CA)
"""
def main():
    sites = get_sites()
    for s in sites:
        check(s)

main()