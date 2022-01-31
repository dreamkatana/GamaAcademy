import os
from app import Servico, Equipe, Post, db

# Inicialização dos dados

SERVICOS = [
{"nome": "Limpeza", "taxa": 1},
{"nome": "Secagem", "taxa": 2},
{"nome": "Lavagem", "taxa": 3},
{"nome": "Brilho", "taxa": 4},
{"nome": "Cera", "taxa": 5}
]

POSTS = [
{"conteudo": "Lorem ipsum dolor sit amet", "titulo": "Titulo E", "status": "Publicado"},
{"conteudo": "Lorem ipsum 53dolor sit amet", "titulo": "Titulo A", "status": "Publicado"},
{"conteudo": "Lorem ipsum 43dolor sit amet", "titulo": "Titulo B", "status": "Fechado"},
{"conteudo": "Lorem ipsum 12dolor sit amet", "titulo": "Titulo C", "status": "Publicado"},
]

EQUIPES = [
{"nome": "Team A", "tipo": "teste",  "status": "ativo"},
{"nome": "Team B", "tipo": "teste",  "status": "ativo"},
{"nome": "Team C", "tipo": "teste",  "status": "fechada"},
{"nome": "Team D", "tipo": "teste",  "status": "ativo"},
]

# Delete database file if it exists currently
if os.path.exists("gama.db"):
    os.remove("gama.db")


db.create_all()

for servico in SERVICOS:
    p = Servico(nome=servico.get("nome"), taxa=servico.get("taxa"))
    db.session.add(p)
db.session.commit()

for post in POSTS:
    p = Post(conteudo=post.get("conteudo"), titulo=post.get("titulo"), status=post.get("status"))
    db.session.add(p)
db.session.commit()

for equipe in EQUIPES:
    p = Equipe(nome=equipe.get("nome"), tipo=equipe.get("tipo"), status=equipe.get("status"))
    db.session.add(p)
db.session.commit()


exit()
