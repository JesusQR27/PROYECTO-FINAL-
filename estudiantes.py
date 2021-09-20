import os
from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def Carreras():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Carrera:")
   gotoxy(35,5);descarrera = input()
   archiCarrera = Archivo("./datos/carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def Materias():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")    
    gotoxy(20,4);print("Materia:")
    gotoxy(28,4);mate=input()
    archiMateria = Archivo("./datos/materia.txt",";")
    lisMateria = archiMateria.leer()
    if lisMateria : idSig = int(lisMateria[-1][0])+1
    else: idSig=1
    entMateria = Materia(idSig,mate)
    datos = entMateria.getMateria()
    datos = ';'.join(datos)
    archiMateria.escribir([datos],"a")
    
    

def Periodos():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE PERIODO")   
    gotoxy(20,4);print("periodo:")
    gotoxy(20,5);print("descripcion:")
    gotoxy(28,4);per=input()
    gotoxy(32,5);des=input()
    archiPeriodo = Archivo("./datos/periodo.txt",";")
    # lisPeriodo = archiPeriodo.leer()
    # if lisPeriodo : idSig = int(lisPeriodo[-1][0])+1
    # else: idSig=1
    entPeriodo = Periodo(per,des)
    datos = entPeriodo.getPeriodo()
    datos = ';'.join(datos)
    archiPeriodo.escribir([datos],"a")
    

def Profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Titulo: : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   ced=validar.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
       
def Estudiantes():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES ")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Dirección:  ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(25,4);nom = input()
   ced=validar.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(25,6);dir = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiEstudiantes = Archivo("./datos/estudiantes.txt")
        lisEstudiantes = archiEstudiantes.leer()
        if lisEstudiantes : idSig = int(lisEstudiantes[-1][0])+1
        else: idSig=1
        entEstudiantes = Estudiante(idSig,nom,ced,dir,tel)
        datos = entEstudiantes.getEstudiante()
        datos = ';'.join(datos)
        archiEstudiantes.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")  

def Matriculas ():
   borrarPantalla()
   
   validar = Valida() 
   gotoxy(20,2);print("INGRESO DE MATRICULA")
   gotoxy(15,4);print("Estudiantes ID[  ]: ")
   gotoxy(15,5);print("Carrera ID[   ]:")
   gotoxy(15,6);print("Periodo ID[       ]:")
   gotoxy(15,7);print("Valor : ")
   lisEstudiantes,entEstudiantes = [],None
   while not lisEstudiantes:
      gotoxy(30,4);id = input().upper()
      archiEstudiantes = Archivo("./datos/estudiantes.txt")
      lisEstudiantes = archiEstudiantes.buscar(id)
      if lisEstudiantes:
          entEstudiantes = Estudiante(lisEstudiantes[0],lisEstudiantes[1],lisEstudiantes[2],lisEstudiantes[3],lisEstudiantes[4]) 
          gotoxy(34,4);print(entEstudiantes.nombre)
      else: 
         gotoxy(33,4);print("No existe estudiantes con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,4);print(" "*40)
#    gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
#    gotoxy(54,10);grabar = input().lower()
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(26,5);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,5);print(entCarrera.descripcion)
      else: 
         gotoxy(33,5);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,5);print(" "*40)
