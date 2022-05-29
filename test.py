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
        tmpr= 3.14*int(radius)*int(radius)
        tmpr= str(tmpr)
        rv = self.app.get(f'/circle/{radius}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'%s\n'%tmpr)

    def test_square(self):
        side = 7
        tmpr= int(side)*int(side)
        tmpr= str(tmpr)
        rv = self.app.get(f'/square/{side}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'%s\n'%tmpr)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
