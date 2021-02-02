#==============================================================================#
#                                                                              #
#                              Logical Drives                                  #
# Descrição: Script que retorna os dispositivos lógicos presentes na máquina   #
# Autores: Hugo Martins Vaz Silva - hugomartinsvaz@gmail.com                   #
#                                   hugo.martins@kot.com.br                    #
#==============================================================================#

import winreg
import string

def get_logical_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter+':\\')
        bitmask >>= 1

    return drives
