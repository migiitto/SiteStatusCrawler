import os
import json

#Kafka
BOOTSTRAP_SERVERS = json.loads(os.environ.get("BOOTSTRAP_SERVERS", '["migi-kafka-testing-msommarberg-6dbf.aivencloud.com:12673"]'))
SECURITY_PROTOCOL = "SSL"
SSL_CERT = "service.cert"
SSL_KEY = "service.key"
SSL_CA = "ca.pem"

#Postgresql
DATABASE_IP = os.environ.get("DATABASE_IP", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", 5432)
DATABASE_USER = os.environ.get("DATABASE_USER", "siteuser")
DATABASE_PASS = os.environ.get("DATABASE_PASS", "siteuser")
DATABASE_DB = os.environ.get("DATABASE_DB", "sitestatus")
