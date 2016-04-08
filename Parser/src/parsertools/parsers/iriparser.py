'''
Created on 28 mrt. 2016

@author: jeroenbruijning
'''
from pyparsing import *
from parsertools.extras import separatedList
from parsertools.base import Parser
from parsertools import ParsertoolsException
from ipaddress import IPv6Address, IPv4Address

#
# Create the parser object
#

parser = Parser()

#
# Patterns
#

#    Some productions are ambiguous.  The "first-match-wins" (a.k.a.
#    "greedy") algorithm applies.  For details, see [RFC3986].
 
# sub-delims     = "!" / "$" / "&" / "'" / "(" / ")"
#                   / "*" / "+" / "," / ";" / "="
sub_delims = Word("!$&'()*+,;=", exact=1).setName('sub-delims')
                
# gen-delims     = ":" / "/" / "?" / "#" / "[" / "]" / "@"   
gen_delims = Word(':/?#[]@', exact=1).setName('gen_delims')

# reserved       = gen-delims / sub-delims
reserved = (gen_delims | sub_delims).setName('reserved')
 
# ALPHA          =  %x41-5A / %x61-7A   ; A-Z / a-z
ALPHA = Word(alphas, exact=1).setName('ALPHA')
 
# DIGIT          =  %x30-39 ; 0-9
DIGIT = Word(nums, exact=1).setName('DIGIT')

# HEXDIG         =  DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
HEXDIG = Word(nums + 'ABCDEF', exact=1).setName('HEXDIG')

# unreserved     = ALPHA / DIGIT / "-" / "." / "_" / "~"
unreserved = (ALPHA | DIGIT | Word('-._~', exact=1)).setName('unreserved')
  
# pct-encoded    = "%" HEXDIG HEXDIG
pct_encoded = ('%' + HEXDIG*2).leaveWhitespace().setName('pct_encoded')
parser.addElement(pct_encoded)
 
# dec-octet      = DIGIT                 ; 0-9
#                   / %x31-39 DIGIT         ; 10-99
#                   / "1" 2DIGIT            ; 100-199
#                   / "2" %x30-34 DIGIT     ; 200-249
#                   / "25" %x30-35          ; 250-255
dec_octet = (DIGIT | \
            Word('123456789', exact=1) + DIGIT | \
            '1' + DIGIT*2 | \
            '2' + Word('01234', exact=1) + DIGIT | \
            '25' + Word('012345', exact=1)).leaveWhitespace().setName('dec_octet')
parser.addElement(dec_octet)
            
# IPv4address    = dec-octet "." dec-octet "." dec-octet "." dec-octet
IPv4address = (dec_octet + ('.' + dec_octet)*3).leaveWhitespace().setName('IPv4address')
parser.addElement(IPv4address)

# h16            = 1*4HEXDIG
h16 = (HEXDIG + (Optional(HEXDIG))*3).leaveWhitespace().setName('h16')
parser.addElement(h16)
 
# ls32           = ( h16 ":" h16 ) / IPv4address
ls32 = ((h16 + ':' + h16) | IPv4address).leaveWhitespace().setName('ls32')
parser.addElement(ls32)

# IPv6address    =                            6( h16 ":" ) ls32
#                 /                       "::" 5( h16 ":" ) ls32
#                   / [               h16 ] "::" 4( h16 ":" ) ls32
#                   / [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32
#                   / [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32
#                   / [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32
#                   / [ *4( h16 ":" ) h16 ] "::"              ls32
#                   / [ *5( h16 ":" ) h16 ] "::"              h16
#                   / [ *6( h16 ":" ) h16 ] "::"
IPv6address =  (
                                                                          (h16 + ':')*6  + ls32  | \
                                                                 '::'   + (h16 + ':')*5  + ls32  | \
                        Optional(                        h16)  + '::'   + (h16 + ':')*4  + ls32  | \
                       (Optional(Optional(h16 + ':')*1 + h16)) + '::'   + (h16 + ':')*3  + ls32  | \
                       (Optional(Optional(h16 + ':')*2 + h16)) + '::'   + (h16 + ':')*2  + ls32  | \
                       (Optional(Optional(h16 + ':')*3 + h16)) + '::'   + (h16 + ':')*1  + ls32  | \
                       (Optional(Optional(h16 + ':')*4 + h16)) + '::'                    + ls32  | \
                       (Optional(Optional(h16 + ':')*5 + h16)) + '::'                    +  h16  | \
                       (Optional(Optional(h16 + ':')*6 + h16)) + '::' ).leaveWhitespace().setName('IPv6address')       
