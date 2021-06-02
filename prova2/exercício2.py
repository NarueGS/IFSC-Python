"""
2) Faça uma função que encontre todas as chaves que estão associadas a um  determinado valor em um dicionário. A função receberá no primeiro parâmetro o  dicionário a ser analisado, e como segundo parâmetro o valor da chave a ser buscada.  A função retornará uma lista com as chaves encontradas, essa lista pode ter diversos  valores, apenas um ou nenhum. Nos exemplos, a função foi chamada de  procuraReversa. 
Exemplos de entrada Exemplos de saída 
procuraReversa({ 'chave1': True, 'chave2': False, 'chave3': True, 22: True }, True) ['chave1', 'chave3', 22] 
procuraReversa({ 'first': 22, 'second': 33, 'third': 44 }, 22) 
['first'] 
procuraReversa({ 'first': 22, 'second': 33, 'third': 44 }, True) 

"""

def procuraReversa(lista,cond):
    response = []
    for positions in lista:
        valor = lista[positions]
        if valor == list:
            for cont in range(len(valor)):
                print("A")
                if positions[cont] == cond:
                    response.append(positions)
        else:
            if valor == cond:
                response.append(positions)
    return response
response = procuraReversa({ 'chave1': True, 'chave2': False, 'chave3': True, 22: True }, True)
if response == []:
    print("There is nothing with this condition in your dictionary")
else:
    print(response)