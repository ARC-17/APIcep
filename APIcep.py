import requests

cep = "01153000"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    request = requests.get(link)

    print(request)

    dic_request = request.json()

    uf = dic_request['uf']
    cidade = dic_request['localidade']
    bairro = dic_request['bairro']
    print(dic_request)
else:
    print("CEP Inválido")