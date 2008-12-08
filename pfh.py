
#the following is kind of ugly.
wc3doc = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0\
 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1\
-transitional.dtd">\n'


def wrap(tag, *blob, **kw):
    cr = ''
    if len(blob) > 1: 
        cr = '\n'
    out = '<'+tag+'>'+cr
    for b in blob:
        out += b+cr
    out += '</'+tag+'>'
    return out


def page(*blob, **kw): 
    out = ''
    if not kw.has_key('doctype') or \
            kw['doctype'] == 'wc3':
        out = wc3doc
    return out+wrap('html', *blob)

def head(*blob, **kw):
    return wrap('head', *blob)

def title(*blob, **kw):
    return wrap('title', *blob)

def body(*blob, **kw): 
    return wrap('body', *blob)

def p(*blob, **kw):
    return wrap('p', *blob)

def em(*blob, **kw):
    return wrap('em', *blob)

def h1(*blob, **kw):
    return wrap('h1', *blob)

def a(*blob, **kw):
    return wrap('a', *blob)

