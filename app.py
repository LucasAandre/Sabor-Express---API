import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' # Um end point

response = requests.get(url) # O get() é um verbo do HTTP onde ele vai solicitar um recurso

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
    print(dados_json) # O print ficou enorme, pois puxou todos os dados disponíveis na url

else:
    print(f'O erro foi: {response.status_code}')
