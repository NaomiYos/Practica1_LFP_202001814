from listapelis import Lista
from colorama import Fore
Lis=Lista()
class Lectorcito:
    def openFile(self):
            #file=input("Ingrese la ruta del archivo ")
            file="archivo.lfp"
            if file is None:
                print("No has seleccioado ningun archivo.".center(50, "!"))
            else:
                extension = file[-3:]
                if extension == "lfp":
                    with open(file, 'r', encoding='utf-8') as infile:
                        
                        for line in infile.readlines():
                                        
                                        actores=[]
                                        dato1=line.split(";")
                                        nombre=dato1[0].strip(" ")
                                        anio=dato1[2].strip(" ")
                                        gen=dato1[3].lstrip(" ")
                                        gen=gen.rstrip("\n")
                                        
                                        arreglo=dato1[1].split(",") 
                                        for actor in arreglo:
                                              actor1=actor.strip(" ")
                                              actores.append(actor1)
                                              
                                              
                                              
                                        print(actor)
                                        Lis.insertar(nombre,actores,anio,gen)
                else:
                    print("Archivo incorrecto, debe tener extensión LFP ")
    def almacenar(self,line):
                    dato=line.split(";")
                    print(dato)

                    actor=dato[1].split(",")
                    print(actor)
                    Lis.insertar(dato[0],actor,dato[2],dato[3])
    def GestionarPelis(self):
          regresar=False
          while regresar!=True:
            Lis.NamePelicula()
            print(Fore.BLUE+"Ingresa el número de la película que deseas consultar:")
            print(Fore.MAGENTA+"Para volver al menú principal preciona x")
            res=input()
            if res.isdigit():
                  Lis.getPeli(res)
            elif res=="x":
                  regresar=True
            else:
                  print("Ingresa una opción válida")
    def Filtrar(self):
          regresarf=False
          while regresarf!=True:
                print(Fore.BLUE+"1. Filtrar por Actores")
                print(Fore.BLUE+"2. Filtrar por Año")
                print(Fore.BLUE+"3. Filtrar por Género")
                print(Fore.YELLOW+"Ingresa el número de la opción que deseas consultar: ")
                print(Fore.MAGENTA+"Para volver al menú principal preciona x")
                res=input()
                if res.isdigit():
                  if res=="1":
                       act=input(Fore.LIGHTWHITE_EX+"Ingresa el nombre del actor que deseas buscar: ")
                       if act.isdigit():
                             print(Fore.RED+"Estás ingresando un número y eso no es un nombre válido")
                       else:
                        respuesta=Lis.filtraractor(act)
                        if respuesta!=None:
                                print(Fore.GREEN+"Estas son las películas en las que aparece "+act+":")
                                print(respuesta)
                        else:
                                print(Fore.RED+"No hemos encontrado a un actor con ese nombre, intenta de nuevo")
                  elif res=="2":
                       an=input(Fore.LIGHTWHITE_EX+"Ingresa el año de las peliculas que deseas buscar: ")
                       if an.isdigit():
                        respuesta=Lis.filtraranio(an)
                        if respuesta!=None:
                                print(Fore.GREEN+"Estas son las películas del año "+an+":")
                                print(respuesta)
                        else:
                                print(Fore.RED+"No hemos encontrado películas de ese año, intenta de nuevo")
                       else:
                            print(Fore.RED+"No es un año válido")
                       
                  elif res=="3":
                       
                       gen=input(Fore.LIGHTWHITE_EX+"Ingresa el género de las peliculas que deseas buscar: ")
                       if gen.isdigit():
                             print(Fore.RED+"Estás ingresando un número y eso no es un género válido")
                       else:
                        respuesta=Lis.filtrargener(gen)
                        if respuesta!=None:
                                print(Fore.GREEN+"Estas son las películas del género "+gen+":")
                                print(respuesta)
                        
                        else:
                                print(Fore.RED+"No hemos encontrado películas de ese género, intenta de nuevo")
                        
                  else:
                       print(Fore.RED+"opcion incorrecta")
                elif res=="x":
                    regresarf=True
                else:
                    print("Ingresa una opción válida")
            
                  