from pyswip import Prolog
import time
import json


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)

    return results


def ask_question(query_string):
    answers = prolog_query(query_string)
    return answers


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += '"'
            continue
        json_str += c
    return json_str


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        # print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        print(">>>> ", text)


print(
    "Olá! Estou aqui para falar sobre a UFC de Itapajé."
)
flg = True
while flg:
    # Q/A
    print("\n\n")
    asked_question = str(input("O que você deseja saber sobre ela? ")).lower()

    if (
        "nome da universidade" in asked_question
        or "nome" in asked_question
    ):
        # Q: Nome da Universidade
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("O nome da Universidade é", "", question, answers)

    elif (
        "historia" in asked_question
        or "historia da universidade" in asked_question
        or "sobre" in asked_question
        or "detalhes" in asked_question
    ):
        # Q: Historia da Universidade.
        question = "History"
        query = "history(" + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "localização da universidade" in asked_question
        or "localização" in asked_question
    ):
        # Q: Onde a universidade está situada?
        question = "Location"
        query = "location(" + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "diretor" in asked_question
        or "diretor atual" in asked_question
        or "qual o diretor atualmente" in asked_question
    ):
        # Q: Qual o diretor atual da Universidade?
        question = "Diretor"
        query = "diretor(" + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "quantidade de cursos" in asked_question
        or "quantos cursos" in asked_question
    ):
        # Q Quantos cursos existem na universidade?
        question = "Number_of_faculties"
        query = "number_of_faculties(" + question + ")."
        answers = ask_question(query)
        say_answers("Existem ", "cursos na UFC - Itapajé", question, answers)

    elif (
        "nome dos cursos" in asked_question
        or "quais são os cursos" in asked_question
        or "cursos" in asked_question
    ):
        # Q Quais os cursos da Universidade?
        question = "Facultiy"
        query = "faculties(" + question + ")."
        answers = ask_question(query)
        say_answers("Existem 3 cursos: ", "", question, answers)

    elif "stop" in asked_question or "exit" in asked_question or "sair" in asked_question or "parar" in asked_question:
        print(">>>>> ", "Obrigada, espero que tenha gostado da pesquisa.")
        break

    else:
        if asked_question != "-----------------":
            confirmation = str(
                input(
                    "Desculpe, isso está fora do meu conhecimento. Você gostaria de continuar? "
                )
            ).lower()
            
            if "não" in confirmation or "no" in confirmation or "nao" in confirmation or "nope" in confirmation or "stop" in confirmation or "n" in confirmation:
                print(">>>>> ", "Obrigada, espero que tenha gostado da pesquisa.")
                break
            else:
                continue

        time.sleep(2)
