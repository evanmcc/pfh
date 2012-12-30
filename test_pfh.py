#!/usr/bin/env python

from __future__ import absolute_import

from unittest import TestCase, main
from __init__ import *
from time import sleep

special_tags = [ 'html' ]

wrap_tags = ['a', 'abbr', 'address', 'b', 'bdo', 'big', 
             'blockquote', 'body', 'button', 'caption', 'cite',
             'code', 'colgroup', 'dd', 'div', 'dl', 'dt', 'em',
             'fieldset', 'form', 'frameset', 'h1', 'h2', 'h3',
             'h4', 'h5', 'h6', 'head', 'i', 'iframe', 
             'ins', 'kbd', 'label', 'legend', 'li', 'map', 'menu', 
             'noframes', 'noscript', 'ol', 'optgroup', 
             'option', 'p', 'pre', 'q', 'samp', 'script', 'select', 
             'small', 'span', 'strong', 'style', 'sub', 'sup', 
             'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 
             'thead', 'title', 'tr', 'tt', 'ul', 'var'] 

bare_tags = ['area', 'base', 'br', 'col', 'frame', 'hr', 'img', 'input']

attr_list = ['name', 'id', 'class', 'flarg'] 

class test_pfh(TestCase):
    def setUp(self):
        pass

    def test_html(self):
        assert(html('foo') == wc3doc+"<html>foo</html>")
        assert(html('foo', doctype='wc3') == wc3doc+"<html>foo</html>")
        dt = '<!DOCTYPE html>\n'
        assert(html('foo', doctype=dt) == dt+"<html>foo</html>")

    def test_wrap(self):
        namespace = globals()
        for tag in wrap_tags:
            assert(namespace[tag]('foo') == 
                   "<%s>foo</%s>" % (tag, tag))

    def test_bare(self):
        namespace = globals()
        for tag in bare_tags:
            assert(namespace[tag]() == 
                   "<%s/>" % tag)
     
    def test_wrap_attrs(self):
        d = {}
        at = ''
        attr_list.sort()
        for attr in attr_list:
            d[attr] = attr
            at += '%s=\"%s\" ' % (attr, attr)
        at = at[:-1]
        results = a('foo', **d).split()[1:]
        results[-1] = results[-1].split('>')[0]
        for result in results:
            l = attr_list[:]
            r = result.split('=')[0]
            assert(r in l)
            l.remove(r)
            assert(r not in l)

    def test_bare_attrs(self):
        d = {}
        at = ''
        attr_list.sort()
        for attr in attr_list:
            d[attr] = attr
            at += '%s=\"%s\" ' % (attr, attr)
        at = at[:-1]
        results = input(**d).split()[1:]
        results[-1] = results[-1].split('>')[0]
        for result in results:
            l = attr_list[:]
            r = result.split('=')[0]
            assert(r in l)
            l.remove(r)
            assert(r not in l)

    def test_factories(self):
        content = newdiv(class_='content')
        content_id = newdiv(id_='content')
        freaky = newspan(class_='freaky')
        freaky_id = newspan(id_='freaky')
        assert(content('foo') ==
               "<div class=\"content\">foo</div>")
        assert(content_id('foo') ==
               "<div id=\"content\">foo</div>")
        assert(freaky('foo') ==
               "<span class=\"freaky\">foo</span>")
        assert(freaky_id('foo') ==
               "<span id=\"freaky\">foo</span>")

if __name__ == '__main__':
    main()
