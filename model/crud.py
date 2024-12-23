from model.conn import connection


def salvar(nome, tipo1, tipo2, foto, descricao, hp, forca, defesa):
    mydb, mycursor = connection()
    sql = "INSERT INTO tb_pokemons (nome,tipo1,tipo2,foto,descricao,hp,forca,defesa) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (nome, tipo1, tipo2, foto, descricao, hp, forca, defesa)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "cadastro feito com sucesso")


def select():

    mydb, mycursor = connection()
    mycursor.execute("SELECT * FROM tb_pokemons")
    resultado = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return resultado


def delete(id):

    mydb, mycursor = connection()
    sql = "DELETE FROM tb_pokemons WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()
    mycursor.close()
    mydb.close()


def update(identificador, campos, valores):

    mydb, mycursor = connection()
    if len(campos) != len(valores) and campos and valores:
        print("erro, tamanho dos campos difere dos valores")
        return
    parametros_sql = ''
    for indice in range(0, len(campos)):
        parametros_sql += '{} = {}, '.format(campos[indice],
                                             valores[indice])
    parametros_sql.removesuffix(', ')
    mycursor.execute('update tb_pokemons set {} where id = {};'.format(
        parametros_sql, identificador
    ))
    mycursor.close()
    mydb.close()


def lista():
    mydb, mycursor = connection()

    mycursor.execute("SELECT * FROM Pokedex")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)

