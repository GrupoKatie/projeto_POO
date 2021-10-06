from categorias.papelaria import Papelaria


WELCOME_MESSAGE = '\nSeja bem vindo. Escolha uma das opções:\n'
OPTIONS_MESSAGE = '\n1. Adição de novo produto\n2. Remoção de um produto\n3. Alterar detalhe de um produto\n4. Relatório de Informações\n5. Relatório de Validade\n'
PRODUCT_OPTIONS = "\n1. Alimento\n2. Bebida\n3. Papelaria\n"  
ERROR_MESSAGE = '\nOpção Inválida!\n'
NOT_FOUND = '\nID não foi encontrado!!\n'

PRODUCT_CHANGE_OPTIONS = '\nNome\nPreço\nData de Validade\nMarca\nQuantidade\nData de adicao'

ALIMENTO_CHANGE_OPTIONS = '\nPeso\nTipo\nTransgenico\n'
PAPELARIA_CHANGE_OPTIONS = '\nCor\nTipo\nReciclável\n'
BEBIDA_CHANGE_OPTIONS = '\nVolume\nTipo\nAlcoólico\n'

PRODUCT_CHANGE_OPTIONS_SPEC = {
    'Alimento': ALIMENTO_CHANGE_OPTIONS,
    'Papelaria': PAPELARIA_CHANGE_OPTIONS,
    'Bebida': BEBIDA_CHANGE_OPTIONS,
}