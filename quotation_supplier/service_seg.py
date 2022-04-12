import requests
import json

def login():
  payload = json.dumps({
    "username": "USER",
    "password": "PASSWORD"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  login = requests.post('URL', headers=headers, data=payload).text


  login_json = json.loads(login)
  token = login_json['token']
  return token


def quotation_seg(token, availability, id, name, supplier_id):
  payload = json.dumps(
    [
      {
        "active": True,
        "availability": availability, # DISPONIBILIDADE ID
        "id": id, # CODPROD
        "name": f"{name}", # CODFABRICANTE
        "supplier_id": supplier_id # FORNECEDOR ID
      }
    ]
  )
  headers = {
    'Authorization': f'{token}',
    'Content-Type': 'application/json',
  }

  quotation = requests.post('URL/quotation?id=id', headers=headers, data=payload) # Requisição de alteração

  print(name, ' - ',availability,' -> ', quotation) # Alteração realizada










