# MARKET+ API

A [Market+](https://capstone-api-q3.herokuapp.com/) tem como intuito ajudar a comunidade onde poderá pesquisar os produtos em nosso banco de dados, e atualizar os preços de acordo com os supermercados, ranqueando estes de acordo com o menor preço registrado. 


## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PATCH` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |



<h3 align='center'> Cadastro de usuário</h3>

`POST /register - para cadastro de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Gabriela",
	"city": "Apucarana",
	"state":"PR",
	"country": "Brasil", 
	"email": "gabriela@email.com",
	"password": "1234"
	
}

```
Caso dê tudo certo, a resposta será assim:

`POST /register - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": ,
  "name": "Gabriela",
  "city": "Apucarana",
  "state": "PR",
  "country": "Brasil",
  "email": "gabriela@email.com"
}
```

<h3 align='center'> Login de usuário</h3>
`POST /login_users - para login de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"email": "gabrielas@email.com",
	"password": "1234"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /login_users - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3NDY0MiwianRpIjoiNWExNTFhNjQtNmYzOS00YjU2LTgzZWQtNjQxM2QxN2JlZjhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImdhYnJpZWxhIiwiY2l0eSI6ImFwdWNhcmFuYSIsInN0YXRlIjoiUFIiLCJjb3VudHJ5IjoiQnJhc2lsIiwiZW1haWwiOiJnYWJyaWVsYXNAZW1haWwuY29tIn0sIm5iZiI6MTYzOTA3NDY0MiwiZXhwIjoxNjM5MDc1NTQyfQ.SU8PBco6gZaLVtsOViDo4werwJHi3GcAkxxsbIZt3rk"
}
```
<h3 align='center'> Buscar usuários</h3>
`GET /users -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /users - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "kaio",
    "city": "brasólia",
    "state": "DF",
    "country": "Brasil",
    "email": "kaio@email.com",
    "sugestions": [],
    "favorite_products": []
  }
]
```
<h3 align='center'> Editar usuário</h3>
`PATCH /users/1 -  FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Gabriela Rodrigues"
  
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /users/1 - FORMATO DA RESPOSTA - 201`

```json

{
  "id":1,
  "name": "Gabriela Rodrigues",
  "city": "Apucarana",
  "state": "PR",
  "country": "Brasil",
  "email": "gabriela@email.com"
}
```

<h3 align='center'> Deletar usuário</h3>
`DELETE /users/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`DELETE /users/1 - FORMATO DA RESPOSTA - 201`
""
<h3 align='center'> Cadastro de mercado</h3>
`POST /stores - para cadastro de produtos FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /stores - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111"
}
```

<h3 align='center'> Cadastro de mercado</h3>
`POST /login_stores - para cadastro de mercados FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111"
  "password": "1234"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /stores - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111",
  "password": "1234"
}
```


<h3 align='center'> Login de mercado</h3>
`POST /login_stores - para logar em mercados FORMATO DA REQUISIÇÃO `

```json
{
	"cnpj": "11111111111111",
	"password": "1234"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /login_stores - FORMATO DA RESPOSTA - STATUS 201`

```json
{
 
}
```

<h3 align='center'> Buscar mercados</h3>
`GET /stores -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`GET /sugestions - FORMATO DA RESPOSTA - 201`
```json
[
  {
  "id": 1,
  "name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111"
  }
]
```

<h3 align='center'> Buscar mercado específico</h3>
`GET /stores/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`GET /sugestions/1 - FORMATO DA RESPOSTA - 201`
```json
[
  {
  "id": 1,
  "name": "Muffato",
	"address": "apucarana",
	"city":"apucarana",
	"state": "PR",
	"phone_number":"996173170",
	"cnpj": "11111111111111"
}
]
```
<h3 align='center'> Deletar mercado</h3>
`DELETE /stores/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`DELETE /stores/1 - FORMATO DA RESPOSTA - 201`
""


<h3 align='center'> Cadastro de produtos</h3>
`POST /products - para cadastro de produtos FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Sabão em pó",
	"category": "Limpeza",
	"product_img": "image.png",
	"price": 9.80
}

```

Caso dê tudo certo, a resposta será assim:

`POST /products - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"name": "Sabão em pó",
	"category": "Limpeza",
	"product_img": "image.png",
	"price": 9.80
}
```

<h3 align='center'> Buscar todos os produtos</h3>
`GET /products -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`GET /products - FORMATO DA RESPOSTA - 201`
```json
[
  {
    "id": 1,
    "name": "Sabão em pó",
    "category": "limpeza",
    "product_img": "image.png",
    "price": 9.80
  }
]
```

<h3 align='center'> Buscar produto específico</h3>
`GET /products/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`GET /products/1 - FORMATO DA RESPOSTA - 201`
```json
{
    "id": 1,
    "name": "Sabão em pó",
    "category": "limpeza",
    "product_img": "image.png",
    "price": 9.80
  }
```
<h3 align='center'> Editar produtos</h3>
`PATCH /products/1 -  FORMATO DA REQUISIÇÃO `

```json
{
	"name": "OMO"
	
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /products/1 - FORMATO DA RESPOSTA - 201`

```json

{
    "id": 1,
    "name": "OMO",
    "category": "limpeza",
    "product_img": "image.png",
    "price": 9.80
  }
```

<h3 align='center'> Cadastro de Sugestões</h3>
`POST /sugestions - para cadastro de sugestões FORMATO DA REQUISIÇÃO `

```json
{
	"type": "produto de limpeza",
	"message": "valor não está atualizado"
	
}

```

Caso dê tudo certo, a resposta será assim:

`POST /sugestions - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
	"type": "produto de limpeza",
	"message": "valor não está atualizado"
  
	
}
```
<h3 align='center'> Deletar sugestão</h3>
`DELETE /sugestions/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`DELETE /sugestions/1 - FORMATO DA RESPOSTA - 201`
""

<h3 align='center'> Buscar sugestões</h3>
`GET /sugestions -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`GET /sugestions - FORMATO DA RESPOSTA - 201`
```json
{
	"type": "produto de limpeza",
	"message": "valor não está atualizado"
	
}
```
