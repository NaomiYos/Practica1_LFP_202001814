from colorama import Fore, Back, Style
from pelicula import Pelicula
from graphviz import Digraph
class Lista():
    def __init__(self) :
        self.peliculas=[]
        self.actoresl=[]
    def insertar(self,nombre,actores,anio,genero):
         nuevo= Pelicula(nombre,actores,anio,genero)
         self.peliculas.append(nuevo)
      
         self.quitardupicidad()
    def NamePelicula(self):
        for i in range(0,len(self.peliculas)):
            print(str(i+1)+".  "+str(self.peliculas[i].nombre))

    def insertaractor(self,actr):
        
        if len(self.actoresl)==0:
         self.actoresl.append(actr)
        else:   
          for i in range(0,len(self.actoresl)):
            encontrado=False
            if actr==self.actoresl[i]:
                encontrado=True
            if encontrado==False:
                self.actoresl.append(actr)
                break
    def imprimiractor(self):
          for i in range(0,len(self.actoresl)):
            print(str(i+1)+".  "+str(self.actoresl[i]))

    def quitardupicidad(self):
        
        x=len(self.peliculas)
        #print ("Cantidad:" + str(x))
        v=""
        if x>1:
            for e in range(1,x-1 ):
                v=self.peliculas[e].nombre
                #for y in range(0,e-1):
                y=0
                while y <= e-1:
                    if v==self.peliculas[y].nombre and self.peliculas[y].nombre!="x" :
                       self.peliculas[y].nombre=self.peliculas[e].nombre
                       self.peliculas[y].actores=self.peliculas[e].actores
                       self.peliculas[y].anio=self.peliculas[e].anio
                       self.peliculas[y].genero=self.peliculas[e].genero
                       self.peliculas[e].nombre="x"
                       break
                    y+=1


        for r in range(x-1,0,-1):
            if self.peliculas[r].nombre=="x":
               self.peliculas.pop(r) 
    def getPeli(self,pos):

        posicion=int(pos)-1
        
        print(Fore.BLUE+"Nombre película: "+str(self.peliculas[posicion].nombre)+ "Género: "+str(self.peliculas[posicion].genero)+" Año: "+str(self.peliculas[posicion].anio))
        print(Fore.GREEN+"Lista de Actores:")
        for actor in self.peliculas[posicion].actores:
            print(str(actor))
    def filtraractor(self,actor):
        listapelis=[]
        for i in range(0,len(self.peliculas)):
            for actorlista in self.peliculas[i].actores:
                if actor==actorlista:
                    listapelis.append(self.peliculas[i].nombre)
        if len(listapelis)==0:
            return None
        else:
            return listapelis
    def filtraranio(self,anio):
        listapelis=[]
        for i in range(0,len(self.peliculas)):
                if anio==self.peliculas[i].anio:
                    listapelis.append(self.peliculas[i].nombre)
        if len(listapelis)==0:
            return None
        else:
            return listapelis
    def filtrargener(self,genero):
        listapelis=[]
        for i in range(0,len(self.peliculas)):
                if genero==self.peliculas[i].genero:
                    listapelis.append(self.peliculas[i].nombre)
        if len(listapelis)==0:
            return None
        else:
            return listapelis
    def graficar(self):
        dot = Digraph('G', filename='grafica.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'

        contador = 0
        c = Digraph('child')
        c.attr(rank='same')

        for i in range(0,len(self.peliculas)):
            c.node(str(contador),str(self.peliculas[i].nombre)+"\n"+str(self.peliculas[i].anio)+"|"+ str(self.peliculas[i].genero))
            contador+=1
        
        d = Digraph('child')
        d.attr(rank='same')
        cont=0
        for i in range(0,len(self.actoresl)):
           d.node("a"+str(cont),str(self.actoresl[i]),color="green")
           cont+=1
        
 
            

        
        
        dot.subgraph(c)
        dot.subgraph(d)

        listapelis=[]
        for i in range(0,len(self.peliculas)):
            for actorlista in self.peliculas[i].actores:
                for j in range(0,len(self.actoresl)):
                    if self.actoresl[j]==actorlista:
                        dot.edge("a"+str(j), str(i))
      
        
        
        

       # dot.edge(str(1), str(contador))

        dot.view()

         


