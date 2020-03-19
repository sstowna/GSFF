#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests

###############################Atualizar################################

get_lastest_version = requests.get("https://raw.githubusercontent.com/JhinScripter/GSFF/master/version.jhinscripter")
lastest_version = get_lastest_version.text
clean_text_ver = lastest_version.replace("\n", "")

get_current_version = open("../version.jhinscripter", "r")
current_version = get_current_version.read()

if current_version == clean_text_ver:
	pass
else:
	print("Update avaliable!\nhttps://github.com/JhinScripter/GSFF\n")

###############################Atualizar################################

print("   ___________ ____________")
print("  / ____/ ___// ____/ ____/")
print(" / / __ \\__ \\/ /_  / /_    ")
print("/ /_/ /___/ / __/ / __/    ")
print("\\____//____/_/   /_/       ")
print("                           ")
print("https://github.com/JhinScripter/GSFF")

pasta_dos_ficheiros = "../files"
string_to_search = raw_input("String: ")

get_files = os.listdir(folder_of_the_files)
for the_file in get_files:
	folder_and_file = folder_of_the_files + "/" + the_file
	the_file_searching = open(folder_and_file, "r")
	if string_to_search in the_file_searching.read():
		print("I found the string on the file: " + folder_and_file)