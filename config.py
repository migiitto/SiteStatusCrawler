import os
import json

BOOTSTRAP_SERVERS = json.loads(os.environ.get("BOOTSTRAP_SERVERS", '["migi-kafka-testing-msommarberg-6dbf.aivencloud.com:12673"]'))
SECURITY_PROTOCOL = "SSL"
SSL_CERT = "service.cert"
SSL_KEY = "service.key"
SSL_CA = "ca.pem"
