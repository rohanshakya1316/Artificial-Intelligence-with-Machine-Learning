% 2. Write a program in Prolog to find max and min of two numbers

% Rule to find the maximum of two numbers
max(X, Y, X) :-
    X >= Y.

max(X, Y, Y) :-
    X < Y.

% Rule to find the minimum of two numbers
min(X, Y, X) :-
    X =< Y.

min(X, Y, Y) :-
    X > Y.