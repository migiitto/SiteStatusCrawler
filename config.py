import os
import json

#Kafka
BOOTSTRAP_SERVERS = json.loads(os.environ.get("BOOTSTRAP_SERVERS", '["migi-kafka-testing-msommarberg-6dbf.aivencloud.com:12673"]'))
SECURITY_PROTOCOL = "SSL"
SSL_CERT = "ssl/service.cert"
SSL_KEY = "ssl/service.key"
SSL_CA = "ssl/ca.pem"

#Postgresql
DATABASE_IP = os.environ.get("DATABASE_IP", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5432")
DATABASE_USER = os.environ.get("DATABASE_USER", "siteuser")
DATABASE_PASS = os.environ.get("DATABASE_PASS", "siteuser")
DATABASE_DB = os.environ.get("DATABASE_DB", "sitestatus")


TEST_DATABASE_IP = os.environ.get("DATABASE_IP", DATABASE_IP)
TEST_DATABASE_PORT = os.environ.get("DATABASE_PORT", DATABASE_PORT)
TEST_DATABASE_USER = os.environ.get("DATABASE_USER", DATABASE_USER)
TEST_DATABASE_PASS = os.environ.get("DATABASE_PASS", DATABASE_PASS)
TEST_DATABASE_DB = os.environ.get("DATABASE_DB", "sitestatus_test")