#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_intro(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'This is a geometry calculator\n')

    def test_circle(self):
        radius= '5'
        rv = self.app.get(f'/circle/{radius}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'25\n')

    def test_hello_name(self):
        side = '7'
        rv = self.app.get(f'/hello/{side}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'49\n')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
