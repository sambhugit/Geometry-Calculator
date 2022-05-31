#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)
@app.route('/square/<side>')
def square(side):
    side= int(side)
    return str(side*side)+"\n"

@app.route('/circle/<radius>')
def circle(radius):
    radius= int(radius)
    a=2
    return str(3.14*radius*radius)+"\n"

@app.route('/sphere/<radius>')
def sphere(radius):
    radius= int(radius)
    return str(4*3.14*radius*radius)+"\n"

@app.route('/cuboid/<side>')
def cuboid(side):
    side= int(side)
    return str(6*side*side)+"\n"

@app.route('/spherevol/<radius>')
def spherevol(radius):
    radius= int(radius)
    return str(1.3*3.14*radius*radius*radius)+"\n"

@app.route('/cuboidvol/<side>')
def cuboidvol(side):
    side= int(side)
    return str(side*side*side)+"\n"

@app.route('/')
def intro():
    return "This is a geometry calculator\n"

if __name__ == '__main__':
    print("This is app.py")
    app.run(host='0.0.0.0')  # open for everyone
