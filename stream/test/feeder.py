#!/usr/bin/env python2.6

import time
import operator
import os
import sys

from pprint import pprint

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import stream


## Test scenario based on ../example/feeder.py

def blocking_producer():
    for n in range(25):
        time.sleep(0.01)
        yield 42

f = lambda x: x ** 2

expected = blocking_producer() >> stream.map(f) >> stream.reduce(operator.add)


## Test cases

def test_ThreadedFeeder():
    result = stream.ThreadedFeeder(blocking_producer) >> stream.map(f) >> stream.reduce(operator.add)
    pprint(result)
    assert result == expected


def test_ForkedFeeder():
    result = stream.ForkedFeeder(blocking_producer) >> stream.map(f) >> stream.reduce(operator.add)
    pprint(result)
    assert result == expected


if __name__ == '__main__':
    import nose
    nose.main()
