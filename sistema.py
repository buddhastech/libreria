def menu():

    menu_opcion = input("""
    1- Busquedas
    2- Mantenimiento
    3- Salir
    
    Indique una opcion: """)
    
    return menu_opcion

def menu_secundario():
    
    menu_opcion = input("""
    1- Libros
    2- Estudiantes
    3- Prestamos
    4- Salir a menu principal
    
    Indique una opcion: """)
        
    return menu_opcion

def menu_busqueda_libros():
    
    menu_opcion = input("""
    1- Con filtros
    2- Sin filtros
    
    Indique una opcion: """)

    return menu_opcion


# busqueda de todos los registros de las diferentes entidades    
def busqueda_de_estudiantes():
    
    archivo = open('estudiantes.txt', 'r')
    registros = archivo.readlines()
    
    print("\n" + " " *12 + "-"*50)
    
    for registro in registros:
        
            
        registro = registro.split(',')
        
        if registro:
        
            print("""
            Cedula: {} 
            Nombre: {}
            Carrera: {}""".format(registro[0], registro[1] + " " + registro[2] + " " + registro[3], registro[4]))

            print(" " *12 + "-"*50)

def busqueda_de_libros():
    
    archivo = open('libros.txt', 'r')
    libros = archivo.readlines()
    
    print("\n" + " " *12 + "-"*50)
    
    for libro in libros:
        libro = libro.split(',')
       
        print("""
            ID Libro: {}
            Titulo: {}
            Autor: {}
            Anio: {} 
        """.format(libro[0], libro[1], libro[2], libro[3]))
        
        print(" " *12 + "-"*50)
   
def busqueda_de_prestamos():

    archivo = open('prestamos.txt', 'r')
    prestamos = archivo.readlines()
    
    print("\n" + " " *12 + "-"*50)
    
    for prestamo in prestamos:
        prestamo = prestamo.split(',')
        
        print("""
            ID Prestamo: {}
            ID Libro: {}
            Carne de estudiante: {}
            Fecha de entrega: {}
        """.format(prestamo[0], prestamo[1], prestamo[2], prestamo[3]))

        print(" " *12 + "-"*50)


# metodo para generar id del prestamo automaticamente
def generador_de_id_prestamo(ultimo_id_prestamo):
    
    nuevo_id = "PRE"
    
    for caracter in ultimo_id_prestamo:
        if caracter.isdigit():
            
            if int(caracter) != 0:
                caracter = int(caracter) + 1
        
            nuevo_id += str(caracter)
    
    return nuevo_id


# metodos para inclusion    
def incluir_estudiante(carne, nombre, apellido1, apellido2, carrera):
    
    archivo = open('estudiantes.txt', 'r+')
    archivo.readlines()
    posicion = archivo.tell() # posicion del puntero en el archivo
    archivo.seek(posicion)
    
    registro = '\n{},{},{},{},{}'.format(carne, nombre, apellido1, apellido2, carrera)
    archivo.write(registro)
    archivo.close()
    
    print("\nEstudiante agregado con exito\n")
    
def incluir_libros(id_libro, titulo, autor, anio):
    
    archivo = open('libros.txt', 'r+')
    libros = archivo.readlines()
    
    libro_encontrado = False
    
    for indice in range(len(libros)): # transforma cada libro en una lista
        
        libros[indice] = libros[indice].split(',')
    
    for libro in libros:
        if id_libro in libro[0]:
            libro_encontrado = True
    
    if not(libro_encontrado):
    
        posicion = archivo.tell() # posicion del puntero en el archivo
        archivo.seek(posicion)
    
        registro = '\n{},{},{},{}'.format(id_libro, titulo, autor, anio)
        archivo.write(registro)
        archivo.close()
        
        print("\nLibro agregado con exito\n")
    
        
    else:
        print("\n")
        print("El ID ya existe...")
        print("\n")
    
def incluir_prestamos(id_libro, carne, fecha_entrega):
    
    archivo = open('prestamos.txt', 'r+')
    prestamos = archivo.readlines()
    
    for indice in range(len(prestamos)): # transforma cada libro en una lista
        
        prestamos[indice] = prestamos[indice].split(',')
    
    id_prestamo = generador_de_id_prestamo(prestamos[-1][0])
    
    
    posicion = archivo.tell() # posicion del puntero en el archivo
    archivo.seek(posicion)
    
    registro = '\n{},{},{},{}'.format(id_prestamo, id_libro, carne, fecha_entrega)
    archivo.write(registro)
    archivo.close()
    
    print("\nPrestamo agregado con exito\n")


# metodos para excluir
def excluir_libro(id_libro):
    
    archivo = open('libros.txt', 'r+')
    libros = archivo.readlines()
    
    for indice in range(len(libros)): # transforma cada libro en una lista
        
        libros[indice] = libros[indice].split(',')
    
    for libro in libros: # recorre todos los libros
        
        if libro[0] == id_libro: # compara el id del libro de cada libro con el introducido por parametro
            libros.remove(libro) # remueve el libro de la lista de libros
        
    libros_actualizados = []
    
    for libro in libros:
        
        registro = "{},{},{},{}".format(libro[0], libro[1], libro[2], libro[3])
        libros_actualizados.append(registro)
    
    print(libros_actualizados)
    
    archivo.truncate(0)
    archivo.seek(0)
    archivo.writelines(libros_actualizados)
    archivo.close()

