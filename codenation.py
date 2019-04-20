import requests
import json
import hashlib

r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=0f662d3a7a300c2f2569a17bad11a814a6f55b61')

# 1 passo
data = r.json()
f = open('answer.json', 'w')
json.dump(data, f)

numero_casas = data['numero_casas']
cifrado = data['cifrado'].lower()


# 2 passo
def findIndex(x):
    if x in ['1', '2','3', '4', '5', '6', '7', '8', '9', '0', '.', ' ']:
        return x
    index = ord(x) + numero_casas
    # if(index > 122):
    #     return (chr(index - 25))
    return (chr(index))

decifrado = [findIndex(x) for x in cifrado]
decifrado = ''.join(decifrado)
data['decifrado'] = decifrado
f = open('answer.json', 'w')
json.dump(data, f)


# 3 passo
m = hashlib.sha1()
m.update(decifrado.encode('utf-8'))
resumo_criptografico = m.hexdigest()

f = open('answer.json', 'w')
data['resumo_criptografico'] = resumo_criptografico
json.dump(data, f)

# 4 passo
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=0f662d3a7a300c2f2569a17bad11a814a6f55b61'
answer = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=answer)
print(r)


# print(data)
# print(' ')
# print(resumo_criptografico)


assert("f" == findIndex('a'))
