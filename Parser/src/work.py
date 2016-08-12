from parsertools.parsers import sparqlparser 
from parsertools.parsers.sparqlparser import *

from parsertools.base import *

pat = Group(separatedList(INTEGER('label'), sep=SPARQLParser.SLASH)).setName('pat')
SPARQLParser.addElement(pat)

s = '123/456/789'

r = SPARQLParser.pat(s)

d1 = r.dump()

pat = Group(separatedList(INTEGER, sep=SPARQLParser.SLASH)('label')).setName('pat')
SPARQLParser.addElement(pat)

s = '123/456/789'

r = SPARQLParser.pat(s)

d2 = r.dump()

assert d1 == d2

print(d2)