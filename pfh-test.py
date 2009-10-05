#!/usr/bin/env python

from pfh import *
from sys import argv

def main():
    var = html(head(title('foo')),
               body(h1('title'), 
                    em('strong!'),
                    br(),
                    br(),
                    br(),
                    a('linky!', href="http://foo.com/bar/", 
                      alt='foo')))
    return var

if __name__ == '__main__':
    try:
        iter = int(argv[1])
    except:
        iter = 1

    pr = False
    for i in xrange(iter):
        if pr:
            print main()
        else:
            main
