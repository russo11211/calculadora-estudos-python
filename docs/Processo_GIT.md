---

## PARTE 3: Comandos para Subir no Git / GitHub

Depois de criar os arquivos na pasta do seu computador:

### 1. Criar o repositório no GitHub
1. Acesse o seu [GitHub](https://github.com).
2. Clique no botão verde **"New"** (ou "+") para criar um repositório.
3. Nome do repositório: `desafio-1-alura` (ou `calculadora-estudos-python`).
4. Deixe como **Público** (Public).
5. **Não marque** as opções de adicionar README ou .gitignore (pois já criamos localmente).
6. Clique em **"Create repository"**.
7. Copie o link do repositório (ex: `https://github.com/SEU_USUARIO/desafio-1-alura.git`).

---

### 2. Comandos no Terminal (dentro da pasta do projeto)

Execute os comandos abaixo, um por um:

```bash
# 1. Inicia o versionamento Git na pasta
git init

# 2. Adiciona todos os arquivos criados para o stage
git add .

# 3. Faz o primeiro commit
git commit -m "feat: implementa calculadora de organizacao de estudos (desafio 1 alura)"

# 4. Garante que o branch principal se chame 'main'
git branch -M main

# 5. Conecta sua pasta local ao repositório criado no GitHub
# (Substitua pela sua URL real copiada no GitHub)
git remote add origin https://github.com/SEU_USUARIO/desafio-1-alura.git

# 6. Envia os arquivos para o GitHub
git push -u origin main


SE O TERMINAL MOSTROU: fatal: not a git repository
(Significa que a pasta oculta .git foi criada dentro de docs, e não na raiz do projeto).
Como o repositório é novo, a forma mais rápida e limpa de resolver é "resetar" o Git local na pasta correta e sobrescrever o GitHub:
1. Apague a configuração antiga do Git que ficou presa na pasta docs:
No Windows (PowerShell):
code
Powershell
Remove-Item -Recurse -Force docs\.git
No Linux / Mac / Git Bash:
code
Bash
rm -rf docs/.git
2. Inicie o Git no lugar certo (na raiz do projeto):
code
Bash
git init
3. Adicione tudo da pasta principal:
code
Bash
git add .
4. Faça o commit completo:
code
Bash
git commit -m "feat: estrutura completa do desafio 1 alura"
5. Renomeie o branch para main e conecte ao seu GitHub:
code
Bash
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
(Substitua com a URL real do seu repositório no GitHub)
6. Envie forçando a substituição do que estava errado lá no GitHub:
code
Bash
git push -u origin main --force
(O --force serve para o GitHub aceitar a nova estrutura da pasta inteira, substituindo aquele commit anterior que tinha apenas a pasta docs).
Ao atualizar a página do seu GitHub no navegador (F5), você verá a pasta inteira com o código calculadora_estudos.py, README.md e a pasta docs organizada corretamente!






Isso acontece quase 100% das vezes pelo mesmo motivo: como o Git foi iniciado primeiro dentro da pasta docs, o Git da pasta principal agora enxerga a pasta docs como um "submódulo fantasma" (ou a pasta oculta .git ainda está presa lá dentro).
Quando isso acontece, o Git simplesmente ignora os arquivos que estão dentro de docs.
Para resolver isso de vez e fazer os arquivos da pasta docs subirem, execute estes 4 comandos no seu terminal (estando na raiz do projeto):
Passo 1: Garantir que a pasta .git interna de docs foi apagada
Execute no terminal:
Se estiver no Windows (PowerShell):
code
Powershell
Remove-Item -Recurse -Force docs\.git -ErrorAction SilentlyContinue
Se estiver no Git Bash, Linux ou Mac:
code
Bash
rm -rf docs/.git
Passo 2: Limpar a memória do Git sobre a pasta docs
Este é o comando-chave. Ele avisa o Git: "pare de tratar a pasta docs como um repositório separado e trate como uma pasta comum":
code
Bash
git rm --cached docs -f -r
Passo 3: Adicionar a pasta docs e seus arquivos novamente
Agora adicione a pasta de volta ao controle do Git:
code
Bash
git add docs/
Para conferir se deu certo, digite:
code
Bash
git status
O que deve aparecer: Você verá os arquivos de dentro de docs listados em verde com a mensagem new file: docs/seu_arquivo.md (ou similar).
Passo 4: Fazer o commit e enviar para o GitHub
code
Bash
git commit -m "fix: inclui arquivos da pasta docs"
git push origin main
⚠️ Caso ainda não apareçam: Verifique estes 2 detalhes
A pasta docs tem arquivos dentro dela?
O Git não rastreia pastas vazias. Se a pasta estiver sem nenhum arquivo, ela não sobe. Coloque um arquivo dentro dela (como o seu relatorio_skillpath.md ou um arquivo de texto qualquer) antes de dar o git add docs/.
O arquivo .gitignore:
Abra seu arquivo .gitignore e veja se você não colocou sem querer a palavra docs ou docs/ dentro dele. Se tiver, apague essa linha e salve.

