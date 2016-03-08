from sparqlparser.grammar import *

s = 'SELECT ?v WHERE {?v <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/TR/2003/CR-owl-guide-20030818/wine#VintageYear> .}'

r = parseQuery(s)

print(r.dump())