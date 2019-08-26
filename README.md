# Solução Desafio

Para solução do desafio, foram criados 4 aplicações, onde 3 das aplicações são responsáveis por armazenar e disponibilizar informações para consulta de consumidores, a ultima aplicação acessa estas 3 bases 
consumindo e disponibilizando as informações.

A busca de informações dos consumidores se dá pelo CPF. Esta busca é feita em um banco de dados simulado pelo conteúdo de arquivo JSON.

## Aplicações
 - Base A =  Dados pessoais
 - Base B = Lista de bens
 - Base C = Movimentações financeiras
 - Main = Aplicação principal. Acessa as outras 3 aplicações 
  
Todas as aplicações foram desenvolvidas com a linguagem de programação Python, utilizando a IDE PyCharm.
Para disponibilização dos dados foi utilizado o Framework FastApi. 
O Framework JWT foi utilizado para realizar a autenticação entre a aplicação principal e as bases A, B e C por meio de um Token assinado que autentica as requisições.
Para criar as requisições entre as aplicaçãoes foi utilizado a ferramenta Postman, que tem como objetivo testar serviços de WEB APIs por meio do envio de requisições HTTP, sendo possível avaliar as respostas das requisições, no caso as informações dos consumidores.
Para facilidade da criação das APIs foi utilizado a plataforma Docker, com objetivo de disponibilizar com maior rapidez as aplicações. Todas as aplicações rodame em containers Docker.

Para rodar todas as aplicações está sendo utilizado o arquivo docker-compose.yml. Nele está contido as configurações de porta de cada aplicação. 

# Execução da solução

Para executar as aplicações com Docker, basta subir todo o ambiente utilizado o Compose.

```
docker-compose build
```

```
docker-compose up
```

## Base A
### Login
```json
url = http://localhost:8000/login
method = POST
header ={
  "Content-Type": "application/json"
}
body ={
  "usuario": "mestre",
  "senha": "mestra"
}
```

### Obter Consumidor

```json
url = http://localhost:8000/obter_pessoa
method = POST
header ={
  "cpf": "05267551996",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJtZXN0cmUiLCJleHAiOjE1NjY1MDU3NjR9.KNxewdJ3wZryVB_pMh3MGMbcq8hTEjAsuHSZJ8suLS8"
}
Body ={}
```


## Base B
### Login
```json
url = http://localhost:8001/login
method = POST
header ={
  "Content-Type": "application/json"
}
body ={
  "usuario": "mestre",
  "senha": "mestra"
}
```

### Obter Consumidor

```json
url = http://localhost:8001/obter_pessoa
method = POST
header ={
  "cpf": "05267551996",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJtZXN0cmUiLCJleHAiOjE1NjY1MDU4OTF9.-yinWiMg2WNT5wcJAwzadz9rqqehFdJNyRhbDMeMC0U"
}
Body ={}
```

## Base C
### Login
```json
url = http://localhost:8002/login
method = POST
header ={
  "Content-Type": "application/json"
}
body ={
  "usuario": "mestre",
  "senha": "mestra"
}
```

### Obter Consumidor

```json
url = http://localhost:8002/obter_pessoa
method = POST
header ={
  "cpf": "05267551996",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJtZXN0cmUiLCJleHAiOjE1NjY1MDU5Nzh9.GYwXeXYuWvycAdm7OnI0Y1v7O8JdivHTes6dfvFy4-0"
}
Body ={}
```
