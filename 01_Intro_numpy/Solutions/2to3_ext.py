def python23(line, cell):

    ip = get_ipython()

    # Definimos un string que contendra los parentesis necesarios, que ejecutaremos mas adelante.
    final_cell = ""
    # Separamos nuestro string en listas de palabras separadas por un salto de linea.
    lineas = cell.split('\n')

    #Recorremos estas palabras, y si se encuentra la palabra string, se procede a separar esa linea en 2:
    #la primera parte seran las identaciones, mientras que la segunda parte sera el string en comillas al
    #cual debemos colocar los parentesis.
    for i in range(len(lineas)):
    	if('print' in lineas[i]):
    		string_parentesis = lineas[i].split('print')

    		#Envolvemos nuestro string en parentesis, y actualizamos la linea.
    		string_parentesis[1] = "(" + string_parentesis[1] + ")"
    		lineas[i] = string_parentesis[0] + 'print ' +string_parentesis[1]

    #Finalmente juntamos todas las lineas con sus espacios respectivos, guardando el resultado en el string 
    #previamente creado.
    for i in range(len(lineas)):
    	final_cell += lineas[i] + '\n'
	
    #Creamos un string con el nombre del archivo que generaremos para guardar el texto con los parentesis
    source_filename = '_2to3ext.py' 
    with open(source_filename, 'w') as f:
        f.write(final_cell)
    #Finalmente ejecutamos el codigo con python3, e imprimimos el resultado deseado.
    output = ip.getoutput("python3 {0:s}".format(
              source_filename))
    print('\n'.join(output))

#Esta funcion cargara nuestro magic al momento que lo llamemos en el notebook.
def load_ipython_extension(ipython):
       ipython.register_magic_function(python23, 'cell')