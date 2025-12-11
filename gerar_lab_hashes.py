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

def criar_hash_md5(senha):
    return hashlib.md5(senha.encode('utf-8')).hexdigest()

def criar_hash_sha256_salted(senha, salt):
    conteudo = senha + salt
    return hashlib.sha256(conteudo.encode('utf-8')).hexdigest()

def main():
    print("--- Gerador de Hashes para Laboratório ---")
    try:
        qtd = int(input("Quantas senhas você quer gerar? "))
    except ValueError:
        print("Por favor, digite um número inteiro.")
        return

    arquivo_md5 = "lab_hashes_md5.txt"
    arquivo_sha256 = "lab_hashes_salted.txt"
    arquivo_gabarito = "lab_gabarito_senhas.txt"

    print(f"\nGerando {qtd} entradas...")

    with open(arquivo_md5, 'w') as f_md5, \
         open(arquivo_sha256, 'w') as f_sha, \
         open(arquivo_gabarito, 'w') as f_gab:
        
        for i in range(qtd):
            if random.random() < 0.7:
                senha_plana = random.choice(SENHAS_FRACAS)
            else:
                senha_plana = gerar_senha_aleatoria()

            usuario = f"user_{i+1}"

            hash_md5 = criar_hash_md5(senha_plana)
            f_md5.write(f"{usuario}:{hash_md5}\n")

            salt = gerar_salt()
            hash_sha = criar_hash_sha256_salted(senha_plana, salt)
            f_sha.write(f"{usuario}:{hash_sha}:{salt}\n")

            f_gab.write(f"{usuario} -> Senha: {senha_plana} | Salt: {salt}\n")

    print("\n--- Concluído! ---")
    print(f"1. Arquivo fraco gerado: {arquivo_md5} (Use para testar velocidade)")
    print(f"2. Arquivo forte gerado: {arquivo_sha256} (Use para entender Salts)")
    print(f"3. Gabarito gerado: {arquivo_gabarito} (NÃO mostre isso para a ferramenta de crack)")

if __name__ == "__main__":
    main()