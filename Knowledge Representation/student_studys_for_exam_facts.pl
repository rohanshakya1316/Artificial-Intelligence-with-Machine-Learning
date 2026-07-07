/*
 5. Represent following facts using prolog: 
        If a student studies they will pass the exam. 
        If the student pass their exam they will be happy. 
        Radha studied for the exam. 
        Rakesh studied for the exam. 
        Anish studied for the exam. 
        Rekha did not study for her exam. 
        Bibek did not study for the exam 

        Using the facts, answer following: 
        i. Did Anish pass? 
        ii. List all the students that passed.
        iii. Did Rekha study?
        iv. List all the students that did not study.
*/

% Facts: Students who studied
studied(radha).
studied(rakesh).
studied(anish).

% Facts: Students who did not study
not_studied(rekha).
not_studied(bibek).

% Rule: If a student studies, they pass the exam
pass(X) :-
    studied(X).

% Rule: If a student passes, they are happy
happy(X) :-
    pass(X).

% Rule: If a student does not study, they fail the exam
fail(X) :-
    not_studied(X).

% Rule: If a student passes, they are happy
sad(X) :-
    fail(X).