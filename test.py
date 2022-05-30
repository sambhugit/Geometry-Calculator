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
        self.assertEqual(rv.data, b'78.5\n')
        
   def test_sphere(self):
        radius= '5'
        rv = self.app.get(f'/sphere/{radius}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'314\n') 
        
   def test_spherevol(self):
        radius= '5'
        rv = self.app.get(f'/spherevol/{radius}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'510.25\n')

    def test_square(self):
        side = '7'
        tmpr= int(side)*int(side)
        tmpr= str(tmpr)
        rv = self.app.get(f'/square/{side}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'49\n')
    
    def test_cuboid(self):
        side = '7'
        rv = self.app.get(f'/cuboid/{side}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'294\n')
        
    def test_cuboidvol(self):
        side = '7'
        rv = self.app.get(f'/cuboid/{side}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'343\n')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