parser.addElement(IPv6address)
                
# IPvFuture      = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )
IPvFuture = ('v' + Optional(HEXDIG) + '.' + OneOrMore(unreserved | sub_delims | Literal(':'))).leaveWhitespace().setName('IPvFuture')
parser.addElement(IPvFuture)
                   
# IP-literal     = "[" ( IPv6address / IPvFuture  ) "]"
IP_literal = (Literal('[') + (IPv6address | IPvFuture) + Literal(']')).leaveWhitespace().setName('IP_literal')
parser.addElement(IP_literal)
 
# port           = *DIGIT
port = (ZeroOrMore(DIGIT)).leaveWhitespace().setName('port')
parser.addElement(port)
 
# scheme         = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
scheme = Combine(ALPHA + ZeroOrMore(ALPHA | DIGIT | Word('+-.', exact=1))).leaveWhitespace().setName('scheme')
parser.addElement(scheme)
 
# iprivate       = %xE000-F8FF / %xF0000-FFFFD / %x100000-10FFFD
iprivate = (Regex('0xE000-0xF8FF') | Regex('0xF0000-0xFFFFD') | Regex('0x100000-0x10FFFD')).leaveWhitespace().setName('iprivate')
parser.addElement(iprivate)
 
# ucschar        = %xA0-D7FF / %xF900-FDCF / %xFDF0-FFEF
#                   / %x10000-1FFFD / %x20000-2FFFD / %x30000-3FFFD
#                   / %x40000-4FFFD / %x50000-5FFFD / %x60000-6FFFD
#                   / %x70000-7FFFD / %x80000-8FFFD / %x90000-9FFFD
#                   / %xA0000-AFFFD / %xB0000-BFFFD / %xC0000-CFFFD
#                   / %xD0000-DFFFD / %xE1000-EFFFD
ucschar = (Regex('0xA0-0xD7FF')      | Regex('0xF900-0xFDCF')   | Regex('0xFDF0-0xFFEF')    | \
                  Regex('0x10000-0x1FFFD')  | Regex('0x20000-0x2FFFD') | Regex('0x30000-0x3FFFD')  | \
                  Regex('0x40000-0x4FFFD')  | Regex('0x50000-0x5FFFD') | Regex('0x60000-0x6FFFD')  | \
                  Regex('0x70000-0x7FFFD')  | Regex('0x80000-0x8FFFD') | Regex('0x90000-0x9FFFDu') | \
                  Regex('0xA0000-0xAFFFD')  | Regex('0xB0000-0xBFFFD') | Regex('0xC0000-0xCFFFDu') | \
                  Regex('0xD0000-0xDFFFD')  | Regex('0xE1000-0xEFFFD')).leaveWhitespace().setName('ucschar')
parser.addElement(ucschar)
 
# iunreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~" / ucschar
iunreserved = (ALPHA | DIGIT | Word('-._~', exact=1)).leaveWhitespace().setName('iunreserved')
parser.addElement(iunreserved)
 
# ipchar         = iunreserved / pct-encoded / sub-delims / ":" / "@"
ipchar = (iunreserved | pct_encoded | sub_delims | Word(':@', exact=1)).leaveWhitespace().setName('ipchar')
parser.addElement(ipchar)
 
# iquery         = *( ipchar / iprivate / "/" / "?" )
iquery = (ZeroOrMore(ipchar | iprivate | Word('/?', exact=1))).leaveWhitespace().setName('iquery')
parser.addElement(iquery)
 
# ifragment      = *( ipchar / "/" / "?" )     
ifragment = (ZeroOrMore(ipchar | Word('/?', exact=1))).leaveWhitespace().setName('ifragment')
parser.addElement(ifragment)
 
# isegment-nz-nc = 1*( iunreserved / pct-encoded / sub-delims / "@" )    ; non-zero-length segment without any colon ":"
isegment_nz_nc  = (OneOrMore(iunreserved | pct_encoded | sub_delims | Literal('@'))).leaveWhitespace().setName('isegment_nz_nc')
parser.addElement(isegment_nz_nc )
                   
# isegment       = *ipchar
isegment = (ZeroOrMore(ipchar)).leaveWhitespace().setName('isegment')
parser.addElement(isegment)
 
# isegment-nz    = 1*ipchar
isegment_nz = (OneOrMore(ipchar)).leaveWhitespace().setName('isegment_nz')
parser.addElement(isegment_nz)
 
