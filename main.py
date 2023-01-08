import os
import sys
import json 

import twilio
import pandas
import requests
from os import remove
from os import  path
from  colorama import init,Fore
#Home programa Este Programa Ahra Casi Todo Por mi Desde Guardar Un Docunento A Combiar Renombrar Y mas vercion 1.1.3 

#Recurse Home
title_descript = "Proyecto Aris"
print(Fore.YELLOW + title_descript.center(41,"="))

#recurse Sistexis function basic
Subir = "~v"
aceptar = "~a"
cancelar = "~c"
enviar = "~set"
copiar = "~copy"
renombrar = "~newname"
escribir = "~while"
cortar = "~cut"
create = "Created"
file_arch = "-Archive"
file_run = "a-"
file_run += create + file_arch;
Archive = "Archive"
mostrar_Carpt = "ls"
ver_list = "cd"
name = "Name"
Archive += name
eliminar = "-delete"
eliminar_Archivos = "Archive"
eliminar_Archivos += eliminar
url = "home/storage/emulated/0/Download/file.txt"
#recurse open-file python 
db = "W"
db_t = ".txt"
db_csv = ".csv"
rutate = "/storage/emulated/0/proyecto Aris/"
rutate += db_t
print(file_run)
#recurse movilidad
def movility(seach):
	if seach == eliminar_Archivos:
		 date = input('Rute/o name/:')
		 path.exists(date)
		 remove(date)
	else: 
	     print('none')
	
	
	
	return seach()

#recurse Open file 
def Ope(rutate):
	 rutate = __file__
	 rutate_formate = ".txt"
	 c =  input('nombre de Archivo:/MiArchivo')
	 c += rutate + c + rutate_formate
	 e = input('Formato De Archivo:/txt/cvs/json')
	 t = input('Titulo Archivo')
	 f = input('Escribe los Datos ')
	 
	 
	
	
	
	
while True:
	seach = input('')
	if seach == eliminar_Archivos:
		movility(seach)
	if seach == ver_list:
		print('Carpeta Abtual',__file__)
	if seach == file_run:
		Ope(rutate)
	else: print('Comando No Valido ')
	

	



