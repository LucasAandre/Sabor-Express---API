from fastapi import FastAPI, Query
import requests

app = FastAPI() # fastapi é um módulo e FastAPI é uma classe
# Nesse caso estou criando uma instância da classe FastAPI
# Essa variável app representa a sua API inteira.

'''
@ indica um decorator.

app.get() significa que você está criando uma rota GET.

'/api/hello' é o caminho da rota.

Ou seja:

🔹 Quando alguém acessar http://localhost:8000/api/hello

→ vai cair na função hello_world.
'''
@app.get('/api/hello') # um endpoint da nossa rota. Esse endpoint está rodando localmente.
def hello_world():
    '''
    Endpoint que exibe a mensagem mais importante do mundo da programação
    '''
    return {'Hello': 'World'}

 # E o FastAPI automaticamente transforma isso em JSON:
'''
 {
  "Hello": "World"
}
 '''

'''
| Você retorna         | FastAPI transforma em | Cliente recebe              |
| -------------------- | --------------------- | --------------------------- |
| `{"Hello": "World"}` | JSONResponse          | `{"Hello": "World"}` (JSON) |
'''

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)): # Query(None) significa que o parâmetro é opcional.
    '''
    Endpoint para visualização dos cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url) # O get() é um verbo do HTTP onde ele vai solicitar um recurso

    if response.status_code == 200:
        dados_json = response.json() # Para puxar os dados da URL

        if restaurante is None:
            return {'Dados': dados_json} # Se nenhum restaurante foi selecionado, mostre o cardápio completo de todos os restaurantes.

        dados_restaurante = []

        for item in dados_json:
            if item['Company'] == restaurante:
                
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}
    
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}

# Não faremos um input para digitar o nome do restaurante e usar no endpoint, pois quando estamos falando de API, a informação vem de outra forma:
'''
1. O usuário digita no próprio link
2. O usuário digita no campo de busca da documentação automática do FastAPI (Swagger)
3. O usuário digita em um aplicativo frontend (site, celular, formulário)
'''
