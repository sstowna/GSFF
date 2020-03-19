#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests

###############################Atualizar################################

pegar_versao_atualizada = requests.get("https://raw.githubusercontent.com/JhinScripter/GSFF/master/version.jhinscripter")
versao_atualizada = pegar_versao_atualizada.text
clean_text_ver = versao_atualizada.replace("\n", "")

pegar_versao_atual = open("../version.jhinscripter", "r")
versao_atual = pegar_versao_atual.read()

if versao_atual == clean_text_ver:
	pass
else:
	print("Atualização disponivel!\nhttps://github.com/JhinScripter/GSFF\n")

###############################Atualizar################################

print("   ___________ ____________")
print("  / ____/ ___// ____/ ____/")
print(" / / __ \\__ \\/ /_  / /_    ")
print("/ /_/ /___/ / __/ / __/    ")
print("\\____//____/_/   /_/       ")
print("                           ")
print("https://github.com/JhinScripter/GSFF")

pasta_dos_ficheiros = "../files"
string_para_achar = raw_input("String: ")

pegar_ficheiros = os.listdir(pasta_dos_ficheiros)
for ficheiro in pegar_ficheiros:
	diretorio_e_ficheiro_atual = pasta_dos_ficheiros + "/" + ficheiro
	ficheiro_atual = open(diretorio_e_ficheiro_atual, "r")
	if string_para_achar in ficheiro_atual.read():
		print("Achei a string no arquivo: " + diretorio_e_ficheiro_atual)