import pandas as pd
import os

data = {'tituloProduto':['furadeira', 'bomba'],
        'preco': [400,500],
        'descricao': ['Fura bem', 'Bomba combustivel'],
        'imagemProduto': ['/image', '/image'],
        'categoriaProduto': ['Ferramentas', 'auto'],
        'lassProduto': ['Casa', 'Carro'],
        'exibirHome':[True, False]
        }
df = pd.DataFrame(data)

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

df.to_csv(caminho_final+'/data/ferramentas.csv', index=False)
