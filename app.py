from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api
from datetime import datetime
from sqlalchemy import true

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gama.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)

class Servico(db.Model):
    __tablename__ = "servico"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32))
    taxa = db.Column(db.Integer)

    def __init__(self, nome, taxa):
        self.nome = nome 
        self.taxa = taxa 

class ServicoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'taxa')

servico_schema = ServicoSchema() 
servicos_schema = ServicoSchema(many=True)

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(32))
    titulo = db.Column(db.String(32))
    status = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, conteudo, titulo, status):
        self.conteudo = conteudo 
        self.titulo = titulo
        self.status = status 

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'conteudo', 'titulo', 'status')

post_schema = PostSchema() 
posts_schema = PostSchema(many=True)


class Equipe(db.Model):
    __tablename__ = "equipe"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32))
    tipo = db.Column(db.String(32))
    status = db.Column(db.String(32))


    def __init__(self, nome, tipo, status):
        self.nome = nome
        self.tipo = tipo
        self.status = status 	 

class EquipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'tipo', 'status')

equipe_schema = EquipeSchema() 
equipes_schema = EquipeSchema(many=True)

# SERVICOS
class ServicoManager(Resource): 
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            servicos = Servico.query.all()
            return jsonify(servicos_schema.dump(servicos))
        servico = Servico.query.get(id)
        return jsonify(servico_schema.dump(servico))
    @staticmethod
    def post():
        nome = request.json['nome']
        taxa = request.json['taxa']
    

        servico = Servico(nome, taxa)
        db.session.add(servico)
        db.session.commit()
        return jsonify({
            'Message': f'Servico {nome} {taxa} inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the servico ID' })
        servico = Servico.query.get(id)

        nome = request.json['nome']
        taxa = request.json['taxa']     

        servico.nome = nome 
        servico.taxa = taxa 
     
        db.session.commit()
        return jsonify({
            'Message': f'Servico {nome} {taxa} altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the servico ID' })
        servico = Servico.query.get(id)

        db.session.delete(servico)
        db.session.commit()

        return jsonify({
            'Message': f'Servico {str(id)} deleted.'
        })

##POST
class PostManager(Resource): 
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            posts = Post.query.all()
            return jsonify(posts_schema.dump(posts))
        post = Post.query.get(id)
        return jsonify(post_schema.dump(post))
    @staticmethod
    def post():
        conteudo = request.json['conteudo']
        titulo = request.json['titulo']
        status = request.json['status']       

        post = Post(conteudo, titulo, status)
        db.session.add(post)
        db.session.commit()
        return jsonify({
            'Message': f'Post {conteudo} {titulo} {status} inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the post ID' })
        post = Post.query.get(id)

        conteudo = request.json['conteudo']
        titulo = request.json['titulo']     
        status = request.json['status'] 

        post.conteudo = conteudo 
        post.titulo = titulo 
        post.status = status 

        db.session.commit()
        return jsonify({
            'Message': f'Post {titulo} altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the post ID' })
        post = Post.query.get(id)

        db.session.delete(post)
        db.session.commit()

        return jsonify({
            'Message': f'Post {str(id)} deleted.'
        })

## EQUIPE
class EquipeManager(Resource): 
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            equipes = Equipe.query.all()
            return jsonify(equipes_schema.dump(equipes))
        equipe = Equipe.query.get(id)
        return jsonify(equipe_schema.dump(equipe))
    @staticmethod
    def equipe():
        nome = request.json['nome']
        tipo = request.json['tipo']
        status = request.json['status']
    

        equipe = Equipe(nome, tipo, status)
        db.session.add(equipe)
        db.session.commit()
        return jsonify({
            'Message': f'Equipe {nome} {tipo} inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the equipe ID' })
        equipe = Equipe.query.get(id)

        nome = request.json['nome']
        tipo = request.json['tipo'] 
        status  = request.json['status']    

        equipe.nome = nome 
        equipe.tipo = tipo  
        equipe.status = status
     
        db.session.commit()
        return jsonify({
            'Message': f'Equipe {nome} {tipo} altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the equipe ID' })
        equipe = Equipe.query.get(id)

        db.session.delete(equipe)
        db.session.commit()

        return jsonify({
            'Message': f'Equipe {str(id)} deleted.'
        })

api.add_resource(ServicoManager, '/api/servicos')
api.add_resource(PostManager, '/api/posts')
api.add_resource(EquipeManager, '/api/equipes')


if __name__ == '__main__':
    app.run(debug=True)
