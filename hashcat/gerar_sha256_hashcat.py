import hashlib
import os
import random
import string

SENHAS_FRACAS = [
    "123456", "senha", "password", "admin", "12345678", "futebol", 
    "brasil", "master", "amor", "segredo", "jesus", "qwerty", "mudar123"
]

def gerar_senha_aleatoria(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def gerar_salt():
    return os.urandom(4).hex()

def criar_hash_sha256_salted(senha, salt):
    # Modo sha256($pass.$salt)
    conteudo = senha + salt
    return hashlib.sha256(conteudo.encode('utf-8')).hexdigest()

def main():
    print("--- Gerador SHA256 Salted para Hashcat ---")
    try:
        qtd = int(input("Quantas senhas gerar? "))
    except ValueError:
        return

    arquivo_hashes = "hashes_para_hashcat.txt"
    arquivo_gabarito = "gabarito_hashcat.txt"

    with open(arquivo_hashes, 'w') as f_hash, open(arquivo_gabarito, 'w') as f_gab:
        for i in range(qtd):
            if random.random() < 0.7:
                senha = random.choice(SENHAS_FRACAS)
            else:
                senha = gerar_senha_aleatoria()

            usuario = f"user_{i+1}"
            salt = gerar_salt()
            h = criar_hash_sha256_salted(senha, salt)

            # Hashcat prefere hash:salt para esse modo
            f_hash.write(f"{h}:{salt}\n")
            
            f_gab.write(f"{usuario} -> Senha: {senha} | Salt: {salt}\n")

    print(f"Arquivo gerado: {arquivo_hashes}")
    print(f"Gabarito: {arquivo_gabarito}")

if __name__ == "__main__":
    main()