# ipath-empty    = 0<ipchar>
ipath_empty = (Empty()).leaveWhitespace().setName('ipath_empty')
parser.addElement(ipath_empty)

# ipath-abempty  = *( "/" isegment )
ipath_abempty = (ZeroOrMore('/' + isegment)).leaveWhitespace().setName('ipath_abempty')
parser.addElement(ipath_abempty)
    
# ipath-absolute = "/" [ isegment-nz *( "/" isegment ) ]
ipath_absolute = ('/' + Optional(isegment_nz + ZeroOrMore('/' + isegment))).leaveWhitespace().setName('ipath_absolute')
parser.addElement(ipath_absolute)
    
# ipath-noscheme = isegment-nz-nc *( "/" isegment )
ipath_noscheme = (isegment_nz_nc + ZeroOrMore('/' + isegment)).leaveWhitespace().setName('ipath_noscheme')
parser.addElement(ipath_noscheme)
 
# ipath-rootless = isegment-nz *( "/" isegment )
ipath_rootless = (isegment_nz + ZeroOrMore('/' + isegment)).leaveWhitespace().setName('ipath_rootless')
parser.addElement(ipath_rootless)
 
# ipath          = ipath-abempty   ; begins with "/" or is empty
#                   / ipath-absolute  ; begins with "/" but not "//"
#                   / ipath-noscheme  ; begins with a non-colon segment
#                   / ipath-rootless  ; begins with a segment
#                   / ipath-empty     ; zero characters
ipath = (ipath_abempty | ipath_absolute | ipath_noscheme | ipath_rootless | ipath_empty).leaveWhitespace().setName('ipath')
parser.addElement(ipath)
                   
# ireg-name      = *( iunreserved / pct-encoded / sub-delims )
ireg_name = (ZeroOrMore(iunreserved | pct_encoded | sub_delims)).leaveWhitespace().setName('ireg_name')
parser.addElement(ireg_name)
 
# iuserinfo      = *( iunreserved / pct-encoded / sub-delims / ":" )
iuserinfo = (ZeroOrMore(iunreserved | pct_encoded | sub_delims)).leaveWhitespace().setName('iuserinfo')
parser.addElement(iuserinfo)
 
# ihost          = IP-literal / IPv4address / ireg-name
ihost = (IP_literal | IPv4address | ireg_name).leaveWhitespace().setName('ihost')
parser.addElement(ihost)
 
# iauthority     = [ iuserinfo "@" ] ihost [ ":" port ]
iauthority = (Optional(iuserinfo + '@') + ihost + Optional(':' + port)).leaveWhitespace().setName('iauthority')
parser.addElement(iauthority)
 
# irelative-part = "//" iauthority ipath-abempty
#                   / ipath-absolute
#                   / ipath-noscheme
#                   / ipath-empty
irelative_part = ('//' + iauthority + ipath_abempty | ipath_absolute | ipath_noscheme | ipath_empty).leaveWhitespace().setName('irelative_part')
parser.addElement(irelative_part)
 
# irelative-ref  = irelative-part [ "?" iquery ] [ "#" ifragment ]
irelative_ref = (irelative_part + Optional('?' + iquery) + Optional('#' + ifragment)).leaveWhitespace().setName('irelative_ref')
parser.addElement(irelative_ref)

# ihier-part     = "//" iauthority ipath-abempty
#                   / ipath-absolute
#                   / ipath-rootless
#                   / ipath-empty
ihier_part = ('//' + iauthority + ipath_abempty | ipath_absolute | ipath_rootless | ipath_empty).leaveWhitespace().setName('ihier_part')
parser.addElement(ihier_part)
                   
# absolute-IRI   = scheme ":" ihier-part [ "?" iquery ]                  
absolute_IRI = (scheme + ':' + ihier_part + Optional('?' + iquery)).leaveWhitespace().setName('absolute_IRI')
parser.addElement(absolute_IRI)
                   
# IRI            = scheme ":" ihier-part [ "?" iquery ] [ "#" ifragment ]
IRI = (scheme + ':' + ihier_part + Optional('?' + iquery) + Optional('#' + ifragment)).leaveWhitespace().setName('IRI')
parser.addElement(IRI)
                          
# IRI-reference  = IRI / irelative-ref
IRI_reference = (IRI | irelative_ref).leaveWhitespace().setName('IRI_reference')
parser.addElement(IRI_reference)

if __name__ == '__main__':
    pass
                          