# # Name :- Anshul Dahake
# # Roll No :- AI 2222
# # Lab Practical No. 1
# # Program :- LISP Output :-
# (format t "Hello, World!~%")
# ;; Arithmetic operations
# (print (+ 11 4))
# (print (- 15 10))
# (print (* 25 2))
# (print (/ 8 4))
# (print (- 10))
# (print (1+ 10))
# (print (1- 10))
# ;; Variable assignment
# (setq val1 50)
# (setq val2 50)
# (setq val3 30)
# ;; Comparison operations and min/max
# (format t "~%Equality (=): ~a" (= val1 val2))
# (format t "~%Inequality (/=): ~a" (/= val1 val3))
# (format t "~%Greater than (>): ~a" (> val1 val3))
# (format t "~%Less than (<): ~a" (< val3 val1))
# (format t "~%Less than or equal to (<=): ~a" (<= val3 val1))
# (format t "~%Max of val1 and val3: ~d" (max val1 val3))
# (format t "~%Min of val1 and val3: ~d~%" (min val1 val3))
# Program :- PROLOG Output :-
# :- initialization(main).
# main :-
# % Arithmetic operators
# write('Hello, World!'), nl,
# A is 11 + 4,
# B is 15 - 10,
# C is 25 * 2,
# D is 8 / 4,
# E is 10 mod 3,
# write('Addition: '), write(A), nl,
# write('Subtraction: '), write(B), nl,
# write('Multiplication: '), write(C), nl,
# write('Division: '), write(D), nl,
# write('Modulo: '), write(E), nl.