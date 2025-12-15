import random
from src.helper import *

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
            
            f_hash.write(f"{usuario}:{h}\n")
            f_gab.write(f"{usuario} -> {senha}\n")

    print(f"Arquivo gerado: {arquivo_hashes}")
    print(f"Gabarito: {arquivo_gabarito}")

if __name__ == "__main__":
    main()