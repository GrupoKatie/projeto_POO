## Implementação do Projeto do Minicurso de Python - POO (2021)

Esse projeto implementa o Mercadinho da Dona Kátia com as seguintes categorias de produto: **Alimento, Bebida e Papelaria.**

# Funcionalidades:
1. **Adição de novo produto**
    1. Para o atributo de data de vencimento em específico, o formato é mês/ano **(mm/aa)**
    2. Para o atributo transgênico, reciclável e alcoólico, o formato da entrada é **True** ou **False**
2. **Remoção de um produto**
    1. Para remover, é necessário indicar o ID do produto
3. **Alterar detalhe de um produto**
    1. Para alterar, é necessário indicar o ID do produto
4. **Relatório de Informações**
5. **Relatório de Validade**
    1. Indica os produtos no estoque com menos de um mês de validade


# Produto:
* Atributos:
  * Nome - string
  * Preço - float
  * Data de validade - datetime
  * Marca: string
  * Quantidade : string
  * Data de adição: datetime
  * ID - string

# Measure: recebe uma string com formato "numero texto", como 3 kg, 22.2 L, 10 ml. Salva com atributos **valor** e **unidade**

# Alimento (herda de Produto):
* Atributos:
  *  Peso - Measure (peso com valor numerico(float) e unidade de medida (string)
  *  Tipo - string
  *  Transgênico - booleano

# Bebida (herda de Produto):
* Atributos:
  *  Volume - Measure (peso com valor numerico(float) e unidade de medida (string)
  *  Tipo - string
  *  Alcoólico - booleano

# Papelaria (herda de Produto):
* Atributos:
  *  Cor - string
  *  Tipo - string
  *  Reciclável - booleano

# Inventário: armazena os produtos em uma lista [] e o indice do ID dos produtos


