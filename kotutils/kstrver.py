#==============================================================================#
#                                                                              #
#                            Kot String Version                                #
# Descrição: Funções para retornar versões a partir de uma string              #
# Autores: Hugo Martins Vaz Silva - hugo.martins@kot.com.br                    #
#                                   hugomartinsvaz@gmail.com                   #
#==============================================================================#

import re

KOT_TOOL_CODE_RGX = '(KOT-[A-Z]{3}-[A-Z]{3}-\d\d\d)'
KOT_TOOL_SEMVER_RGX = '(_\d.\d.\d_)'

#==============================================================================#
# Função: getToolVersion
# Descrição: procura em uma string o padrão de versão
# Recebe: uma string
# Retorna: string do tipo versão e.g: '1.2.33'
#==============================================================================#
def getToolVersion(input_string):
    t_semver_rgx = re.compile(KOT_TOOL_SEMVER_RGX)
    match = t_semver_rgx.search(input_string)
    if match != None:
        return match.string[(match.start()+1):(match.end()-1)]
    else:
        return None

#==============================================================================#
# Função: getToolCode
# Descrição: procura em uma string o padrão de código de ferramentas da kot
# Recebe: uma string
# Retorna: string do tipo código de ferramenta e.g: 'KOT-ABC-XYZ-000'
#==============================================================================#
def getToolCode(input_string):
    t_code_rgx = re.compile(KOT_TOOL_CODE_RGX)
    match = t_code_rgx.match(input_string)
    if match != None:
        return match.string[match.start():match.end()]
    else:
        return None

