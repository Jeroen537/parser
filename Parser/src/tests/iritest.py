'''
Created on 7 apr. 2016

@author: jeroenbruijning
'''
from parsertools.parsers.iriparser import parser
import parsertools

testcases = [
             'example://a/b/c/%7Bfoo%7D',
             'eXAMPLE://a/./b/../b/%63/%7bfoo%7d',
             'ftp://cnn.example.com&story=breaking_news@10.0.0.1/top_story.htm',
             'ftp://ftp.is.co.za/rfc/rfc1808.txt',
             'http://www.ietf.org/rfc/rfc2396.txt',
             'ldap://[2001:db8::7]/c=GB?objectClass?one',
             'mailto:John.Doe@example.com',
             'news:comp.infosystems.www.servers.unix',
             'tel:+1-816-555-1212',
             'telnet://192.0.2.16:80/',
             'urn:oasis:names:specification:docbook:dtd:xml:4.1.2'
             ]
          

for c in testcases:
    print('parsing {}'.format(c))
    r = parser.IRI(c)
    print(r.dump())


# 
# 5.4.1.  Normal Examples
# 
#       "g:h"           =  "g:h"
#       "g"             =  "http://a/b/c/g"
#       "./g"           =  "http://a/b/c/g"
#       "g/"            =  "http://a/b/c/g/"
#       "/g"            =  "http://a/g"
#       "//g"           =  "http://g"
#       "?y"            =  "http://a/b/c/d;p?y"
#       "g?y"           =  "http://a/b/c/g?y"
#       "#s"            =  "http://a/b/c/d;p?q#s"
#       "g#s"           =  "http://a/b/c/g#s"
#       "g?y#s"         =  "http://a/b/c/g?y#s"
#       ";x"            =  "http://a/b/c/;x"
#       "g;x"           =  "http://a/b/c/g;x"
#       "g;x?y#s"       =  "http://a/b/c/g;x?y#s"
#       ""              =  "http://a/b/c/d;p?q"
#       "."             =  "http://a/b/c/"
#       "./"            =  "http://a/b/c/"
#       ".."            =  "http://a/b/"
#       "../"           =  "http://a/b/"
#       "../g"          =  "http://a/b/g"
#       "../.."         =  "http://a/"
#       "../../"        =  "http://a/"
#       "../../g"       =  "http://a/g"
# 
# 5.4.2.  Abnormal Examples
# 
#    Although the following abnormal examples are unlikely to occur in
#    normal practice, all URI parsers should be capable of resolving them
#    consistently.  Each example uses the same base as that above.
# 
#    Parsers must be careful in handling cases where there are more ".."
#    segments in a relative-path reference than there are hierarchical
#    levels in the base URI's path.  Note that the ".." syntax cannot be
#    used to change the authority component of a URI.
# 
#       "../../../g"    =  "http://a/g"
#       "../../../../g" =  "http://a/g"
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Berners-Lee, et al.         Standards Track                    [Page 36]
# 
#  
# RFC 3986                   URI Generic Syntax               January 2005
# 
# 
#    Similarly, parsers must remove the dot-segments "." and ".." when
#    they are complete components of a path, but not when they are only
#    part of a segment.
# 
#       "/./g"          =  "http://a/g"
#       "/../g"         =  "http://a/g"
#       "g."            =  "http://a/b/c/g."
#       ".g"            =  "http://a/b/c/.g"
#       "g.."           =  "http://a/b/c/g.."
#       "..g"           =  "http://a/b/c/..g"
# 
#    Less likely are cases where the relative reference uses unnecessary
#    or nonsensical forms of the "." and ".." complete path segments.
# 
#       "./../g"        =  "http://a/b/g"
#       "./g/."         =  "http://a/b/c/g/"
#       "g/./h"         =  "http://a/b/c/g/h"
#       "g/../h"        =  "http://a/b/c/h"
#       "g;x=1/./y"     =  "http://a/b/c/g;x=1/y"
#       "g;x=1/../y"    =  "http://a/b/c/y"
# 
#    Some applications fail to separate the reference's query and/or
#    fragment components from the path component before merging it with
#    the base path and removing dot-segments.  This error is rarely
#    noticed, as typical usage of a fragment never includes the hierarchy
#    ("/") character and the query component is not normally used within
#    relative references.
# 
#       "g?y/./x"       =  "http://a/b/c/g?y/./x"
#       "g?y/../x"      =  "http://a/b/c/g?y/../x"
#       "g#s/./x"       =  "http://a/b/c/g#s/./x"
#       "g#s/../x"      =  "http://a/b/c/g#s/../x"
# 
#    Some parsers allow the scheme name to be present in a relative
#    reference if it is the same as the base URI scheme.  This is
#    considered to be a loophole in prior specifications of partial URI
#    [RFC1630].  Its use should be avoided but is allowed for backward
#    compatibility.
# 
#       "http:g"        =  "http:g"         ; for strict parsers
#                       /  "http://a/b/c/g" ; for backward compatibility
# 
# 
# ==========
# 
# 
#      example://a/b/c/%7Bfoo%7D
#       eXAMPLE://a/./b/../b/%63/%7bfoo%7d
#       
#             ftp://cnn.example.com&story=breaking_news@10.0.0.1/top_story.htm
#             
#           
#       ftp://ftp.is.co.za/rfc/rfc1808.txt
# 
#       http://www.ietf.org/rfc/rfc2396.txt
# 
#       ldap://[2001:db8::7]/c=GB?objectClass?one
# 
#       mailto:John.Doe@example.com
# 
#       news:comp.infosystems.www.servers.unix
# 
#       tel:+1-816-555-1212
# 
#       telnet://192.0.2.16:80/
# 
#       urn:oasis:names:specification:docbook:dtd:xml:4.1.2
#           
#           
# 
# 
# 5.4.1.  Normal Examples
# 
#       "g:h"           =  "g:h"
#       "g"             =  "http://a/b/c/g"
#       "./g"           =  "http://a/b/c/g"
#       "g/"            =  "http://a/b/c/g/"
#       "/g"            =  "http://a/g"
#       "//g"           =  "http://g"
#       "?y"            =  "http://a/b/c/d;p?y"
#       "g?y"           =  "http://a/b/c/g?y"
#       "#s"            =  "http://a/b/c/d;p?q#s"
#       "g#s"           =  "http://a/b/c/g#s"
#       "g?y#s"         =  "http://a/b/c/g?y#s"
#       ";x"            =  "http://a/b/c/;x"
#       "g;x"           =  "http://a/b/c/g;x"
#       "g;x?y#s"       =  "http://a/b/c/g;x?y#s"
#       ""              =  "http://a/b/c/d;p?q"
#       "."             =  "http://a/b/c/"
#       "./"            =  "http://a/b/c/"
#       ".."            =  "http://a/b/"
#       "../"           =  "http://a/b/"
#       "../g"          =  "http://a/b/g"
#       "../.."         =  "http://a/"
#       "../../"        =  "http://a/"
#       "../../g"       =  "http://a/g"
# 
# 5.4.2.  Abnormal Examples
# 
#    Although the following abnormal examples are unlikely to occur in
#    normal practice, all URI parsers should be capable of resolving them
#    consistently.  Each example uses the same base as that above.
# 
#    Parsers must be careful in handling cases where there are more ".."
#    segments in a relative-path reference than there are hierarchical
#    levels in the base URI's path.  Note that the ".." syntax cannot be
#    used to change the authority component of a URI.
# 
#       "../../../g"    =  "http://a/g"
#       "../../../../g" =  "http://a/g"
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Berners-Lee, et al.         Standards Track                    [Page 36]
# 
#  
# RFC 3986                   URI Generic Syntax               January 2005
# 
# 
#    Similarly, parsers must remove the dot-segments "." and ".." when
#    they are complete components of a path, but not when they are only
#    part of a segment.
# 
#       "/./g"          =  "http://a/g"
#       "/../g"         =  "http://a/g"
#       "g."            =  "http://a/b/c/g."
#       ".g"            =  "http://a/b/c/.g"
#       "g.."           =  "http://a/b/c/g.."
#       "..g"           =  "http://a/b/c/..g"
# 
#    Less likely are cases where the relative reference uses unnecessary
#    or nonsensical forms of the "." and ".." complete path segments.
# 
#       "./../g"        =  "http://a/b/g"
#       "./g/."         =  "http://a/b/c/g/"
#       "g/./h"         =  "http://a/b/c/g/h"
#       "g/../h"        =  "http://a/b/c/h"
#       "g;x=1/./y"     =  "http://a/b/c/g;x=1/y"
#       "g;x=1/../y"    =  "http://a/b/c/y"
# 
#    Some applications fail to separate the reference's query and/or
#    fragment components from the path component before merging it with
#    the base path and removing dot-segments.  This error is rarely
#    noticed, as typical usage of a fragment never includes the hierarchy
#    ("/") character and the query component is not normally used within
#    relative references.
# 
#       "g?y/./x"       =  "http://a/b/c/g?y/./x"
#       "g?y/../x"      =  "http://a/b/c/g?y/../x"
#       "g#s/./x"       =  "http://a/b/c/g#s/./x"
#       "g#s/../x"      =  "http://a/b/c/g#s/../x"
# 
#    Some parsers allow the scheme name to be present in a relative
#    reference if it is the same as the base URI scheme.  This is
#    considered to be a loophole in prior specifications of partial URI
#    [RFC1630].  Its use should be avoided but is allowed for backward
#    compatibility.
# 
#       "http:g"        =  "http:g"         ; for strict parsers
#                       /  "http://a/b/c/g" ; for backward compatibility


          