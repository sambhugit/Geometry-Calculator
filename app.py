#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)
@app.route('/square')
def square(side):
    side= int(side)
    return str(side*side)+"\n"

@app.route('/circle')
def circle(radius):
    radius= int(radius)
    return str(3.14*radius*radius)+"\n"

@app.route('/')
def intro():
    return "This is a geometry calculator\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone
