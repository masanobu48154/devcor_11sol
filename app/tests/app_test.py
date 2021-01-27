import unittest
import requests
import socket
import re


class AppTest(unittest.TestCase):


    def setUp(self):
        self.url = 'http://localhost:5000'

    def test_welcome(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')

        self.assertEqual(status_code,200)
        self.assertIn('Welcome to Cisco DevNet.', content)
.
    def test_welcome_negative(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')

        self.assertEqual(status_code,200)
        self.assertNotIn('Welcome home.', content)

    def test_ip(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')

        self.assertEqual(status_code,200)
        ip_regex = 'IP address of the server is ([0-9]{1,3}\.){3}[0-9]{1,3}.'
        self.assertRegex(content, ip_regex)

if __name__ == "__main__":
    unittest.main()