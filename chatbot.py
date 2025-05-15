import datetime
import random

print("Olá! Eu sou o ChatGPTinho, seu assistente virtual.")
nome = input("Antes de começarmos, qual é o seu nome? ")
print(f"Prazer em te conhecer, {nome}!")

while True:
    pergunta = input("\nEm que posso te ajudar? (Digite 'sair' para encerrar): ").lower()

    if "hora" in pergunta or "horas" in pergunta:
        agora = datetime.datetime.now()
        print(f"Agora são {agora.strftime('%H:%M')}.")

    elif "data" in pergunta:
        hoje = datetime.date.today()
        print(f"Hoje é {hoje.strftime('%d/%m/%Y')}.")

    elif "seu nome" in pergunta or "quem é você" in pergunta:
        print("Eu sou o ChatGPTinho, um chatbot simples criado em Python!")

    elif "tudo bem" in pergunta or "como vai" in pergunta:
        print("Estou ótimo! E você, como está se sentindo?")

    elif "triste" in pergunta:
        print("Sinto muito por isso. Lembre-se: dias difíceis também passam. Você é forte!")

    elif "feliz" in pergunta or "contente" in pergunta:
        print("Que ótimo saber disso! Continue espalhando essa energia positiva!")

    elif "ansioso" in pergunta or "ansiosa" in pergunta:
        print("Tente respirar fundo. Um passo de cada vez. Você vai conseguir!")

    elif "obrigado" in pergunta or "valeu" in pergunta:
        print("De nada! Estou sempre por aqui.")

    elif "piada" in pergunta:
        piadas = [
            "Por que o computador foi ao médico? Porque ele pegou um vírus!",
            "O que o zero disse para o oito? Belo cinto!",
            "Por que o Python é tão calmo? Porque ele não dá erro... ele lança exceção!"
        ]
        print(random.choice(piadas))

    elif "motivação" in pergunta or "frase" in pergunta:
        frases = [
            "Acredite em você! Todo especialista já foi um iniciante.",
            "O sucesso é a soma de pequenos esforços repetidos todos os dias.",
            "Você é capaz de muito mais do que imagina."
        ]
        print(random.choice(frases))

    elif "clima" in pergunta or "tempo" in pergunta:
        print("Eu ainda não tenho acesso à previsão do tempo, mas espero que esteja um ótimo dia aí!")

    elif "curso" in pergunta or "faculdade" in pergunta:
        print("Estudar T.I. é um ótimo caminho! Continue firme, você vai longe!")

    elif "filme" in pergunta:
        print("Eu curto ficção científica. Já assistiu 'O Jogo da Imitação'?")

    elif "esporte" in pergunta or "futebol" in pergunta:
        print("Eu sou fã de futebol digital! Mas confesso que gosto quando o Brasil joga bem!")

    elif pergunta == "sair":
        print("Até logo! Foi um prazer conversar com você.")
        break

    else:
        print("Desculpe, ainda não sei responder isso. Tente perguntar outra coisa.")