grammar Property;

pr : prevK k expression;

k: 'K' EQUALS NUMBER;

prevK: 'prevK' EQUALS NUMBER;


expression : andexpression;
andexpression : orexpression (AND orexpression)*;
orexpression : notexpression (OR notexpression)*;
notexpression : NOT atom | atom;
atom : IDENTIFIER NUMBER | LPAREN andexpression RPAREN | boolean ;

boolean :
    TRUE | FALSE;

LPAREN : '(' ;
RPAREN : ')' ;
TRUE : 'TRUE';
FALSE : 'FALSE';
AND : '&';
OR : '|';
NOT : '~';
EQUALS : '=';
NUMBER : [0-9]+;
IDENTIFIER : 'X';
ENDLINE : ('\r\n'|'\n'|'\r')+ -> skip;
WHITESPACE : [\t ]+ -> skip;
