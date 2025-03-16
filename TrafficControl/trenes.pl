:- discontiguous l1/1, l6/1, u4/1, l2/1, l4/1, l5/1, u1/1, u7/1, u8/1.
:- dynamic u1/1, u2/1, u3/1, u4/1, u5/1, u6/1, u7/1, u8/1, l1/1, l2/1, l3/1, l4/1, l5/1, l6/1, s2/1, s4/1.

% Hechos iniciales
% s1(ocupada).
% s3(ocupada).
% s5(ocupada).

% s2(libre).
% s4(libre).
% u1(verde).

% Reglas de trenes

% Regla 1
l1(rojo):- u1(verde).

% Regla 2
l6(rojo) :- u6(verde).

% Regla 3
u2(rojo):- s1(ocupada).

% Regla 4
l2(rojo):- s2(ocupada).

% Regla 5
u3(rojo):- s3(ocupada).

% Regla 6
u4(rojo):- s3(ocupada).

% Regla 7
u5(rojo) :- s4(ocupada).

% Regla 7b: U5 = verde si S4 no está ocupada
u5(verde) :- \+ s4(ocupada).

% Regla 8
l5(rojo):- s5(ocupada).

% Regla 9
u1(rojo) :- u3(rojo), l3(rojo).
u1(rojo) :- u5(rojo), l5(rojo).

% Regla 10
l1(rojo) :- u3(rojo), l3(rojo).
l1(rojo) :- u5(rojo), l5(rojo).

% Regla 11
u6(rojo) :- u2(rojo), l2(rojo).
u6(rojo) :- u4(rojo), l4(rojo).

% Regla 12a: L6 = rojo si u2(rojo) y l2(rojo) son verdaderos, o si u4(rojo) y l4(rojo) son verdaderos
l6(rojo) :- u2(rojo), l2(rojo).
l6(rojo) :- u4(rojo), l4(rojo).

% Regla 12b: L6 = verde si no se cumple ninguna de las condiciones anteriores
l6(verde) :- \+ (u2(rojo), l2(rojo)), \+ (u4(rojo), l4(rojo)).

% Regla 13
u7(rojo):- u2(rojo), l2(rojo).

% Regla 14
u8(rojo):- u5(rojo), l5(rojo).

% Regla 15
u4(rojo):- u3(verde).

% Regla 16
l4(rojo):- l3(verde).

% Regla 17
l2(rojo):- u2(verde).

% Regla 18a: L3 = rojo si u3(verde) es verdadero
l3(rojo) :- u3(verde).

% Regla 18b: L3 = verde si u3(verde) no es verdadero
l3(verde) :- \+ u3(verde).

% Regla 19
l4(rojo):- u4(verde).

% Regla 20
l5(rojo):- u5(verde).

% Regla 21
u7(rojo) :- u1(verde).
u7(rojo) :- l1(verde).

% Regla 22
u8(rojo) :- u6(verde).
u8(rojo) :- l6(verde).

% Predicado para mostrar todas las conclusiones
mostrar_conclusiones :-
    writeln('Conclusiones:'),
    writeln('-------------'),
    (l1(X) -> writeln('L1 = rojo') ; writeln('L1 = verde')),
    (l6(X) -> writeln('L6 = rojo') ; writeln('L6 = verde')),
    (u2(X) -> writeln('U2 = rojo') ; writeln('U2 = verde')),
    (l2(X) -> writeln('L2 = rojo') ; writeln('L2 = verde')),
    (u3(X) -> writeln('U3 = rojo') ; writeln('U3 = verde')),
    (u4(X) -> writeln('U4 = rojo') ; writeln('U4 = verde')),
    (u5(X) -> writeln('U5 = rojo') ; writeln('U5 = verde')),
    (l5(X) -> writeln('L5 = rojo') ; writeln('L5 = verde')),
    (u1(X) -> writeln('U1 = rojo') ; writeln('U1 = verde')),
    (u6(X) -> writeln('U6 = rojo') ; writeln('U6 = verde')),
    (u7(X) -> writeln('U7 = rojo') ; writeln('U7 = verde')),
    (u8(X) -> writeln('U8 = rojo') ; writeln('U8 = verde')),
    (l4(X) -> writeln('L4 = rojo') ; writeln('L4 = verde')),
    (l3(X) -> writeln('L3 = rojo') ; writeln('L3 = verde')),
    writeln('-------------').

% Predicado para obtener las conclusiones una por una
recorrido(Conclusiones) :-
    findall(
        [Variable, Valor],
        (
            (l1(X), Variable = 'L1', Valor = X);
            (l6(X), Variable = 'L6', Valor = X);
            (u2(X), Variable = 'U2', Valor = X);
            (l2(X), Variable = 'L2', Valor = X);
            (u3(X), Variable = 'U3', Valor = X);
            (u4(X), Variable = 'U4', Valor = X);
            (u5(X), Variable = 'U5', Valor = X);
            (l5(X), Variable = 'L5', Valor = X);
            (u1(X), Variable = 'U1', Valor = X);
            (u6(X), Variable = 'U6', Valor = X);
            (u7(X), Variable = 'U7', Valor = X);
            (u8(X), Variable = 'U8', Valor = X);
            (l4(X), Variable = 'L4', Valor = X);
            (l3(X), Variable = 'L3', Valor = X)
        ),
        Conclusiones
    ).