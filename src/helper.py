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

def criar_hash_sha256(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def criar_hash_sha256_salted(senha, salt):
    conteudo = senha + salt
    return hashlib.sha256(conteudo.encode('utf-8')).hexdigest()

def criar_hash_md5(senha):
    return hashlib.md5(senha.encode('utf-8')).hexdigest()