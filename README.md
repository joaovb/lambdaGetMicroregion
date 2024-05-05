# Estrutura do Projeto

Aqui está a explicação da estrutura do projeto:

## Diretórios

- `src/`: Diretório principal do código fonte.
- `adapters/`: Contém os adaptadores que conectam o código da aplicação com recursos externos, como APIs.
- `domain/`: Contém a lógica de negócio da aplicação.
- `infra/`: Contém a infraestrutura da aplicação, como acesso a banco de dados ou APIs externas.
- `tests/`: Diretório para testes unitários.
- `lambda_ibge/`: Diretório raiz do projeto.

## Arquivos

- `adapters/ibge_adapter.py`: Este arquivo contém o adaptador para chamar a API do IBGE.
- `domain/ibge_service.py`: Este arquivo contém a lógica de negócio para lidar com os dados retornados pela API do IBGE.
- `infra/ibge_api.py`: Este arquivo contém o código para fazer chamadas à API do IBGE.
- `tests/test_ibge_service.py`: Este arquivo contém os testes unitários para o serviço do IBGE.
- `tests/test_ibge_adapter.py`: Este arquivo contém os testes unitários para o adaptador do IBGE.
