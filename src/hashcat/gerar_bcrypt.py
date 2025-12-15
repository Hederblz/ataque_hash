import random
import bcrypt
from src.helper import *

def main():
    print("--- Gerador Bcrypt (Algoritmo Lento) ---")
    try:
        qtd = int(input("Quantas senhas gerar? "))
        fator_custo = int(input("Defina o Fator de Custo (Recomendado 10-12): "))
    except ValueError:
        return

    arquivo_hashes = "hashes_bcrypt.txt"
    arquivo_gabarito = "gabarito_bcrypt.txt"

    print(f"Gerando hashes com custo {fator_custo}... (Isso pode demorar um pouco)")

    with open(arquivo_hashes, 'w') as f_hash, open(arquivo_gabarito, 'w') as f_gab:
        for i in range(qtd):
            if random.random() < 0.7:
                senha_plana = random.choice(SENHAS_FRACAS)
            else:
                senha_plana = gerar_senha_aleatoria()

            usuario = f"user_{i+1}"
            
            salt = bcrypt.gensalt(rounds=fator_custo)
            hash_bytes = bcrypt.hashpw(senha_plana.encode('utf-8'), salt)
            
            hash_str = hash_bytes.decode('utf-8')

            f_hash.write(f"{usuario}:{hash_str}\n")
            
            f_gab.write(f"{usuario} -> Senha: {senha_plana} | Custo: {fator_custo}\n")

    print(f"\nArquivo gerado: {arquivo_hashes}")
    print(f"Gabarito: {arquivo_gabarito}")

if __name__ == "__main__":
    main()