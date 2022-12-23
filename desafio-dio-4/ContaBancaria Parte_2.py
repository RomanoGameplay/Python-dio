from datetime import datetime
import pprint
import pymongo as pym


client = pym.MongoClient(
    'mongodb+srv://RomanoGameplay:ohayougozaimashita@cluster0.mpiehhb.mongodb.net/?retryWrites=true&w=majority')
db = client.test
collections = db.test_collection

new_posts = [
    {
        'author': 'Amanda',
        'endereco': 'amanda@mgmail.com',
        'cpf': '111222',
        'conta':
            {
                'agencia': '001',
                'num': '01-a',
                'tipo': 'conta_corrente'
            },
        'balanco': 0,
        'date': datetime.utcnow()
    },
    {
        'author': 'Beltrami',
        'endereco': 'beltramibb@mgmail.com',
        'cpf': '222333',
        'conta':
            {
                'agencia': '001',
                'num': '01-a',
                'tipo': 'conta_corrente'
            },
        'balanco': 200,
        'date': datetime.utcnow()
    },
    {
        'author': 'Carlos',
        'endereco': 'carlitos@mgmail.com',
        'cpf': '333444',
        'conta':
            {
                'agencia': '001',
                'num': '01-a',
                'tipo': 'conta_corrente'
            },
        'balanco': 1340,
        'date': datetime.utcnow()
    },
    {
        'author': 'Evaristo',
        'endereco': 'evacosta@mgmail.com',
        'cpf': '444555',
        'conta':
            {
                'agencia': '001',
                'num': '01-a',
                'tipo': 'conta_corrente'
            },
        'balanco': 0,
        'date': datetime.utcnow()
    },
    {
        'author': 'Dani',
        'endereco': 'daniela@mgmail.com',
        'cpf': '555666',
        'conta':
            {
                'agencia': '001',
                'num': '01-a',
                'tipo': 'conta_corrente'
            },
        'balanco': 4500,
        'date': datetime.utcnow()
    }
]
posts = db.posts
result = posts.insert_many(new_posts)

print('\n Documentos presentes na coleção posts:\n')
for post in posts.find():
    print('\n')
    pprint.pprint(post)

print('\nRecuperando info da coleção postde forma ordenada:')
for post in posts.find({}).sort('date'): pprint.pprint(post)

print('\nRecuperação do autor "Joao": ')
pprint.pprint(db.posts.find_one({'author': 'Joao'}))

print('\nRecuperação do autor "Beltrami": ')
pprint.pprint(db.posts.find_one({'author': 'Beltrami'}))

db['posts'].drop()

print('\nApós o comando drop: \n')
for post in posts.find(): pprint.pprint(post)
