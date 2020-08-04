from io import open
#write w--read r--append a
archivo=open("textito.txt","r")
print(archivo.read(20))
#archivo.seek(20)
print(archivo.read())
'''
archivo.write("\nsigo funcionando")
archivo.close()
''''''
lineas=archivo.readlines()
archivo.close()
print(lineas)
''''''
txto=archivo.read()
archivo.close()
print(txto)
'''
#frase="hola mundo en otro archivo \n vamossssss \n funcione puto"
#archivo.write(frase)
#archivo.close()