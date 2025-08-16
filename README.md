# 📊 Análise Exploratória de Produtos com Azure Databricks

Este projeto demonstra um fluxo de trabalho completo para análise de dados utilizando a plataforma Azure Databricks, desde a configuração do ambiente até a visualização de insights, com todo o código versionado utilizando Git.

---

## 📜 Visão Geral do Projeto

O objetivo deste repositório é servir como um guia prático para realizar uma análise exploratória de dados em um ambiente de nuvem. O projeto utiliza um conjunto de dados público sobre produtos para contar a quantidade de itens por categoria, demonstrando as capacidades de processamento e visualização do Databricks.

### ✨ Tecnologias Utilizadas
* **Plataforma Cloud:** Microsoft Azure
* **Processamento de Dados:** Azure Databricks
* **Linguagem:** SQL e Python
* **Controle de Versão:** Git & GitHub

---

## 🚀 Guia de Configuração e Execução

Siga os passos abaixo para replicar o ambiente e executar a análise.

### 1. Configuração do Cluster no Databricks

Para executar o notebook, é necessário um cluster computacional. Este projeto foi desenvolvido utilizando um cluster temporário com uma configuração simples, ideal para análises exploratórias.

**Configuração do Cluster:**
![Configuração do Cluster](http://googleusercontent.com/file_content/4)

### 2. Integração com o Git

O versionamento do código é feito diretamente na interface do Databricks através da funcionalidade "Repos".

**Passo A: Conectar a Conta Git**
Primeiro, conecte sua conta do GitHub ao Databricks em `User Settings > Git integration`, utilizando um Personal Access Token (PAT).

![Integração Git com Databricks](http://googleusercontent.com/file_content/1)

**Passo B: Clonar o Repositório**
Depois, adicione o repositório ao seu workspace através da seção "Repos".

![Adicionando um Repositório](http://googleusercontent.com/file_content/3)

### 3. Conjunto de Dados

O conjunto de dados utilizado, `products.csv`, está localizado na pasta `/data`.

Para este projeto de estudo, o arquivo de dados foi incluído diretamente no repositório para facilitar a replicação. Em projetos de produção, a prática recomendada é manter os dados em um Data Lake (como o ADLS) e acessá-los a partir do notebook.

### 4. Executando a Análise

O notebook `analise-produtos.py` contém o código SQL que lê os dados da tabela `products` e realiza uma contagem de produtos agrupados por categoria.

### 5. Salvando o Trabalho (Commit & Push)

Após adicionar o notebook ao repositório, todas as alterações são salvas (commitadas) de volta para o GitHub através da interface do Databricks.

![Commit e Push das alterações](http://googleusercontent.com/file_content/5)

---

## 📈 Resultados da Análise

A execução do notebook gera uma visualização de gráfico de barras que mostra a distribuição da quantidade de produtos por categoria. Isso permite identificar rapidamente quais são as categorias com o maior número de itens cadastrados.

![Gráfico de Produtos por Categoria](http://googleusercontent.com/file_content/0)

Este gráfico é um exemplo simples de como podemos extrair insights valiosos de forma rápida e visual utilizando as ferramentas do Azure Databricks.
