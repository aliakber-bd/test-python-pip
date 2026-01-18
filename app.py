#!/usr/bin/env python3
"""Test Python PIP project"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Test PIP project'

if __name__ == '__main__':
    print("Test project for PIP package manager")
