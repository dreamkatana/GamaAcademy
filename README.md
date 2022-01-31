# GamaAcademy
CRUD do teste da Gama Academy

API para o consumo de dados das tabelas (Serviços, Posts, Equipes).
Banco de dados SQLITE mas que pode ser alterado através do SQLALCHEMY. 

Script: create_db.py deve ser utilizado para criar o banco de dados e inserir a massa de dados inicial.
Script: app.py é o serviço principal.

API: 
> GET
* curl --location --request GET 'http://127.0.0.1:5000/api/equipes'
* curl --location --request GET 'http://127.0.0.1:5000/api/posts'
* curl --location --request GET 'http://127.0.0.1:5000/api/servicos'

> DELETE
* curl --location --request DELETE 'http://127.0.0.1:5000/api/equipes?id=1'
* curl --location --request DELETE 'http://127.0.0.1:5000/api/users?id=1'
* curl --location --request DELETE 'http://127.0.0.1:5000/api/servicos?id=1'

> UPDATE
* curl --location --request PUT 'http://127.0.0.1:5000/api/equipes?id=1' \
--header 'Content-Type: application/json' \
--data-raw '{"nome": "Team A", "tipo": "teste",  "status": "fechado"}'

> INSERT
* curl --location --request POST 'http://127.0.0.1:5000/api/posts' \
--header 'Content-Type: application/json' \
--data-raw '{"conteudo": "GIT exemplo", "titulo": "Titulo E", "status": "Publicado"}'
