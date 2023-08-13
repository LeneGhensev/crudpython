##CRUD Python##

import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bdcrudpython',
)

##Executa os comandos da conexão
cursor = conexao.cursor() #para iniciar a conexão

#CREATE
nome_aluno = "Lene"
nota_final = 5
comando = f'INSERT INTO alunos (nome_aluno, nota_final) VALUES ("{nome_aluno}", {nota_final})' #O id do aluno não precisa ser passado porque ao criar a tabela, coloquei como autoincrement
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

#READ
comando = f'SELECT * FROM bdcrudpython.alunos'
cursor.execute(comando)
resultado = cursor.fetchall() #para ler o banco de dados 
print(resultado)
 
#UPDATE
nota_final = 6
id_aluno = 3
comando = f'UPDATE alunos SET nota_final = {nota_final} WHERE id_aluno = {id_aluno}'
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

#DELETE
nome_aluno = "Lenenew3"
comando = f'DELETE FROM alunos WHERE nome_aluno = "{nome_aluno}"'
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

cursor.close() #esse comando encerra a conexão 
conexao.close() #esse comando encerra a conexão 