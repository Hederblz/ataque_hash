### O que é 'quebrar' um hash
Comece com a função hash em si. Explique que não é uma descriptografia, mas sim o processo de encontrar a entrada original (a senha) que gerou o valor de hash de saída. Use um exemplo simples de uma string $\to$ hash.

### diferença entre hash seguro e inseguro

Use exemplos. Um hash inseguro (como MD5 ou SHA-1) é rápido e suscetível a colisões. Um hash seguro (como SHA-256 ou SHA-3) é mais resistente. Ponto-chave: A velocidade é a inimiga da segurança do hash de senha.

### tipos de ataques e técnicas

1. Ataques Baseados em Previsão
    - Ataque de Dicionário: Explique que senhas fracas são a norma.
        - Demonstração Rápida: Use um wordlist pequeno contra um hash inseguro.

    - Ataque de Força Bruta: Explicar que tenta todas as combinações possíveis. Enfatize que é inviável para senhas longas/complexas.

    - Ataques de Máscara: Uma forma otimizada de força bruta (ex: Senha20??).

2. Otimização de Ataques e Pré-cálculo

    - Rainbow Table: Explique como elas funcionam para economizar tempo de computação.
        - Ponto-chave: Elas mapeiam o hash diretamente de volta à senha sem precisar da função hash para cada tentativa.

    - Colisão: Explique que, teoricamente, duas entradas podem gerar o mesmo hash (MD5, SHA-1).

3. Tipos de Ataques por Local (Online vs. Offline)

    - Offline: O atacante possui o arquivo de hash (/etc/shadow) e tenta quebrá-los em seu próprio hardware (rápido).

    - Online: O atacante tenta senhas diretamente no formulário de login (lento, suscetível a bloqueio/limitação de taxa).

### Demonstração Prática

Crie um arquivo de exemplo com 5 a 10 hashes usando algoritmos e técnicas diferentes:

MD5 (simples, unsalted)
SHA-256 (simples, unsalted)
SHA-256 (com salt fraco/reutilizado)
Bcrypt (com salt forte, difícil de quebrar)

- Demonstração das Técnicas de Ataques:

    - Dicionário (Unsalted/Inseguro): Quebre o MD5 e o SHA-256 rapidamente.

    - Força Bruta/Máscara (Unsalted): Quebre uma senha curta e previsível.

    - Rainbow Table e Salt:
        - Explique que o salt destrói a eficácia da Rainbow Table.
        - Mostre um hash com salt e demonstre que, embora o dicionário ainda funcione, a tabela pré-calculada não funciona mais. Explique que o salt força o atacante a pré-calcular uma tabela para CADA salt único.

### Soluções e Políticas de Armazenamento

1. Algoritmos Lentos e o Papel do Custo

    - Algoritmos Lentos (bcrypt/scrypt/Argon2): Explique que esses algoritmos foram criados para aumentar o custo do ataque.

    - Fator de Custo/Iterações: Mostre que eles permitem definir um fator de custo/trabalho. *

    - Ponto-chave: Se demora 0.1 segundo para o servidor verificar uma senha legítima, isso significa que o atacante demorará milhões de anos para quebrar um DB inteiro.

2. Políticas de Armazenamento Correto de Senhas

    - Use KDFs Modernos: Mantenha-se atualizado (Argon2 é o padrão ouro atual).

    - Salt Forte e Único: Cada senha DEVE ter um salt criptograficamente seguro e único (nunca reutilizar).

    - Fator de Custo Alto: Sempre use o máximo de iterações/custo que o seu hardware pode suportar (sem prejudicar a experiência do usuário).

    - Políticas de Senha: Implemente requisitos de complexidade e tamanho (mínimo de 12 caracteres é um bom ponto de partida).