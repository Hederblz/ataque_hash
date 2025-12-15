import random
from src.helper import *

def main():
    print("--- Gerando SHA-256 Salted e Unsalted ---")
    try:
        qtd = int(input("Quantas senhas gerar? "))
    except ValueError:
        return

    arq_unsalted = "sha256_UNSALTED.txt"
    arq_salted = "sha256_SALTED.txt"
    arq_gabarito = "gabarito_sha256.txt"

    with open(arq_unsalted, 'w') as f_uns, \
         open(arq_salted, 'w') as f_salt, \
         open(arq_gabarito, 'w') as f_gab:
        
        for i in range(qtd):
            if random.random() < 0.7:
                senha = random.choice(SENHAS_FRACAS)
            else:
                senha = gerar_senha_aleatoria()

            usuario = f"user_{i+1}"

            hash_unsalted = criar_hash_sha256(senha)
            f_uns.write(f"{usuario}:{hash_unsalted}\n")

            salt = gerar_salt()
            hash_salted = criar_hash_sha256_salted(senha, salt) 
            
            f_salt.write(f"{usuario}:{hash_salted}:{salt}\n")
            
            f_gab.write(f"{usuario} -> Senha: {senha} | Salt: {salt}\n")

    print("\n--- Arquivos Gerados ---")
    print(f"1. {arq_unsalted}")
    print(f"2. {arq_salted}")
    print(f"3. {arq_gabarito}")

if __name__ == "__main__":
    main()