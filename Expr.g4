grammar Expr;

doc : field_size state_seg initialization next_state;

field_size : 'SIZE' COLON NUMBER;

state_seg : 'STATES' create_state+;

create_state : state_name COLON NUMBER;

initialization : 'INIT' state_name_bracket;

next_state :  create_next_state+;

// create next state
create_next_state: 'NEXT' state_name_bracket COLON EQUALS state_name_next;

state_name_bracket: OPEN_BR state_name_next CLOSE_BR ;

state_name : 's' NUMBER;

state_name_next : 's' NUMBER;










NUMBER : [0-9]+;
COLON : ':';
OPEN_BR : '(';
CLOSE_BR : ')';
EQUALS : '=';
T : 'T';
F : 'F';

ENDLINE : ('\r\n'|'\n'|'\r')+ -> skip;
WHITESPACE : [\t ]+ -> skip;