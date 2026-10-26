<div align="center">

# 🧠 Lógica de Programação com Python

### Bootcamp de Analista de Dados Júnior · Generation Brasil

**Primeiros passos em programação: variáveis, entrada e saída de dados e listas.**

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
```

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

## 📁 Arquivo de Prática

- 🐍 `Turma.py`: script em Python usado para praticar variáveis, entrada e saída de dados e manipulação de listas.

## 🚀 Como executar

Com o Python instalado, execute no terminal:

```bash
# Rodar o arquivo de prática
python Turma.py

# Ativar o Zen do Python no terminal
python -c "import this"
```

Se o `python` não funcionar, tente `python3`.