def excluir_estudiante(cedula):
    
    archivo = open('estudiantes.txt', 'r+')
    estudiantes = archivo.readlines()
    
    for indice in range(len(estudiantes)): # transforma cada libro en una lista
        
        estudiantes[indice] = estudiantes[indice].split(',')
    
    for estudiante in estudiantes: # recorre todos los libros
        
        if estudiante[0] == cedula: # compara el id del libro de cada libro con el introducido por parametro
            estudiantes.remove(estudiante) # remueve el libro de la lista de libros
        
    estudiantes_actualizados = []
    
    for estudiante in estudiantes:
        
        registro = "{},{},{},{},{}".format(estudiante[0], estudiante[1], estudiante[2], estudiante[3],estudiante[4])
        estudiantes_actualizados.append(registro)
    
    print(estudiantes_actualizados)
    
    archivo.truncate(0)
    archivo.seek(0)
    archivo.writelines(estudiantes_actualizados)
    archivo.close()

def excluir_prestamos(id_prestamo):
    
    archivo = open('prestamos.txt', 'r+')
    prestamos = archivo.readlines()
    
    for indice in range(len(prestamos)): # transforma cada libro en una lista
        
        prestamos[indice] = prestamos[indice].split(',')
    
    for prestamo in prestamos: # recorre todos los libros
        
        if prestamo[0] == id_prestamo: # compara el id del libro de cada libro con el introducido por parametro
            prestamos.remove(prestamo) # remueve el libro de la lista de libros
        
    prestamos_actualizados = []
    
    for prestamo in prestamos:
        
        registro = "{},{},{},{}".format(prestamo[0], prestamo[1], prestamo[2], prestamo[3])
        prestamos_actualizados.append(registro)
    
    print(prestamos_actualizados)
    
    archivo.truncate(0)
    archivo.seek(0)
    archivo.writelines(prestamos_actualizados)
    archivo.close()



# busqueda de un libro por filtros
def busqueda_de_libro(titulo, autor, anio):
   
    archivo = open('libros.txt', 'r+')
    libros = archivo.readlines()
    
    libros_filtrados = []
 
    for indice in range(len(libros)): # transforma cada libro en una lista
        
        libros[indice] = libros[indice].split(',')

    for libro in libros:
        
        libro[3] = libro[3].rstrip('\n')
        
        if titulo and autor and anio:
            
            if libro[1] == titulo and libro[2] == autor and int(libro[3]) >= int(anio):
                
                libros_filtrados.append(libro)
              
        
        if titulo and autor == "" and anio == "":
            
            if libro[1] == titulo:
                libros_filtrados.append(libro)
        
        if autor and titulo == "" and anio == "":
            
            if libro[2] == autor:
                libros_filtrados.append(libro)
    
        if anio and titulo == "" and autor == "":
          
            if int(libro[3]) >= int(anio):
                libros_filtrados.append(libro)
    

    if libros_filtrados:
        
        for libro_filtrado in libros_filtrados:
               
            print(" " *12 + "-"*50)
            
            print("""
            ID Libro: {}
            Titulo: {}
            Autor: {}
            Anio: {} 
            """.format(libro_filtrado[0], libro_filtrado[1], libro_filtrado[2], libro_filtrado[3]))

            print(" " *12 + "-"*50)
    else:
       
        print("\nNo hay libros encontrados...\n")
        



while True:

    opcion_menu_1 = menu()
    
    if opcion_menu_1 == "1":
        
        opcion_menu_2 = menu_secundario()
        
        if opcion_menu_2 == "1":
            
            opcion_busqueda = menu_busqueda_libros()
            
            if opcion_busqueda == "1":
                
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el autor del libro: ")
                anio = input("Ingrese el anio: ")
                
                busqueda_de_libro(titulo, autor, anio)
            
            if opcion_busqueda == "2":
                busqueda_de_libros()
        
        elif opcion_menu_2 == "2":
            
            busqueda_de_estudiantes()
         
        elif opcion_menu_2 == "3":
            
            busqueda_de_prestamos()
            
    elif opcion_menu_1 == "2":
        
        opcion_mantenimiento = menu_secundario()
        
        if opcion_mantenimiento == "1":
            
            id_libro = input("Indique el ID del libro: ")
            titulo = input("Indique el titulo del libro: ")
            autor = input("Indique el autor del libro: ")
            anio = input("Indique el anio de publicacion: ")
            
            incluir_libros(id_libro, titulo, autor, anio)
            
        elif opcion_mantenimiento == "2":
            
            carne = input("Indique el carne de estudiante: ")
            nombre = input("Indique el nombre del estudiante: ")
            apellido1 = input("Indique el primer apellido del estudiante: ")
            apellido2 = input("Indique el segundo apellido del estudiante: ")
            carrera = input("Indique la carrera a la que pertenece: ")
            
            incluir_estudiante(carne, nombre, apellido1, apellido2, carrera)
        
        elif opcion_mantenimiento == "3":
            
            busqueda_de_libros()
            print("\n")
            
            id_libro = input("Indique el ID del Libro: ")
            carne = input("Indique el carne del estudiante: ")
            fecha_entrega = input("Indique la fecha de entrega: ")
            
            incluir_prestamos(id_libro, carne, fecha_entrega)
    
    else:
        break

