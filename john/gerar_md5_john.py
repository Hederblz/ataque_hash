import hashlib
import random
import string

SENHAS_FRACAS = [
    "123456", "senha", "password", "admin", "12345678", "futebol", 
    "brasil", "master", "amor", "segredo", "jesus", "qwerty", "mudar123"
]

def gerar_senha_aleatoria(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def criar_hash_md5(senha):
    return hashlib.md5(senha.encode('utf-8')).hexdigest()

def main():
    print("--- Gerador MD5 para John the Ripper ---")
    try:
        qtd = int(input("Quantas senhas gerar? "))
    except ValueError:
        return

    arquivo_hashes = "hashes_para_john.txt"
    arquivo_gabarito = "gabarito_john.txt"

    with open(arquivo_hashes, 'w') as f_hash, open(arquivo_gabarito, 'w') as f_gab:
        for i in range(qtd):
            if random.random() < 0.7:
                senha = random.choice(SENHAS_FRACAS)
            else:
                senha = gerar_senha_aleatoria()

            usuario = f"user_{i+1}"
            h = criar_hash_md5(senha)
            
            # O John aceita bem o formato user:hash
            f_hash.write(f"{usuario}:{h}\n")
            f_gab.write(f"{usuario} -> {senha}\n")

    print(f"Arquivo gerado: {arquivo_hashes}")
    print(f"Gabarito: {arquivo_gabarito}")

if __name__ == "__main__":
    main()