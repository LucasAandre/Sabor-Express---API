import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' # Um endpoint

response = requests.get(url) # O get() é um verbo do HTTP onde ele vai solicitar um recurso

'''
Ao lidar com APIs e dados externos, é uma prática valiosa salvar e organizar esses dados para facilitar 
futuras análises ou utilizações. Existe uma biblioteca em Python chamada requests, que é uma biblioteca 
popular para fazer requisições HTTP. Ela simplifica o processo de enviar solicitações, seja para obter 
informações de uma API, interagir com serviços web ou realizar outras operações que envolvam comunicação via HTTP.
'''

'''
Ao acessar a url, não esperamos uma pasta / tela bonita. Esperamos dados!
'''

print(response) # <Response [200]>

'''
200 significa que a solicitação foi atendida com sucesso.
404 significa que o link não foi encontrado.

O nome desses números é STATUS CODE
'''

if response.status_code == 200:
    dados_json = response.json() # Para puxar os dados da URL
    dados_restaurante = {}

    for item in dados_json:
        nome_restaurante = item['Company']

        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = [] # Vou criar uma lista dentro do dicionário (cada chave, será uma lista. Cada lista terá as informações de um restaurante)
        
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'O erro foi: {response.status_code}')

# print(dados_restaurante['KFC'])

# Criando arquivos com Python:
for nome_restaurante, dados in dados_restaurante.items(): # aqui ele trás o nome da chave (nome do restaurante) e os dados presentes na chave
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante: # w = write (ou seja, quero escrever nesse arquivo que será criado) --> será escrito os dados de dados_restaurante
        json.dump(dados, arquivo_restaurante, indent=4) # indent=4 → Faz a formatação “bonita”, com recuo de 4 espaços (para leitura humana). Sem indent, o JSON ficaria tudo em uma linha só.
    '''
    O open() cria o arquivo
    O json.dump() escreve o conteúdo dentro dele
    '''
