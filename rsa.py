import random 
import math 

def gera_primos():
# RSA precisa de números grandes para a criptografia ser efetiva    
    primos = []
    for possivel_primo in range(1000, 10000):
        if all(possivel_primo % i != 0 for i in range(2, int(possivel_primo**0.5) + 1)):
            primos.append(possivel_primo)
    return random.choice(primos)


def gera_coprimo(z, n):
    # o máximo divisor comum entre e, z deve ser 1 e e < n
    while True:
        e = random.randint(2, z)
        if (math.gcd(e, z) == 1) & (e < n):
            return e
            
def calcula_mod_inverso(a, m):
    # checa se mdc == 1
    if math.gcd(a, m) != 1:
        return None
    # calcula inverso multiplicativo de a mod b
    return pow(a, -1, m)
    
def gera_chaves():
    p = gera_primos()
    q = gera_primos()
    n = p * q
    z = (p - 1) * (q - 1)
    e = gera_coprimo(z, n)
    d = calcula_mod_inverso(e, z)
    return (n, e), d

def criptografar(mensagem, public_key):
    n = public_key[0]
    e = public_key[1]
    return pow(mensagem, e, n)

def decriptar(texto_cifrado, n, private_key):
    return pow(texto_cifrado, private_key, n)

mensagem = input("Insira a mensagem (número):")
mensagem = int(mensagem)

public_key, private_key = gera_chaves()
n = public_key[0]
texto_cifrado = criptografar(mensagem, public_key)
msg_decriptada = decriptar(texto_cifrado,n, private_key)

print("Mensagem criptografada:", texto_cifrado)
print("Mensagem descriptografada:", msg_decriptada)