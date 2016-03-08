import sys
from pyparsing import *
from sparqlparser.grammar import *
from sparqlparser.grammar import stripComments
from sparqlparser.grammar_functest import printResults

s = '''
PREFIX ns: http://ds.tno.nl
PREFIX foaf: http://xmlns.com/foaf/0.1/

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
'''
parseQuery(s)