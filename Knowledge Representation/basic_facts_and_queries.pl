% 4.Write a prolog program to represent few basic facts and perform queries (Elephant is an animal. Elephant is bigger than horse) etc.

% Facts
animal(elephant).
animal(horse).
animal(lion).
animal(tiger).
animal(dog).
animal(cat).

bigger(elephant, horse).
bigger(horse, dog).
bigger(lion, dog).
bigger(tiger, cat).
bigger(elephant, lion).

color(elephant, gray).
color(horse, brown).
color(lion, yellow).
color(tiger, orange).
color(dog, black).
color(cat, white).