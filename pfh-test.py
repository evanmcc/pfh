#!/usr/bin/env python

from pfh import *

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
    for i in xrange(10000):
        main()
