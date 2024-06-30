import os
import scandir

def contar_arquivos_em_subpastas(diretorio):
    resultado = {}
    for entrada in scandir.scandir(diretorio):
        if entrada.is_dir():
            total_arquivos = 0
            for subentrada in scandir.scandir(entrada.path):
                if subentrada.is_dir():
                    num_arquivos = sum(1 for _ in scandir.scandir(subentrada.path) if _.is_file())
                    total_arquivos += num_arquivos
            resultado[entrada.name] = total_arquivos
    return resultado

diretorio_principal = 'C:/Users/madus/OneDrive/Área de Trabalho/dev/trabalhoEDL/PokemonSplit'
resultado = contar_arquivos_em_subpastas(diretorio_principal)

soma = 0
for pasta, total_arquivos in resultado.items():
    print(f'{pasta} - {total_arquivos} arquivos')
    soma = soma + total_arquivos
print(f'Total database - {soma} arquivos')