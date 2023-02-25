from colorama import Fore, Back, Style
from lector import Lectorcito
Lec=Lectorcito()


class Menu():
    def menu(self):
        flagC=False
        print(Fore.MAGENTA+"""
          __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / | Lenguajes Formales y de Programación | \ |
          | / |             Sección: A+              | \ |
          |___| Naomi Rashel Yos Cujcuj 202001814    |___|
         (_____)------------------------------------(_____) """)
        mostrar=input("Presiona m para mostrar el menú principal ")
        if mostrar=="m":
            mm=True
        else:
            mm=False
        while mm==True:
            print(Fore.LIGHTBLACK_EX+"----MENU----")
            print(Fore.CYAN+ "1. Cargar Archivo")
            print(Fore.CYAN+ "2. Gestionar películas")
            print(Fore.CYAN+ "3. Filtrado")
            print(Fore.CYAN+ "4. Gráficas")
            print(Fore.CYAN+ "5. Salir")
            opcion=input(Fore.YELLOW+'Ingrese una opcion: ')
           

            if opcion=="1":
                Lec.openFile()
                flagC=True
            elif opcion == '2':
                if flagC:
                    Lec.GestionarPelis()     
                else:
                    print("Cargue el archivo primero")  
            elif opcion == '3':
                if flagC:
                    Lec.Filtrar()   
                else:
                    print("Cargue el archivo primero")  
            elif opcion == '4':
                if flagC:
                    Lec.Graficar() 
                else:
                    print("Cargue el archivo primero")  
            elif opcion == '5':
                print("¡Adiós!")
                mm=False
            else:
                print("Opción incorrecta")

            
                


    