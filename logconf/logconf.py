#==============================================================================#
#                                                                              #
#                              Logical Drives                                  #
# Descrição: Script que retorna os dispositivos lógicos presentes na máquina   #
# Autores: Hugo Martins Vaz Silva - hugomartinsvaz@gmail.com                   #
#                                   hugo.martins@kot.com.br                    #
#==============================================================================#

import os
import sys
import logging

logger = logging.getLogger()

#==============================================================================#
# Classe: MaxLevelFilter
# Herda: logging.Filter
# Descrição: classe para filtrar mensagens que tem menor nível que sel.level
#==============================================================================#
class MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level

#==============================================================================#
# Função: config_log
# Descrição: função que configura o log
# Recebe:
#==============================================================================#
def config_log(fotmat_str=None, level=logging.WARNING):

    format_str = '%(asctime)s %(levelname)s [%(module)s.%(funcName)s:%]: %(message)s'

    # configurando o formato das mensagens de log
    formatter = logging.Formatter(format_str)
    
    # fonte das informações a serem logadas
    logging_out = logging.StreamHandler(sys.stdout)
    logging_err = logging.StreamHandler(sys.stderr)

    # formatando os handlers
    logging_out.setFormatter(formatter)
    logging_err.setFormatter(formatter)

    # adicionando filtro ao handler de stdout
    logging_out.addFilter(MaxLevelFilter(logging.WARNING))

    # setando  nível do logging
    logging_out.setLevel(logging.DEBUG)
    logging_err.setLevel(logging.WARNING)

    # criando um logger global
    global logger

    # adcionando os handlers ao logger global
    logger.addHandler(logging_out)
    logger.addHandler(logging_err)

    # setando o nível de log para o logger global
    logger.setLevel(level)
