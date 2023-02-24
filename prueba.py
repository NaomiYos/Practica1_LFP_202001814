data="""The Avengers; Robert Downey Jr,Chris Evans,Chris Hemsworth ; 2012 ; Ficcion
Spiderman;Tobey Maguire,Kirsten Dunst,Willem Dafoe;2002;Accion
"""
file="archivo.lfp"
nombre=" naomi\n"
nombre=nombre.lstrip(" ")
nombre=nombre.rstrip("\n")
print(nombre)
"""with open(file, 'r', encoding='utf-8') as infile:
                        

    for line in infile.readlines():
                    print("line")
                    dato=line.split(";")
                    print(dato)
                    actor=dato[1].split(",")
                    print(actor)
                   # for i in range(0,len(self.peliculas)):
                    listita=[1]"""