#    gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
#    gotoxy(54,10);grabar = input().lower()
   lisPeriodos,entPeriodos = [],None
   while not lisPeriodos:
      gotoxy(26,6);id = input().upper()
      archiPeriodos = Archivo("./datos/periodo.txt")
      lisPeriodos = archiPeriodos.buscar(id)
      if lisPeriodos:
          entPeriodos = Periodo(lisPeriodos[0],lisPeriodos[1]) 
          gotoxy(35,6);print(entPeriodos.descripcion)
      else: 
         gotoxy(33,6);print("No existe Periodos con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,6);print(" "*40)
   
   val=validar.solo_numeros("Error: Solo numeros",22,7)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiMatriculas = Archivo("./datos/matricula.txt")
        lisMatriculas = archiMatriculas.leer()
        if lisMatriculas : idSig = int(lisMatriculas[-1][0])+1
        else: idSig=1
        entMatriculas = Matricula(idSig,entEstudiantes,entCarrera,entPeriodos,val)
        datos = entMatriculas.getMatricula()
        datos = ';'.join(datos)
        archiMatriculas.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente \n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")
   
def notas():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE NOTAS ")
   gotoxy(15,4);print("Periodo ID[        ]:")
   gotoxy(15,5);print("Estudiantes ID[  ]: ")
   gotoxy(15,6);print("Materia ID  [ ] :")
   gotoxy(15,7);print("Profesor ID[  ]: " )
   gotoxy(15,8);print("Nota 1: ")
   gotoxy(15,9);print("Nota 2: ")
   lisPeriodos,entPeriodos = [],None
   while not lisPeriodos:
      gotoxy(27,4);id = input().upper()
      archiPeriodos = Archivo("./datos/periodo.txt")
      lisPeriodos = archiPeriodos.buscar(id)
      if lisPeriodos:
          entPeriodos = Periodo(lisPeriodos[0],lisPeriodos[1]) 
          gotoxy(36,4);print(entPeriodos.descripcion)
      else: 
         gotoxy(36,4);print("No existe Periodos con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(36,4);print(" "*40)
         
   lisEstudiantes,entEstudiantes = [],None
   while not lisEstudiantes:
      gotoxy(31,5);id = input().upper()
      archiEstudiantes = Archivo("./datos/estudiantes.txt")
      lisEstudiantes = archiEstudiantes.buscar(id)
      if lisEstudiantes:
          entEstudiantes = Estudiante(lisEstudiantes[0],lisEstudiantes[1],lisEstudiantes[2],lisEstudiantes[3],lisEstudiantes[4]) 
          gotoxy(34,5);print(entEstudiantes.nombre)
      else: 
         gotoxy(34,5);print("No existe estudiantes con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(34,5);print(" "*40)
         
   lisMaterias,entMaterias = [],None
   while not lisMaterias:
      gotoxy(28,6);id = input().upper()
      archiMaterias = Archivo("./datos/materia.txt")
      lisMaterias = archiMaterias.buscar(id)
      if lisMaterias:
          entMaterias = Materia(lisMaterias[0],lisMaterias[1]) 
          gotoxy(33,6);print(entMaterias.descripcion)
      else: 
         gotoxy(33,6);print("No existe Materias con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,6);print(" "*40)
    
   lisProfesores,entProfesores = [],None
   while not lisProfesores:
      gotoxy(28,7);id = input().upper()
      archiProfesores = Archivo("./datos/profesor.txt")
      lisProfesores = archiProfesores.buscar(id)
      if lisProfesores:
          entProfesores = Profesor(lisProfesores[0],lisProfesores[1],lisProfesores[2],lisProfesores[3],lisProfesores[4],lisProfesores[5]) 
          gotoxy(33,7);print(entProfesores.nombre)
      else: 
         gotoxy(33,7);print("No existe Profesores con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,7);print(" "*40)
         
   not1=validar.solo_numeros("Error: Solo numeros",23,8)
   not2=validar.solo_numeros("Error: Solo numeros",23,9)
   
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   
   if grabar == "s":
        archiNotas = Archivo("./datos/notas.txt")
        lisNotas = archiNotas.leer()
        if lisNotas : idSig = int(lisNotas[-1][0])+1
        else: idSig=1
        entNotas = Notas(idSig,entPeriodos,entEstudiantes,entMaterias,entProfesores,not1,not2)
        datos = entNotas.getEstudiantes()
        datos = ';'.join(datos)
        archiNotas.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
       
       
        
# Menu Principal
opc=''
while opc !='5':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                Carreras()
        
            elif opc1=="2":
                
                Materias()
                
            elif opc1=="3":
                Periodos()
            
            elif opc1 == "4":
                Profesores()
        
            elif opc1 == "5":
                Estudiantes()
 
    if opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
             Matriculas()
           
            elif opc2 == "2":
                pass
            
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
             notas()
            
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

