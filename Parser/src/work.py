# -*- coding: UTF-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from pyparsing import *

def printResults(l, rule, dump=False):
    
#     element = eval('SPARQLParser.' + rule)
    for s in l:
        print(s, len(s), type(s))
        r = rule.parseString(s, parseAll=True)
        while len(r) == 1 and isinstance(r[0], ParseResults):
            r = r[0]
        rendering = str(r[0].encode('utf-8)'))
        rendering = r[0]
        print('rendering: {} (type={})'.format(rendering, type(rendering)))
#         try:
#             checkIri(r[0])
#         except NoPrefixError:
#             warnings.warn('No prefix declaration found for prefix, ignoring')
        assert ''.join(r[0].__str__().upper().split()) == ''.join(s.upper().split()), 'Parsed expression: "{}" conflicts with original: "{}"'.format(r[0].__str__(), s)
        if s != rendering:
            print()
            print(rule)
            print('\nParse :', s)
            print('Render:', rendering)
            print('Note: rendering (len={}) differs from input (len={})'.format(len(rendering), len(s)))
        if dump:
            print('\ndump:\n')
            print(r[0].dump())
            print()
            
PN_CHARS_BASE_e = '[A-Za-z\uBBC0-\uBBD6]'
PN_CHARS_BASE = Regex(PN_CHARS_BASE_e)

# l = ['a', 'Z', '\uBBC1'.encode('utf-8')]
l = ['a', 'Z', '\uBBC1']
printResults(l, PN_CHARS_BASE, dump=False)