#==============================================================================#
#                                                                              #
#                     Win Registry Installed Programs                          #
#                                                                              #
# Descrição: Script que consulta os registros do windows e acha os programas   #
#            instalados                                                        #
# Autores: Hugo Martins Vaz Silva - hugo.martins@kot.com.br                    #
#                                   hugomartinsvaz@gmail.com                   #
#==============================================================================#

import winreg

def get_win_32_apps():
    hive = winreg.HKEY_LOCAL_MACHINE
    flag = winreg.KEY_WOW64_32KEY

    return get_regs(hive, flag)

def get_win_64_apps():
    hive = winreg.HKEY_LOCAL_MACHINE
    flag = winreg.KEY_WOW64_64KEY

    return get_regs(hive, flag)

def get_win_std_apps():
    hive = winreg.HKEY_CURRENT_USER
    flag = 0

    return get_regs(hive, flag)

def get_all_apps():
    software_list32 = get_win_32_apps()
    software_list64 = get_win_64_apps()
    software_listSTD = get_win_std_apps()

    return software_list32 + software_list64 + software_listSTD

def get_regs(hive, flag):

    # estabelece uma conexão com um registro do windows e retorna um handle
    aReg = winreg.ConnectRegistry(None, hive)

    # abre a chave especificada re retorna um objeto handle
    aKey = winreg.OpenKey(aReg,
                          r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0,
                          winreg.KEY_READ | flag)

    # consulta o número de subchave que a chave tem
    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:

            # retorna o nome da sub-chave(i) da chave passada
            asubkey_name = winreg.EnumKey(aKey, i)

            # cria um objeto handle para a sub-chave
            asubkey = winreg.OpenKey(aKey, asubkey_name)

            # busca o nome do software a partir da query de DisplayName da sub-chave
            software['NAME'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            # tenta buscar a versão uma vez que nem sempre terá o valor
            try:
                software['VERSION'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['VERSION'] = 'undefined'

            # tenta buscar quem publicou o software
            try:
                software['PUBLISHER'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['PUBLISHER'] = 'undefined'

        except EnvironmentError:
            continue

        return software_list
