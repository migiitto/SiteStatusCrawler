import datetime
import json
import time
import unittest

from kafka import KafkaConsumer, KafkaProducer

from checker.CheckerConf import CheckerConf
from checker.checker import validate_response, check
from config import DATABASE_IP, DATABASE_PORT, DATABASE_USER, DATABASE_PASS, DATABASE_DB, BOOTSTRAP_SERVERS, \
    SECURITY_PROTOCOL, SSL_CERT, SSL_KEY, SSL_CA
from database.database import get_conn, get_cursor


class TestDatabase(unittest.TestCase):
    def test_configuration_not_empty(self):
        mandatory_config_db = [DATABASE_IP,
                            DATABASE_PORT,
                            DATABASE_USER,
                            DATABASE_PASS,
                            DATABASE_DB]
        self.assertTrue(all(len(c) != 0 for c in mandatory_config_db))

    def test_connection(self):
        self.assertIsNotNone(get_cursor(get_conn()))

class TestCheckerConf(unittest.TestCase):
    jsonstr = '{"id": 1, "name": "test", "url": "https://www.google.com", "regex": null, "period": 60}'
    sql = [1, "test", "https://www.google.com", 60, None]

    def test_conf_builder(self):
        conf1 = CheckerConf.fromJSON(self.jsonstr)
        conf2 = CheckerConf.fromSQL(self.sql)
        self.assertEqual(conf1.toJSON(), conf2.toJSON())

    def test_checker(self):
        conf1 = CheckerConf.fromJSON(self.jsonstr)
        response = check(conf1)
        self.assertEqual(conf1.toJSON(), response[0]) #configuration
        self.assertGreater(response[1], 0) #statuscode
        self.assertLess(response[2], 10) # response time in sec
        self.assertIs(response[3], None) # regex
        self.assertEqual(datetime.datetime.now()-datetime.datetime.fromisoformat(response[4]) < datetime.timedelta(seconds=1), True) # timestamp in isoformat

class TestConsumerProducer(unittest.TestCase):
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
                             ssl_cafile=SSL_CA,
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    timestamp = datetime.datetime.now().isoformat()

    def test_producer(self):
        ret = self.producer.send("testtopic", self.timestamp)
        time.sleep(2)
        self.assertIs(ret.is_done, True)

    def test_consumer(self):
        """
        for consumable in self.consumer:
            if consumable.value == self.timestamp:
                self.assertEqual(True, True)
        self.assertEqual(True, False)
        """
        pass
class TestChecker(unittest.TestCase):

    def test_validate_response(self):
        pattern = "<title[^>]*>(.*?)</title>"
        text = "<title>Google</title>"
        self.assertIs(validate_response(text, pattern), True)
        invalid_text = "<html><body>500 Server Error</body></html>"
        self.assertIs(validate_response(invalid_text, pattern), False)



if __name__ == '__main__':
    unittest.main()