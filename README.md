<div align="center">

# 🧠 Lógica de Programação com Python

### Bootcamp de Analista de Dados Júnior · Generation Brasil

**Primeiros passos em programação: variáveis, entrada e saída de dados, listas, funções, data e hora, cores e fluxos de controle.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Aprendizado-2ea44f?style=for-the-badge)

</div>

---

## 🎯 Sobre este repositório

Este projeto foi criado durante o **Bootcamp de Analista de Dados da Generation Brasil**. O objetivo é praticar os **fundamentos de lógica de programação em Python**, a base necessária para trabalhar com dados nas próximas etapas do curso.

## 📚 Conceitos Abordados

**1. Variáveis**
- Como armazenar dados na memória (textos, números, etc).
- Atribuição de valores e uso das variáveis ao longo do código.

**2. Entrada e Saída (I/O)**
- `input()`: receber dados digitados pelo usuário.
- `print()`: exibir resultados na tela.

**3. Listas**
- Agrupamento de vários valores em uma única variável.
- Acesso aos itens pelo índice, lembrando que a contagem começa em zero (0).

**4. Manipulação de Listas**
- `.append()`: adicionar um item ao final da lista.
- `.remove()`: remover um item pelo valor.
- `.pop()`: remover um item pelo índice.

**5. Fluxos de Controle**
- **Decisão** (`if`, `elif`, `else`): o programa escolhe um caminho de acordo com uma condição.
- **Repetição com contador** (`for` + `range()`): repete um bloco um número definido de vezes.
- **Repetição com condição** (`while`): repete um bloco enquanto uma condição for verdadeira.
- **Operadores**: comparação (`==`, `!=`, `>`, `<`, `>=`, `<=`), lógicos (`and`, `or`, `not`) e resto da divisão (`%`).

**6. Funções**
- Blocos de código reutilizáveis, definidos com `def`.
- Parâmetros permitem enviar informações para a função; `return` devolve um resultado.

**7. Data e hora**
- Uso do módulo `datetime` para consultar a data e a hora atuais.
- Formatação de datas e horários com `strftime()`.

**8. Cores no terminal**
- Uso de códigos ANSI para colorir textos exibidos com `print()`.
- O código de reset restaura a cor padrão depois da mensagem.

---

## 💡 Exemplo Rápido

```python
# Variáveis
nome = input("Qual é o seu nome? ")
print("Olá,", nome)

# Listas
turma = ["Ana", "Bruno", "Carla"]
turma.append("Daniel")   # adiciona ao final
turma.remove("Bruno")    # remove pelo valor
turma.pop(0)             # remove pelo índice

print(turma)

# Função simples

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Ana"))
```

---

## 🔀 Fluxos de Controle na Prática

Exercícios que praticam decisão e repetição.

### 1. Tabuada (`for` + `range`)

Pede um número e mostra a tabuada de 1 a 10.

```python
numero = int(input("Tabuada de qual número? "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

### 2. Senha (`while`)

Repete o pedido até o usuário digitar a senha correta.

```python
senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")
    if tentativa != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Acesso liberado!")
```

### 3. Notas (`if/elif/else`)

Recebe duas notas, calcula a média e informa a situação do aluno.

```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

### 4. Nomes Aprovados (listas + `for` + `if`)

Guarda os alunos aprovados em uma lista e exibe o resultado no final.

```python
aprovados = []

for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input(f"Nota de {nome}: "))

    if nota >= 7:
        aprovados.append(nome)

print("Alunos aprovados:", aprovados)
print("Total de aprovados:", len(aprovados))
```

---

## 🧩 Funções na Prática

Uma função reúne instruções que podem ser chamadas sempre que necessário. Os parâmetros recebem valores e `return` devolve o resultado para o restante do programa.

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

media = calcular_media(8.5, 7.0)
print(f"Média: {media:.1f}")
```

---

## 📅 Data e Hora na Prática

O módulo `datetime` permite consultar a data e a hora atuais. Com `strftime()`, é possível escolher como elas serão exibidas. Neste exemplo, `%d/%m/%Y` representa dia/mês/ano e `%H:%M` representa hora e minuto.

```python
from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M")

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
```

---

## 🎨 Cores no Terminal

Códigos ANSI podem mudar a cor do texto em muitos terminais. `\033[32m`, por exemplo, inicia o verde, e `\033[0m` volta à cor padrão. O suporte pode variar conforme o terminal utilizado.

```python
VERDE = "\033[32m"
VERMELHO = "\033[31m"
RESET = "\033[0m"

print(f"{VERDE}Operação concluída!{RESET}")
print(f"{VERMELHO}Ocorreu um erro.{RESET}")
```

---

## 🐍 O Zen do Python

Ao rodar `import this` no Python, aparece o "poema" com os princípios que guiam a linguagem (PEP 20, de Tim Peters):

```python
import this
```

| Original | Tradução |
|---|---|
| Beautiful is better than ugly. | Bonito é melhor que feio. |
| Explicit is better than implicit. | Explícito é melhor que implícito. |
| Simple is better than complex. | Simples é melhor que complexo. |
| Complex is better than complicated. | Complexo é melhor que complicado. |
| Flat is better than nested. | Plano é melhor que aninhado. |
| Sparse is better than dense. | Esparso é melhor que denso. |
| Readability counts. | Legibilidade conta. |
| Special cases aren't special enough to break the rules. | Casos especiais não são especiais o bastante para quebrar as regras. |
| Although practicality beats purity. | Embora a praticidade vença a pureza. |
| Errors should never pass silently. | Erros nunca devem passar em silêncio. |
| Unless explicitly silenced. | A menos que sejam silenciados explicitamente. |
| In the face of ambiguity, refuse the temptation to guess. | Diante da ambiguidade, recuse a tentação de adivinhar. |
| There should be one-- and preferably only one --obvious way to do it. | Deve haver uma, e preferencialmente só uma, maneira óbvia de fazer isso. |
| Although that way may not be obvious at first unless you're Dutch. | Embora essa maneira possa não ser óbvia no início, a menos que você seja holandês. |
| Now is better than never. | Agora é melhor que nunca. |
| Although never is often better than *right* now. | Embora nunca seja muitas vezes melhor que *já*. |
| If the implementation is hard to explain, it's a bad idea. | Se a implementação é difícil de explicar, é uma má ideia. |
| If the implementation is easy to explain, it may be a good idea. | Se a implementação é fácil de explicar, pode ser uma boa ideia. |
| Namespaces are one honking great idea -- let's do more of those! | Espaços de nomes são uma ótima ideia, vamos fazer mais deles! |

## 📁 Arquivos de Prática

- 🐍 `Turma.py`: variáveis, entrada e saída de dados e manipulação de listas.
- 🐍 `tabuada.py`: laço `for` com `range()`.
- 🐍 `senha.py`: laço `while` com validação de entrada.
- 🐍 `notas.py`: média e situação do aluno com `if/elif/else`.
- 🐍 `aprovados.py`: listas combinadas com `for` e `if`.
- 🐍 `funcoes.py`: criação e chamada de funções com parâmetros e `return`.
- 🐍 `data_hora.py`: consulta e formatação de data e hora com `datetime`.
- 🐍 `cores.py`: mensagens coloridas no terminal com códigos ANSI.

## 🚀 Como executar

Com o Python instalado, execute no terminal:

```bash
# Rodar um arquivo de prática (exemplo)
python Turma.py
python tabuada.py

# Ativar o Zen do Python no terminal
python -c "import this"
```

Se o `python` não funcionar, tente `python3`.