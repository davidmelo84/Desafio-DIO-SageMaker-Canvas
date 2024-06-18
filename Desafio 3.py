# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um modelo e retornar sua respectiva aplicação.
def aplicar_modelos(modelo):
    if modelo == "Jurassic-2":
        return "Processamento de linguagem natural e geração de texto"

    elif modelo == "Amazon Titan":
        return "Análises de dados complexos"

    elif modelo == "Claude 2":
        return "Análises preditivas em tempo real"

    elif modelo == "Falcon":
        return "Tarefas de classificação e regressão"

    elif modelo == "MPT":
        return "Aprendizado de transferência para diferentes domínios de dados"

    else:
        return "Modelo desconhecido"

print(aplicar_modelos(entrada))
