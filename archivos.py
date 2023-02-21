file = open('alumnos.txt', 'r')
nombres = file.readlines()
print(nombres)
file.close()