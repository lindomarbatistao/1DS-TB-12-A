import pandas as pd
import sqlite3

class Programa:
    def __init__(self, db='db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()
    
    def menu(self):
        while True:
            print('\n'
                '[1] - Create \n'
                '[2] - Read \n'
                '[3] - Update \n'
                '[4] - Delete \n'
                '[5] - Exit \n'
                '\n'
                )
            op = int(input('Escolha uma opção: '))
            match op:
                case 1:
                    self.menu_create()
                case 2:
                    print('Read')
                case 3:
                    print('Update')
                case 4:
                    print('Delete')
                case 5:
                    print('Você saiu...')
                    break
                case _:
                    print('Opção inválida!')

    def create(self, titulo, preco, descricao,img, cat, classif, exibir):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO api_produto(tituloProduto, preco, descricao,
               imgProduto, catProduto, classProduto,
               exibirHome)
               VALUES(?,?,?,?,?,?,?)
                       ''', (titulo, preco, descricao, img, cat, classif, exibir))
        self.conn.commit()
        print("Produto cadastrado com sucesso!!!")
    
    def menu_create(self):
        print('\n'
              '[1]-Título\n'
              '[2]-Preço\n'
              '[3]-Descrição\n'
              '[4]-Imagem\n'
              '[5]-Categoria\n'
              '[6]-Classificação\n'
              '[7]-Exibir(true/false)\n'
              )
        titulo = input('Título: ')
        preco = float(input('Preço: '))
        descricao = input('Descrição: ')
        img = input('Imagem: ')
        cat = input('Categoria: ')
        classif = input('Classificação: ')
        exibir = input('Exibir: ')
        self.create(titulo, preco, descricao, img, cat, classif, exibir)

bosch = Programa()