from sparqlparser.grammar import *

s = '''
PREFIX ns: <http://ds.tno.nl>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema>

SELECT ?p ?t WHERE
{
?p a foaf:Person .
?p ns:hasTemp ?t .
?p ns:hasAge ?a .
?t a ns:TempInC .
FILTER ( (datatype(?t) = xsd:float) &&
( ?t > 37.0 ) &&
( ?a < 37.0 )
).
}
'''[1:-1]

r = parseQuery(s)

print(r.dump())