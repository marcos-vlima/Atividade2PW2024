# Atividade Avaliativa

## Faça um Fork do Repositório

Faça um fork do repositório 

## Modifique o Arquivo README.md

Substitua os nomes fictícios pelos nomes dos integrantes da equipe.

## Adicione um CRUD de Categoria

Complemente o projeto atual da Quitanda Online adicionando um CRUD completo para a categoria do produto. A categoria de um produto tem apenas um Id e um Nome. Crie todos os artefatos para garantir a criação do CRUD completo.

## Associe a Categoria ao Produto

No cadastro e alteração de produtos, adicione um campo do tipo *select* para que o usuário possa selecionar uma das categorias cadastradas.

Dicas:
1. Crie um campo IdCategoria na tabela de produtos, e modifique os SQLs necessários adicionando o IdCategoria.
2. Modifique modelo (classe) e o repositório de produtos para permitir a inclusão e a alteração de produtos, incluindo IdCategoria.
3. Modifique os templates de alterar e de cadastrar produtos adicionando um campo *select* para a escolha da categoria.
4. Modifique a rota de exibição dos formulários de alteração e de atualização e produtos passando um dicionário contendo o Id e o Nome das categorias cadastradas, para exibir no campo *select*.