#==============================================================================#
#                                                                              #
#                     Win Registry Installed Programs                          #
#                                                                              #
# Descrição: script de setup da biblioteca ve-py.utils                         #
#                                                                              #
# Autores: Hugo Martins Vaz Silva - hugo.martins@kot.com.br                    #
#                                   hugomartinsvaz@gmail.com                   #
#==============================================================================#

import setuptools

setuptools.setup(
    name="vepyutils",
    version="0.0.4",
    author="Hugo Martins Vaz Silva",
    author_email="hugomartinsvaz@gmail.com",
    description="Biblioteca de scripts utilitários",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
