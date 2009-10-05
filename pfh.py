
from inspect import getframeinfo, currentframe
from sys import _getframe

wc3doc = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n\
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'

#
#  CORE GENERATION FUNCTIONS
#

def wrap(*blob, **kw):
    tag = _getframe.f_back.f_code.co_name
    cr = ''
    if len(blob) > 1: 
        cr = '\n'
    return starttag(tag, cr, False, **kw) + endtag(tag, cr, *blob)

def bare(*blob, **kw):
    tag = _getframe.f_back.f_code.co_name
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
        out += b+cr
    out += '</'+tag+'>'
    return out

#
# TAGS
#

# Special Tags 
def html(*blob, **kw): 
    out = ''
    if not kw.has_key('doctype') or \
            kw['doctype'] == 'wc3':
        out = wc3doc
    return out+wrap(*blob)

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

def html(*blob, **kw):
    return wrap(*blob, **kw)

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

def link(*blob, **kw):
    return bare(*blob, **kw)

def meta(*blob, **kw):
    return bare(*blob, **kw)

def param(*blob, **kw):
    return bare(*blob, **kw)




