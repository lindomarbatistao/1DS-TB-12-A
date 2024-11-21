import pandas as pd
import os

data = {
    'tituloProduto':['Vela','Cook Top'],
    'preco':[100,2000],
    'descricao':['Vela automotiva', 'Fogão'],
    'imgProduto':['/images', '/images'],
    'catProduto':['Auto', 'Dom'],
    'classProduto':['Popular', 'Popular'],
    'exibirHome':[True, False]
}

df = pd.DataFrame(data)

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

df.to_csv(caminho_final+'/data/ferramentas.csv')
