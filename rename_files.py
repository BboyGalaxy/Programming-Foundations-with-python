import os

def rename_files():
	file_list = os.listdir(r"E:\Udacity\3-Programming fundation with python\prank")
	#print file_list
	saved_path = os.getcwd()
	os.chdir(r"E:\Udacity\3-Programming fundation with python\prank")
	for file_name in file_list:
		print("Nombre antiguo -- " + file_name)
		print("nombre nuevo -- " + file_name.translate(None,"0123456789"))
		os.rename(file_name,file_name.translate(None,"0123456789"))
	os.chdir(saved_path)

rename_files()