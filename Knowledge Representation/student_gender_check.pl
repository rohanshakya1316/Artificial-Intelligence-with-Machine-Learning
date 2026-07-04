% 1. Write a program in Prolog to categorize male and female students in class


% Facts: Male students
male(rohan).
male(samir).
male(ramesh).
male(akash).

% Facts: Female students
female(sita).
female(gita).
female(priya).
female(anita).

% Rule to check whether a student is male
student_male(X) :-
    male(X).

% Rule to check whether a student is female
student_female(X) :-
    female(X).