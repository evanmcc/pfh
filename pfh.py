
from inspect import getframeinfo, currentframe
from types import TupleType, ListType
from sys import _getframe

#begin library code.

wc3doc = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'''

#
#  CORE GENERATION FUNCTIONS
#

def wrap(*blob, **kw):
    if kw.has_key('tagname'):
        tag = kw['tagname']
        del kw['tagname']
    else:
        tag = _getframe().f_back.f_code.co_name
    cr = ''
    if len(blob) > 1: 
        cr = '\n'
    return starttag(tag, cr, False, **kw) + endtag(tag, cr, *blob)

def bare(*blob, **kw):
    if kw.has_key('tagname'):
        tag = kw['tagname']
        del kw['tagname']
    else:
        tag = _getframe().f_back.f_code.co_name
    return starttag(tag, '', True, **kw)

def starttag(tag, cr, bare, **kw):
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

def endtag(tag, cr, *blob): 
    out = ''
    for b in blob:
        if type(b) == TupleType or \
                type(b) == ListType:
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
    return out+wrap(*blob, **kw)


# the below is an experiment in trying to do the rest of this 
# procedurally. it didn't work, but I am including it so as to 
# seal off a blind alley for the next time I give it a shot.

#wrap_tags = [ 'a', 'abbr', 'address' ] 
#namespace = locals() 

#for tag in wrap_tags:
    #kw['tagname'] = tag
#    def inner(*blob, **kw):
#        return wrap(*blob, **kw)
#    namespace[tag] = lambda *blob, **kw: wrap(*blob, **kw, tagname=tag)

# Tags requiring an end tag. 

def a(*blob, **kw):
    return wrap(*blob, **kw)

def abbr(*blob, **kw):
    return wrap(*blob, **kw)

def address(*blob, **kw):
    return wrap(*blob, **kw)
  
def b(*blob, **kw):
    return wrap(*blob, **kw)

def bdo(*blob, **kw):
    return wrap(*blob, **kw)

def big(*blob, **kw):
    return wrap(*blob, **kw)

def blockquote(*blob, **kw):
    return wrap(*blob, **kw)

def body(*blob, **kw):
    return wrap(*blob, **kw)

def button(*blob, **kw):
    return wrap(*blob, **kw)

def caption(*blob, **kw):
    return wrap(*blob, **kw)

def cite(*blob, **kw):
    return wrap(*blob, **kw)

def code(*blob, **kw):
    return wrap(*blob, **kw)

def colgroup(*blob, **kw):
    return wrap(*blob, **kw)

def dd(*blob, **kw):
    return wrap(*blob, **kw)

# namespace collision
#def del(*blob, **kw):
#    return wrap(*blob, **kw)

# namespace collision
#def def(*blob, **kw):
#    return wrap(*blob, **kw)

def div(*blob, **kw):
    return wrap(*blob, **kw)

def dl(*blob, **kw):
    return wrap(*blob, **kw)

def dt(*blob, **kw):
    return wrap(*blob, **kw)

def em(*blob, **kw):
    return wrap(*blob, **kw)

def fieldset(*blob, **kw):
    return wrap(*blob, **kw)

def form(*blob, **kw):
    return wrap(*blob, **kw)

def frameset(*blob, **kw):
    return wrap(*blob, **kw)

def h1(*blob, **kw):
    return wrap(*blob, **kw)

def h2(*blob, **kw):
    return wrap(*blob, **kw)

def h3(*blob, **kw):
    return wrap(*blob, **kw)

def h4(*blob, **kw):
    return wrap(*blob, **kw)

def h5(*blob, **kw):
    return wrap(*blob, **kw)

def h6(*blob, **kw):
    return wrap(*blob, **kw)

def head(*blob, **kw):
    return wrap(*blob, **kw)

#defined specially elsewhere, for now.
#def html(*blob, **kw):
#    return wrap(*blob, **kw)

def i(*blob, **kw):
    return wrap(*blob, **kw)

def iframe(*blob, **kw):
    return wrap(*blob, **kw)

def ins(*blob, **kw):
    return wrap(*blob, **kw)

def kbd(*blob, **kw):
    return wrap(*blob, **kw)

def label(*blob, **kw):
    return wrap(*blob, **kw)

def legend(*blob, **kw):
    return wrap(*blob, **kw)

def li(*blob, **kw):
    return wrap(*blob, **kw)

def map(*blob, **kw):
    return wrap(*blob, **kw)

def menu(*blob, **kw):
    return wrap(*blob, **kw)

def noframes(*blob, **kw):
    return wrap(*blob, **kw)

def noscript(*blob, **kw):
    return wrap(*blob, **kw)

def object(*blob, **kw):
    return wrap(*blob, **kw)

def ol(*blob, **kw):
    return wrap(*blob, **kw)

def optgroup(*blob, **kw):
    return wrap(*blob, **kw)

def option(*blob, **kw):
    return wrap(*blob, **kw)

def p(*blob, **kw):
    return wrap(*blob, **kw)

def pre(*blob, **kw):
    return wrap(*blob, **kw)

def q(*blob, **kw):
    return wrap(*blob, **kw)

def samp(*blob, **kw):
    return wrap(*blob, **kw)

def script(*blob, **kw):
    return wrap(*blob, **kw)

def select(*blob, **kw):
    return wrap(*blob, **kw)

def small(*blob, **kw):
    return wrap(*blob, **kw)

def span(*blob, **kw):
    return wrap(*blob, **kw)

def strong(*blob, **kw):
    return wrap(*blob, **kw)

def style(*blob, **kw):
    return wrap(*blob, **kw)

def sub(*blob, **kw):
    return wrap(*blob, **kw)

def sup(*blob, **kw):
    return wrap(*blob, **kw)

def table(*blob, **kw):
    return wrap(*blob, **kw)

def tbody(*blob, **kw):
    return wrap(*blob, **kw)

def td(*blob, **kw):
    return wrap(*blob, **kw)

def textarea(*blob, **kw):
    return wrap(*blob, **kw)

def tfoot(*blob, **kw):
    return wrap(*blob, **kw)

def th(*blob, **kw):
    return wrap(*blob, **kw)

def thead(*blob, **kw):
    return wrap(*blob, **kw)

def title(*blob, **kw):
    return wrap(*blob, **kw)

def tr(*blob, **kw):
    return wrap(*blob, **kw)

def tt(*blob, **kw):
    return wrap(*blob, **kw)

def ul(*blob, **kw):
    return wrap(*blob, **kw)

def var(*blob, **kw):
    return wrap(*blob, **kw)


# Tags forbidding an end tag.

def area(*blob, **kw):
    return bare(*blob, **kw)

def base(*blob, **kw):
    return bare(*blob, **kw)

def br(*blob, **kw):
    return bare(*blob, **kw)

def col(*blob, **kw):
    return bare(*blob, **kw)

def frame(*blob, **kw):
    return bare(*blob, **kw)

def hr(*blob, **kw):
    return bare(*blob, **kw)

def img(*blob, **kw):
    return bare(*blob, **kw)

def input(*blob, **kw):
    return bare(*blob, **kw)

# input subtypes, shortcuts for forms.

def submit(name, label='', image='', id='', class_=''):
    kw = {'type':'submit'} 
    if label:
        kw['value'] = label
    if image:
        kw['src'] = image
    if class_:
        kw['class_'] = class_
    if id:
        kw['id'] = id
    
    return input(**kw)

def passw(label='', image='', id='', class_=''):
    kw = {'type':'password'} 
    if label:
        kw['value'] = label
    if image:
        kw['src'] = image
    if class_:
        kw['class_'] = class_
    if id:
        kw['id'] = id
    
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

def newelt(elt, class_='', id=''):
    if not class_ and not id: 
        print 'must define class or id'
        return False
    def inner(*blob, **kw):
        if class_:
            kw['class_'] = class_
        if id:
            kw['id'] = id
        #this may be unsafe if you don't do 'from pfh import *'
        return globals()[elt](*blob, **kw)
    return inner

def newdiv(class_='', id=''): 
    return newelt('div', class_, id)   
def newspan(class_='', id=''):
    return newelt('span', class_, id)


