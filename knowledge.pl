name('Universidade Federal do Ceará - Campus de Anita').
location('O Campus Jardins de Anita fica situado no município de Itapajé - CE, localizado a aproximadamente 130km da capital do Estado.').
diretor('Prof. Márcio Veras Correa, mestrado e doutorado em Economia').
history('Em setembro de 2021 foram iniciadas as atividades acadêmicas no novo campus da Universidade Federal do Ceará (UFC) localizado em Itapajé, a 137 Km de Fortaleza. A nova estrutura, intitulada Jardins de Anita, oferta três cursos de graduação tecnológica: Segurança da Informação, Análise e Desenvolvimento de Sistemas e Ciência de Dados.
Apesar de inicialmente ter considerado ofertar licenciaturas, a UFC optou por manter um foco na área de tecnologia da informação').
number_of_faculties('3').

faculties('Segurança da Informação, Análise e Desenvolvimento de Sistemas e Ciência de Dados').

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

history(X, Y) :-
    name(X),
    history(Y).
location(X, Y) :-
    name(X),
    location(Y).
diretor(X, Y) :-
    name(X),
    diretor(Y).
number_of_faculties(X, Y) :-
    name(X),
    number_of_faculties(Y).

faculties(X, Y) :-
    name(X),
    faculties(Y).
