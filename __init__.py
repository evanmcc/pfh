# See MIT-LICENSE in this directory for license information.

from inspect import getframeinfo, currentframe
from sys import _getframe

wc3doc = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'''

#  CORE GENERATION FUNCTIONS

def _wrap(*blob, **kw):
    if kw.get('__tagname'):
        tag = kw['__tagname']
        del kw['__tagname']
    else:
        tag = _getframe().f_back.f_code.co_name
    cr = ''
    if len(blob) > 1: 
        cr = '\n'
    return _starttag(tag, cr, False, **kw) + _endtag(tag, cr, *blob)

def _bare(*blob, **kw):
    if kw.get('__tagname'):
        tag = kw['__tagname']
        del kw['__tagname']
    else:
        tag = _getframe().f_back.f_code.co_name
    return _starttag(tag, '', True, **kw)

def _starttag(tag, cr, bare, **kw):
    out = at = bre = ''
    lk = len(kw)
    fix = ''
    if bare: 
        bre = '/'
    if lk > 0:
        at += ' '
        for (i, k) in enumerate(kw):
            if k[-1] == '_':
                fix = k[:-1]
                at += fix + '="' + kw[k] + '"'
            else:
                at += k + '="' + kw[k] + '"'
            if i != lk-1:
                at += ' '
    out = '<'+tag+at+bre+'>'+cr
    return out

def _endtag(tag, cr, *blob): 
    out = ''
    for b in blob:
        if type(b) in [tuple, list]:
            for i in b:
                out += i+cr
        else:
            out += b+cr
    out += '</'+tag+'>'
    return out

#
# TAGS
#

# Special Tags 
#  - maybe should just replace this with a doctype tag and have html act 
#    normally?

def html(*blob, **kw): 
    out = ''
    if not kw.has_key('doctype'): 
        out = wc3doc
    else:
        if kw['doctype'] == 'wc3':
            out = wc3doc
        else:
            out = kw['doctype']
        del kw['doctype']
    return out+_wrap(*blob, **kw)


_wrap_tags = [ 'a', 'abbr', 'address', 'b', 'bdo', 'big', 'blockquote',
              'body', 'button', 'caption', 'cite', 'code',
              'colgroup', 'dd',
              # namespace collisions
              # 'del', 'def', 'object',
              'div', 'dl', 'dt', 'em', 'form', 'frameset', 'fieldset',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
              'head', 'i', 'iframe', 'ins', 'kbd', 'label', 
              'legend', 'li', 'map', 'menu', 'noframes', 'noscript',
              'ol', 'optgroup', 'option', 'p', 'pre', 'q', 'samp',
              'script', 'select', 'small', 'span', 'strong', 'style',
              'sub', 'sup', 'table', 'tbody', 'td', 'textarea', 
              'tfoot', 'th', 'thead', 'title', 'tr', 'tt', 
              'ul', 'var'] 
_bare_tags = ['area', 'base', 'br', 'col', 'frame', 'hr', 'img',
             'input']
_namespace = locals() 

def _gen_fn(tag, fn):
    def inner(*blob, **kw):
        kw['__tagname'] = tag
        return fn(*blob, **kw)
    return inner 

for tag in _wrap_tags:
    _namespace[tag] = _gen_fn(tag, _wrap)

for tag in _bare_tags:
    _namespace[tag] = _gen_fn(tag, _bare)

# input subtypes, shortcuts for forms.

def submit(name, label='', image='', id_='', class_=''):
    kw = {'type':'submit'} 
    if label:
        kw['value'] = label
    if image:
        kw['src'] = image
    if class_:
        kw['class_'] = class_
    if id_:
        kw['id'] = id_
    
    return input(**kw)

def passw(label='', image='', id_='', class_=''):
    kw = {'type':'password'} 
    if label:
        kw['value'] = label
    if image:
        kw['src'] = image
    if class_:
        kw['class_'] = class_
    if id_:
        kw['id_'] = id_
    
    return input(**kw)

#end input subtypes

def link(*blob, **kw):
    return bare(*blob, **kw)

def meta(*blob, **kw):
    return bare(*blob, **kw)

def param(*blob, **kw):
    return bare(*blob, **kw)

# some utility functions for defining new divs and spans
# these are marginally useful, but more informative as an 
# example for making your own, similar functions.

def newelt(elt, class_='', id_=''):
    if not class_ and not id_: 
        print 'must define class or id'
        return False
    def inner(*blob, **kw):
        if class_:
            kw['class_'] = class_
        if id_:
            kw['id_'] = id_
        #this may be unsafe if you don't do 'from pfh import *'
        return globals()[elt](*blob, **kw)
    return inner

def newdiv(class_='', id_=''): 
    return newelt('div', class_, id_)   
def newspan(class_='', id_=''):
    return newelt('span', class_, id_)


