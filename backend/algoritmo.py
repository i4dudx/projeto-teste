# Importa o módulo para obter o ano atual
from datetime import datetime

# Obtém o ano atual

ano_atual = datetime.now().year

# solicita o ano de nascimento

ano_nascimento = int(input("em que ano você nasceu? "))

# calcula a idade

idade = ano_atual-ano_nascimento

# exibe o resultado

print(f"você tem {idade} anos ou fará {idade} anos este ano! ")