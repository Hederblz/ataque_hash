from passlib.hash import lmhash
from passlib.hash import nthash

# --- CONFIGURAÇÃO ---
# Tabelas XP Free Fast só quebram senhas curtas (até 14 chars) e alfanuméricas
SENHAS_PARA_TESTAR = [
    "123456", "SENHA", "ADMIN", "WINDOWS", "XP2025", "TESTE123"
]

ARQUIVO_SAIDA = "hashes_lm_final.txt"

def main():
    print("--- Gerador PWDUMP com LM Hash (Para Tabela XP) ---")
    
    with open(ARQUIVO_SAIDA, 'w') as f:
        for i, senha in enumerate(SENHAS_PARA_TESTAR):
            usuario = f"UserXP_{i+1}"
            uid = 1000 + i
            
            try:
                # 1. Gera o Hash LM (O que a tabela XP Free Fast quer)
                lm = lmhash.hash(senha)
                
                # 2. Gera o Hash NTLM (Só para preencher tabela, não vamos usar)
                nt = nthash.hash(senha)
                
                # Formato PWDUMP: User:UID:LM:NTLM:::
                linha = f"{usuario}:{uid}:{lm}:{nt}:::"
                
                f.write(linha + "\n")
                print(f"Gerado: {usuario} -> {senha}")
                
            except Exception as e:
                print(f"Erro ao gerar hash para {senha}: {e}")

    print(f"\n[Sucesso] Arquivo salvo: {ARQUIVO_SAIDA}")

if __name__ == "__main__":
    main()