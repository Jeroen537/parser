from parsertools.parsers import sparqlparser 
from parsertools.parsers.sparqlparser import SPARQLParser as SP

q = '''
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>

SELECT ?p WHERE 
    {
        ?p a foaf:Person
    } 
'''

r = sparqlparser.parseQuery(q)
r.expandIris()
subjpath = r.searchElements(element_type=SP.IRIREF, value=None)[1]
print(subjpath.dump())
print(subjpath.getParent())
print(subjpath.getAncestors())
assert str(subjpath.getParent()) == '<http://xmlns.com/foaf/0.1/Person>'
assert str(subjpath.getAncestors()) == '[iri("<http://xmlns.com/foaf/0.1/Person>"), GraphTerm("<http://xmlns.com/foaf/0.1/Person>"), VarOrTerm("<http://xmlns.com/foaf/0.1/Person>"), GraphNodePath("<http://xmlns.com/foaf/0.1/Person>"), ObjectPath("<http://xmlns.com/foaf/0.1/Person>"), ObjectListPath("<http://xmlns.com/foaf/0.1/Person>"), PropertyListPathNotEmpty("a <http://xmlns.com/foaf/0.1/Person>"), TriplesSameSubjectPath("?p a <http://xmlns.com/foaf/0.1/Person>"), TriplesBlock("?p a <http://xmlns.com/foaf/0.1/Person>"), GroupGraphPatternSub("?p a <http://xmlns.com/foaf/0.1/Person>"), GroupGraphPattern("{ ?p a <http://xmlns.com/foaf/0.1/Person> }"), WhereClause("WHERE { ?p a <http://xmlns.com/foaf/0.1/Person> }"), SelectQuery("SELECT ?p WHERE { ?p a <http://xmlns.com/foaf/0.1/Person> }"), Query("PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?p WHERE { ?p a <http://xmlns.com/foaf/0.1/Person> }"), QueryUnit("PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?p WHERE { ?p a <http://xmlns.com/foaf/0.1/Person> }")]'


