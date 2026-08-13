# 🌲 Aventura na Floresta — Jogo de Texto em Python

Projeto desenvolvido em Python como exercício de introdução à **lógica de programação e estruturas condicionais**.

O programa apresenta ao usuário uma aventura interativa em uma floresta, na qual suas escolhas determinam os próximos acontecimentos da história.

O projeto possui diferentes caminhos, decisões, finais e situações de sucesso ou derrota.

---

## 📌 Sobre o projeto

O usuário começa a aventura em uma floresta escura e encontra dois itens:

- 🔥 Fósforo
- 🔦 Lanterna

A partir da escolha inicial, diferentes situações são apresentadas.

Cada decisão do usuário altera o caminho da história, criando diferentes possibilidades de resultado.

O projeto foi desenvolvido para praticar principalmente:

- `if`
- `elif`
- `else`
- Comparações
- Operadores lógicos
- Valores booleanos
- Entrada de dados
- Strings
- Estruturas condicionais aninhadas

---

## 🎮 Como funciona

A aventura começa solicitando uma escolha:

```python
escolha = input("Qual você quer pegar? ")

Como o usuário pode digitar a mesma palavra utilizando letras maiúsculas ou minúsculas, a entrada é convertida para letras minúsculas:

escolha = escolha.lower()

Dessa forma, entradas como:

FÓSFORO
Fósforo
fósforo

podem ser tratadas de maneira mais consistente.

🌳 Caminhos da aventura

🔥 Caminho do fósforo

Ao escolher o fósforo, o jogador encontra um urso-pardo.

A partir desse momento, pode escolher entre:

Correr;
Se esconder.

Cada escolha apresenta novas decisões.

Por exemplo:

Você quer CORRER ou SE ESCONDER atrás de uma árvore?

O caminho de correr apresenta novas opções:

Entrar em um tronco;
Descer pelo riacho.

Já o caminho de se esconder apresenta outras possibilidades:

Jogar uma pedra;
Atacar o urso.


🔦 Caminho da lanterna

Ao escolher a lanterna, o jogador pode:

Seguir o caminho;
Procurar nas árvores.

Dependendo da decisão, novas situações são apresentadas.

O jogador pode encontrar uma caixa e decidir:

Abrir;
Continuar.

Cada escolha altera o desenvolvimento da aventura.


🧠 Estruturas condicionais

O principal recurso utilizado no projeto são as estruturas condicionais.

Exemplo:

if escolha == "fósforo":
    # Caminho do fósforo

if escolha == "lanterna":
    # Caminho da lanterna

Também foram utilizados elif e else para trabalhar com diferentes possibilidades:

if escolha == "correr":
    # Caminho 1

elif escolha == "se esconder":
    # Caminho 2

else:
    print("Essa não é uma opção.")


📚 Conceitos praticados
if

Utilizado para verificar se uma determinada condição é verdadeira.

if escolha == "fósforo":
    print("Você pegou o fósforo.")
elif

Utilizado para verificar uma condição alternativa:

if escolha == "correr":
    # ...

elif escolha == "se esconder":
    # ...
else

Utilizado quando nenhuma das condições anteriores é atendida:

else:
    print("Essa não é uma opção.")
Comparação de strings

As escolhas do usuário são comparadas com valores específicos:

if escolha == "entrar":
.lower()

Utilizado para converter a entrada do usuário para letras minúsculas:

escolha = escolha.lower()

Isso facilita a comparação das respostas.

Condicionais aninhadas

O projeto utiliza estruturas condicionais dentro de outras estruturas condicionais.

Por exemplo:

if escolha == "fósforo":

    escolha = input("Você quer correr ou se esconder? ")

    if escolha == "correr":
        # ...

    elif escolha == "se esconder":
        # ...

Isso permite criar diferentes níveis de decisão dentro da aventura.

🎯 Objetivo de aprendizado

O objetivo principal deste projeto foi aprender a utilizar estruturas condicionais para criar programas capazes de tomar decisões com base nas informações fornecidas pelo usuário.

O projeto também ajudou a compreender como diferentes condições podem ser combinadas para criar múltiplos caminhos de execução.

🧪 Testes realizados

Durante o desenvolvimento, diferentes combinações de respostas podem ser utilizadas para verificar os caminhos disponíveis.

Alguns cenários incluem:

Cenário 1 — Fósforo
Fósforo
→ Correr
→ Entrar
→ Sair

Resultado:

Você consegue fugir do urso.
Cenário 2 — Fósforo
Fósforo
→ Correr
→ Entrar
→ Ficar

Resultado:

O personagem morre.
Cenário 3 — Lanterna
Lanterna
→ Seguir
→ Atacar

Resultado:

O personagem é atacado pelo urso.
Cenário 4 — Lanterna
Lanterna
→ Procurar
→ Abrir
→ Atacar

Resultado:

O personagem consegue sobreviver.

Esses diferentes caminhos ajudam a verificar se as condições estão direcionando o programa para os resultados esperados.


🚀 Possíveis melhorias

O projeto pode ser expandido de diversas formas:

Adicionar mais caminhos para a história;
Criar um sistema de pontuação;
Adicionar vida ou energia ao personagem;
Criar inventário de itens;
Permitir reiniciar a aventura;
Criar uma condição de vitória;
Criar mais finais;
Utilizar funções para organizar cada parte da história;
Evitar repetição de código;
Criar um sistema de validação das opções;
Utilizar estruturas de repetição para permitir novas tentativas.

📖 O que aprendi

Neste projeto, aprendi a utilizar estruturas condicionais em Python para criar diferentes caminhos de execução.

Pratiquei if, elif e else, além de comparações entre strings e utilização do método .lower() para tratar diferentes formas de entrada do usuário.

Também aprendi sobre condicionais aninhadas, utilizando uma decisão dentro de outra para criar diferentes níveis de escolhas.

O projeto foi importante para entender como a lógica condicional pode ser utilizada para transformar um programa simples em uma experiência interativa com diferentes resultados.

Além disso, durante o desenvolvimento, comecei a perceber a importância de testar diferentes combinações de entradas para verificar se cada caminho do programa apresenta o resultado esperado.
