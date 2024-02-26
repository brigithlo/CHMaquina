from os import fdopen
from time import time,  sleep
import tkinter as tk
from tkinter import *
from tkinter import Label, Scrollbar, scrolledtext as st
import sys
from tkinter import filedialog  as fd
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
    



sintaxis=['nueva','almacene','cargue','lea','sume','reste','multiplique','itere','fin','divida','potencia','modulo','concatene','elimine','extraiga','y','o','no','muestre','imprima','retorne','vaya','vayasi','etiqueta','i','r','c','l']
sintaxis2=['nueva','almacene','cargue','lea','sume','reste','multiplique','divida','potencia','modulo','concatene','elimine','extraiga','Y','O','NO','muestre','imprima','retorne','vaya','vayasi','etiqueta']
sint=['C','I','R']
ventana1=Tk()
#ventana1.iconbitmap(r'C:\Users\jss\chpython\picture_compress.ico')
ventana1.title('CHMaquina')
ventana1.geometry('1100x900')



controlC=IntVar()
controlC=0
listaMemoria=list()
valr=''
valorKernel=StringVar()
valorMemoria=StringVar()
valorVelocidad=StringVar()
conty=0
tota_lineas=2
contenido2=[]
Necesaria=0
lista_linea=list()
lista_variable=list()
lista_etiqueta=list()
lista_auxiliar=list()
lista_valores=list()
lista_direccion=list()
lista_dimensiones_Programas=list()
cantidadProgramas=0
archi2=list()
acumulador=StringVar()


def salir(self):
   sys.exit(0)

def if_integer(string):
       try:
          int(string)
          return True
       except ValueError:
           return False   
        

def extraer_V_E():
    valor=0
    for x in range(0,len(lista_linea)):
        
        if str(lista_linea[x])=='nueva':
            lista_variable.append(lista_linea[valor + 1])
            #scrolledtext1.insert(END,lista_linea[x+2])
            cadena='C'
            #scrolledtext1.insert(END,cadena[0])
            if if_integer(lista_linea[x+3])==True:
                lista_valores.append(lista_linea[valor+3])
            else:
                band=0
                for u in range(len(sint)):
                 
                 if lista_linea[x+2]==sint[u]: 
                   
                   lista_valores.append(lista_linea[x+3])
                   band=1
                if band==0:    
                    lista_valores.append('0')   
        if str(lista_linea[x])=='etiqueta':
            lista_etiqueta.append(lista_linea[valor + 1])
            
        valor=valor+1


## verificar si la variable ya está ocupada para declarar
def No_Declarada():
    bandf=0
    for x in range(0,len(lista_linea)):
       
        for t in range(len(sintaxis)):
           # scrolledtext1.insert(END,'nO ENTRO')
            if lista_linea[x].lower()==sintaxis[t]:
               # scrolledtext1.insert(END, 'si ENTRO')
                bandf=1
                
                

        if bandf==0:
         
           for y in range(x+1):
               
            

               if lista_linea[x]==lista_linea[y]:
                  
                   #scrolledtext1.insert(END,lista_linea[x])
                   if if_integer(lista_linea[x])==True:
                      
                       break
                   else:
                     if lista_linea[y-3]=='nueva':
                              break
                    
                     
                     if lista_linea[y-1]=='nueva':
                      #  scrolledtext1.insert(END,'\n BIEN')
                        break
                     else:
                        
                         if lista_linea[x]!='':
                           var=2
                           messagebox.showinfo(message="Error... Hay una variable que no se ha declarado",title="Declaracion-Variable")
                           scrolledtext1.insert(END,'\nError...No se ha declarado la variable >> ')
                           scrolledtext1.insert(END, lista_linea[x])
                           return var
      
           #scrolledtext1.insert(END,'\n Error.. Hay una variable que NO decl')             

                         
        else:  
           bandf=0
def excepcion():
    for x in range(len(lista_linea)):
        if lista_linea[x].lower()=='acumulador':
              messagebox.showinfo(message="Error... Variable ACUMULADOR está recervada por el sistema",title="Declaracion-Variable")
              return 0


def Repite_Declarada():
    bandf=0
    for x in range(0,len(lista_linea)):
       
        for t in range(len(sintaxis)):
           # scrolledtext1.insert(END,'nO ENTRO')
            if lista_linea[x].lower==sintaxis[t]:
               # scrolledtext1.insert(END, 'si ENTRO')
                bandf=1
                break
                

        if bandf==0:
         
           for y in range(x-1):
               #scrolledtext1.insert(END,'\n')
               
               if lista_linea[x].lower()==lista_linea[y]:
                   
                   #scrolledtext1.insert(END,lista_linea[x])
                   if if_integer(lista_linea[x])==True:
                      
                       break
                   else:
                     if lista_linea[y-1]=='nueva':
                        var=2
                        if lista_linea[x-1]=='nueva':
                            messagebox.showinfo(message="Error...Hay una variable con el mismo nombre",title="Declaracion-Variable")
                            scrolledtext1.insert(END,'\nError... Ya fue declarada la variable >> ')
                            scrolledtext1.insert(END,lista_linea[x])
                            return var
                            
                    
      
           #scrolledtext1.insert(END,'\n Error.. Hay una variable que NO decl')             

                         
        else:  
           bandf=0







def VerificarTipo():
     flag=0
     for x in range(0,len(lista_linea)):   
       # scrolledtext1.insert(END, 't')  
        #scrolledtext2.insert(END,lista_linea[x+2])
        if lista_linea[x]=='nueva':
           
            flag=0
            for y in range(len(sintaxis)):

               if lista_linea[x+2].upper==sintaxis[y]:
                 #scrolledtext2.insert(END,'  TIPO ')
                 flag=1
                
           
            if flag==1:
                #scrolledtext2.insert(END, lista_linea[x+2])
                var=2
                messagebox.showinfo(message="Error.. Verifica el tipo de las variable",title="TipoVariable")
                scrolledtext1.insert(END, '\nErorr.. Verificar el tipo de la variable >> ')
                scrolledtext1.insert(END,lista_linea[x+1])
                flag=0
               # return var
              

 
def save():
    with open(filename.get(), 'w') as file:
        file.write(scrolledtext3.get('1.0', END))
 

def Limpiar():
    scrolledtext1.delete(1.0,END)
    scrolledtext2.delete(1.0,END)
    scrolledtext3.delete(1.0,END)
    memoria.delete(*memoria.get_children())
    PC.delete(*PC.get_children())
    Acumulador.delete(*PC.get_children())
    
    MJ.delete(*PC.get_children())
    etiqueta.delete(*etiqueta.get_children())
    variable.delete(*variable.get_children())
    global lista_auxiliar
    global lista_etiqueta
    global lista_linea
    global listaMemoria
    global lista_valores
    global lista_variable

    lista_auxiliar=list()
    
    lista_etiqueta=list()
    lista_variable=list()
    listaMemoria=list()
    lista_linea=list()
    lista_valores=list()
    lista_auxiliar.clear()
   
    lista_etiqueta.clear()
    
    lista_variable.clear()

    listaMemoria.clear()
    
    lista_linea.clear()
    
    lista_valores.clear()
    
    control=0
    cantidadProgramas=0



def cargar():  
 #if controlC!=1:

    #scrolledtext1.delete(1.0,END)
    memoria.delete(*memoria.get_children())
    #etiqueta.delete(*etiqueta.get_children())
   # variable.delete(*variable.get_children())
    val1=valorKernel.get()      
    val2=valorMemoria.get() 
    
  
      
######  aqui cargamos el sistema operativo
    cont=0
    Necesaria=0
   
  
    memoria.insert(parent='', index='end',text='0000',values='')
  
    
    for y in range(int(val1)):
        cont=cont+1
        Necesaria=Necesaria+1
        if y>=9:
           s='00'+str(y+1)
        else:
            if y>99:
                 s='0'+str(y+1)
            else:
                 s='000'+str(y+1)     
      

        memoria.insert(parent='', index='end',text=s,values='**CH-SO_V21**')
  
####### aqui cargamos el programa
   
    
    for linea in range(len(listaMemoria)):
        if cont>=9 and cont<=99:
            s='00'+str(cont+1)
        else:
             if cont>99:
               s='0'+str(cont+1)
             else:
                 s='000'+str(cont+1) 
      
        cont=cont+1
       
        memoria.insert(parent='', index='end',text=s,values= listaMemoria[linea])
    contVAR=0
    conETi=0   

    for line in range(len(listaMemoria)):
        
    
      #  scrolledtext1.insert(END, 'E1')    
        if 'nueva' in listaMemoria[line]:
            if contVAR <len(lista_variable):
                #scrolledtext1.insert(END,lista_variable[contVAR])


                if Necesaria>=9 and Necesaria<=99:
                     s='00'+str(Necesaria+1)
                else:
                    if Necesaria>99:
                       s='0'+str(Necesaria+1)
                    else:
                       s='000'+str(Necesaria+1) 
               
                variable.insert(parent='', index='end',text=s,values=lista_variable[contVAR])
               
         
                
                contVAR=contVAR+1
                #scrolledtext1.insert(END,listaMemoria[line])
        else:
            if 'etiqueta' in listaMemoria[line]:
                if len(lista_etiqueta)!=0:
                  #  scrolledtext1.insert(END,lista_etiqueta[conETi])


                    if Necesaria>=9 and Necesaria<=99:
                       s='00'+str(Necesaria+1)
                    else:
                       if Necesaria>99:
                          s='0'+str(Necesaria+1)
                       else:
                          s='000'+str(Necesaria+1) 
                     
                    etiqueta.insert(parent='', index='end',text=s,values=lista_etiqueta[conETi])

                    conETi=conETi+1
                    #scrolledtext1.insert(END, listaMemoria[line])    
        
        Necesaria=Necesaria+1
    for y in range(len(lista_variable)):
        lista_variable.pop(0)
    for y in range(len(lista_etiqueta)) :   
        lista_etiqueta.pop(0)
    for y in range(len(lista_valores)):
        lista_valores.pop(0)        
    #lista_etiqueta.clear()
    #lista_variable.clear() 
    #lista_etiqueta.append(' ')
    #lista_etiqueta.append(' ')
                


     
def AbrirCh():
    var1=0
    var2=0
    var3=0
    var4=0
    valK=valorKernel.get()
    valM=valorMemoria.get()
    cadena=StringVar()
    band=1
    #scrolledtext3.delete(1.0,END)
    nombrerarc=fd.askopenfilename(initialdir="c:/chpython" , title="abrir archivo",filetypes= (("txt file","*.ch"),("todos los archivos","*.*")))
    global cantidadProgramas
    if nombrerarc!='':
        scrolledtext2.insert(END,nombrerarc)
       
        archi=open(nombrerarc,"r", encoding="utf-8")
  
        listar=archi.readlines()
         
        archi.close()
       
        contarPrograma=len(listar)-1
        cantidadProgramas=cantidadProgramas+1

        if contarPrograma  <= int(valM) -int(valK)-len(listaMemoria)-1:
          
          
            #contenido2.append(contenido)

          
          archi=open(nombrerarc,"r", encoding="utf-8")
          contenido=archi.read() 
          archi.close()
         
          scrolledtext3.insert(END,contenido)
          cont=-1
          flarg=1
          for linea in contenido:
               
                cont=cont+1
                var=len(linea)
              
                for iterar in range(var):
                   
                   
                    if contenido[cont]=='/':
                        flarg=0
                    if flarg==0 and contenido[cont]!='\n':
                        break
                    else:
                        flarg=1
                        
                        

                    if linea[iterar]==' ' or linea[iterar]=='\n' or linea[iterar]=='':
                        band=0
                    else:
                
                        if band==0:
                           
                           
                            cadena="".join(lista_auxiliar)
                            lista_linea.append(cadena)
                            lista_auxiliar.clear() 
                            band=1

                        lista_auxiliar.append(linea[iterar]) 
          cadena="".join(lista_auxiliar)
          if cadena!='':               
           lista_linea.append(cadena)
           lista_auxiliar.clear()               
        else: 
            messagebox.showinfo(message="El programa no puede ser cargado, No hay Memoria libre",title="Memoria")
           # scrolledtext1.insert(END, 'EL programa no puede ser cargado porque no hay memoria')    
       # scrolledtext2.insert(END, lista_linea)
        
        
        var1=VerificarTipo()
       # scrolledtext2.insert(END,val)
        var2=excepcion()
        var3=No_Declarada()
       # scrolledtext2.insert(END,val)

        var4=Repite_Declarada()
       # scrolledtext2.insert(END,val)
      
        archi=open(nombrerarc,"r", encoding="utf-8")
        #listar=archi.readlines()
       
       
        if  (var1!=2 and var2!=2) and (var3!=2 and var4!=2):
         
           conti=0
           extraer_V_E()
           for x in range(int(contarPrograma)+1):
               conti=conti+1
               contenido=archi.readline()
               if 'retorne' in contenido:
                   listaMemoria.append(contenido)
                   break
               else:
                   listaMemoria.append(contenido)
           #scrolledtext1.insert(END, conti)
           lista_dimensiones_Programas.append(conti)
           numer=len(lista_variable)
           lista_dimensiones_Programas.append(numer)
          # scrolledtext1.insert(END,lista_dimensiones_Programas)
           val1=valorKernel.get()      
           val2=valorMemoria.get() 
           inter=int(val2)-int(val1)-1
           varb=len(lista_variable)
           ciy=len(listaMemoria)

           if (varb+ciy)<=inter:

               for y in range(len(lista_valores)):
       
            
                catenar= '_ '+ lista_variable[y] + ' _ ' + lista_valores[y]
                listaMemoria.append(catenar)
            
   
  
           else:
                messagebox.showinfo(message="Error.. Memoria insuficiente",title="Memoria")
           archi.close() 
           lista_linea.clear()
           lista_linea.clear()
        else:
            lista_linea.clear()
            lista_auxiliar.clear()
      

#############################################################################################################################
############################################# codigo parala ejecusion ######################################################




def descomponer(stringD):
   listarespaldo=list()
   listarespaldo2=list()
   ban2=1
   for x in range(len(stringD)):
       if stringD[x]==' ' or stringD[x]=='_' or stringD=='\n':
          ban2=0
       else:
           if ban2==0:
                cadena="".join(listarespaldo)
                listarespaldo2.append(cadena)
                listarespaldo.clear()
                ban2=1

           listarespaldo.append(stringD[x]) 
   cadena="".join(listarespaldo)
   listarespaldo2.append(cadena)
   return listarespaldo2 

def iguales(palabra,stringtr):
    lista=descomponer(stringtr)
    for p in range(lista):
        if str(palabra)==str(lista[p]):
            return True
        else:
            return False    

def cargue(acumulador,lista,linea_instrucion,inicio,fin):
   #scrolledtext2.insert(END, inicio)
   #scrolledtext2.insert(END, fin)
   listaA=list()
   listaA2=list()
   listaA.clear()
   listaA2.clear()
   #scrolledtext2.insert(END, linea_instrucion)
   listaA=descomponer(linea_instrucion)
   #scrolledtext2.insert(END, fin)
   #scrolledtext1.insert(END, fin)
   for x in range(inicio,fin):
        
        cade1=listaA[1]  
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        #scrolledtext2.insert(END, cade3)
        if cade1[0] ==cade3[0]:
            # scrolledtext2.insert(END, 'BIEN_1')
         # listaA2=descomponer(lista[x])
          #if listaA[1]==listaA2[0]:
             #scrolledtext2.insert(END, 'BIEN')
             if if_integer(listaA2[1]==True):
                # if acumulador!='':
                     acumulador=str(listaA2[2])
                     #scrolledtext1.insert(END, 'Bien en la funcion cargue')

             else:
                 scrolledtext1.insert(END,'Error.. en la funcion cargue')
   #scrolledtext2.insert(END, 'CARGUE: \n')        
  # scrolledtext2.insert(END,acumulador)        
   return acumulador          
      
              


            
def almacene(acumulador, lista,linea_instrucion,inicio,fin):
    listaA=list()
    listaA2=list()
    listaA2.clear()
    listaA.clear()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1]  
    for x in range(inicio,fin):
        #scrolledtext1.insert(END, lista[x])
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        
        if cade1[0]== cade3[0]:
           
            if if_integer(listaA2[2])==True:
                cadena='_ '+listaA2[1]+' _ '+ acumulador
                lista[x]=cadena
               # scrolledtext2.insert(END, 'ALMAC: \n')
               # scrolledtext2.insert(END, acumulador)

def lea(acumulador, lista,linea_instrucion,inicio,fin):

    ### poner aqui instrucion para leer
    variab=Entry(ventana1).place(x=200,y=200)
    variableValor=variab.get()
    
    # ejemplo lea m
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        #scrolledtext2.insert(END, ' lea ')
        if cade1[0]==cade3[0]:
             #listaA2=descomponer(lista[x])
             if if_integer(listaA2[1])==True:
                cadena='_ '+ listaA2[0] +' _ '+ str(variableValor)
                lista[x]=cadena
           


def sume(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
       
        if cade1[0]== cade3[0]:
             
            
             if if_integer(listaA2[2])==True:
                     #scrolledtext2.insert(END, ' sume ')
                     #if acumulador!='': ##############################  tal vez en este se de un error
                   
                     valor=int(listaA2[2])
                     valor2= int(acumulador)
                     resultd=valor2+valor
                     acumulador=str(resultd)
                     #scrolledtext2.insert(END, ' _')
                     #scrolledtext2.insert(END, acumulador)
                     #scrolledtext3.insert(END,acumulador)
                     return acumulador
               
               
           



def reste(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    #scrolledtext2.insert(END, cade1)
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        #scrolledtext2.insert(END, cade3)

       # scrolledtext2.insert(END, '\n')
        if cade1[0]== cade3[0]:
            # scrolledtext2.insert(END, ' reste ')
            
             if if_integer(listaA2[2])==True:
                 #scrolledtext2.insert(END, listaA2[2])
                    # scrolledtext2.insert(END, ' reste ')
               
                     valor=int(listaA2[2])
                     valor2= int(acumulador)
                     resultd=valor2-valor
                     acumulador=str(resultd)
                     #scrolledtext2.insert(END, 'RESTE: \n')
              

                    # scrolledtext2.insert(END,acumulador)
                     return acumulador              
               
               


def multiplicar(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        
        if cade1[0]== cade3[0]:
            # listaA2=descomponer(lista[x])
             if if_integer(listaA2[2])==True:
                 #if acumulador!='': ##############################  tal vez en este se de un error
                     valor=int(listaA2[2])
                     valor2= int(acumulador)
                     resultd=valor2*valor
                     acumulador=str(resultd)
                     #scrolledtext2.insert(END, 'MULTIP: \n')
          
                     #scrolledtext1.insert(END,acumulador)
                     return acumulador                  
               


def dividir(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
       # scrolledtext2.insert(END, ' divi ')
        if cade1[0]== cade3[0]:
             #listaA2=descomponer(lista[x])
             if if_integer(listaA2[2])==True:
                 #if acumulador!='': ##############################  tal vez en este se de un error
                     valor=int(listaA2[2])
                     valor2= int(acumulador)
                     resultd=int(valor2/valor)
                     acumulador=str(resultd)
                    # scrolledtext2.insert(END, '\n')
             

                    # scrolledtext1.insert(END,acumulador)
                     return acumulador
               


def modulo(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        #scrolledtext2.insert(END, ' modulo ')
        if cade1[0]== cade3[0]:
             #listaA2=descomponer(lista[x])
             if if_integer(listaA2[2])==True:
                # if acumulador!='': ##############################  tal vez en este se de un error
                     valor=int(listaA2[2])
                     valor2= int(acumulador)
                     resultd=valor2%valor
                     acumulador=str(resultd)
                    # scrolledtext1.insert(END,acumulador)
                     return acumulador
  

def potencia(acumulador,lista,linea_instrucion,inicio,fin):

   
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
       # scrolledtext2.insert(END, ' potencia ')
        #scrolledtext2.insert(END, listaA2[2])
        if cade1[0]== cade3[0]:
            # listaA2=descomponer(lista[x])
             if if_integer(listaA2[2])==True:
                     #scrolledtext2.insert(END, listaA2[2])
               
                     valor=int(listaA2[2])
                     #scrolledtext2.insert(END, valor)
                     temp2=valor
                     if valor<0:
                         valor=valor*(-1)
                     valor2= int(acumulador)
                     #scrolledtext2.insert(END, valor2)
                     temp=1
                     if valor==0:
                         acumulador='1'
                     else:
                       for y in range(0,valor):

                          temp=temp*valor2
                       if temp2<0:
                           temp2=1/temp
                           acumulador=str(temp2)
                       else:
                           acumulador=str(temp)
                     #scrolledtext1.insert(END,acumulador)
                     return acumulador
   

def concatenar(acumulador,lista,linea_instrucion,inicio,fin):
   
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        if cade1[0]== cade3[0]:
           # if acumulador!='': ##############################  tal vez en este se de un error
                valor=str(listaA2[2])
                valor2= str(acumulador)
                resultd=valor2 + valor
                acumulador=str(resultd)
                #scrolledtext1.insert(END,acumulador)
                return acumulador



def eliminar(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        if cade1[0]== cade3[0]:
            cadena=acumulador.removesuffix(listaA2[2])
           # scrolledtext1.insert(END,cadena)
            return cadena               
                  

### no entiendo lo que tiene que hacer esta funcion 
def extraiga(acumulador,lista,linea_instrucion,inicio,fin):
    
    listaA=list()
    listaA2=list()
    listaAux=list()
    valor=0
    cantidad=len(acumulador)
   # scrolledtext2.insert(END,acumulador)
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cade3=listaA2[1]
        #scrolledtext2.insert(END, cade3)
        if cade1[0]== cade3[0]:
          #  listaA2=descomponer(lista[x])
            valor=listaA2[2]
           
            break
    acumulador
    #scrolledtext2.insert(END,valor)    
    x=0
    while x<int(cantidad):
        if x>=int(valor):
           listaAux.append(acumulador[x])
        x=x+1
    cadena="".join(listaAux)
    #scrolledtext1.insert(END,cadena )
    return cadena




def andlogi(acumulador,lista,linea_instrucion,inicio,fin):
    #scrolledtext1.insert(END, 'segund')
    valor1=0
    valor2=0
    valor3=0
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    cade2=listaA[2]
    cade3=listaA[3]
   
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        
        cade=listaA2[1]
        
       
        if cade1[0]== cade[0]:
          
          
            valor1=listaA2[2]
        if cade2[0]== cade:
            valor2=listaA2[2]
    
    if valor1=='1' and valor2=='1':
       
        valor3=1
    else:
       
        valor3=0
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cadex=listaA2[1]
       
        if cade3[0]==cadex:
           
            cadex=listaA2[1]
            cadena='_ '+ cadex+ ' _ '+ str(valor3)
            
            lista[x]=cadena

  

def orlog(acumulador,lista,linea_instrucion,inicio,fin):
  band=0
  while band!=1:
    valor1=0
    valor2=0
    valor3=0
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    #scrolledtext1.insert(END, 'orlogi4')
    cade1=listaA[1] 
    cade2=listaA[2]
    cade3=listaA[3]
    band=1
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        
        cade=listaA2[1]
        
       
        if cade1[0]== cade[0]:
          
          
            valor1=listaA2[2]
        if cade2[0]== cade:
            valor2=listaA2[2]
    
    if valor1=='0' and valor2=='0':
       
        valor3=0
    else:
        valor3=1
    band=1

    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cadex=listaA2[1]
       
        if cade3[0]==cadex:
           
            cadex=listaA2[1]
            cadena='_ '+ cadex+ ' _ '+ str(valor3)
            
            lista[x]=cadena
    band=1        
    

def norl(acumulador,lista,linea_instrucion,inicio,fin):
    #scrolledtext1.insert(END, 'tercer')
    valor1=0
    valor2=0
    valor3=0
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
    cade2=listaA[2]
    cade3=listaA[3]
   
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        
        cade=listaA2[1]
        
       
        if cade1[0]== cade[0]:
          
          
            valor1=listaA2[2]
        if cade2[0]== cade:
            valor2=listaA2[2]
    
    if valor1=='0' and valor2=='0':
       
        valor3=1
    else:
       
        valor3=0
    for x in range(inicio,fin):
        listaA2=descomponer(lista[x])
        cadex=listaA2[1]
       
        if cade3[0]==cadex:
           
            cadex=listaA2[1]
            cadena='_ '+ cadex+ ' _ '+ str(valor3)
            
            lista[x]=cadena


def muestre(acumulador,lista,linea_instrucion,inicio,fin):
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
   
    if cade1[0].upper=='ACUMULADOR':
        scrolledtext2.insert(END,acumulador)
    else:
       for x in range(inicio,fin):
           listaA2=descomponer(lista[x])
           cade3=listaA2[1]
           #scrolledtext2.insert(END, cade3)
           if cade1[0]== cade3[0]:
                listaA2=descomponer(lista[x])
                scrolledtext2.insert(END,'\n\n')
                scrolledtext2.insert(tk.END,listaA2[2])
           


def imprima(acumulador,lista,linea_instrucion,inicio,fin):

    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion)
    cade1=listaA[1] 
   
    if cade1[0].upper=='ACUMULADOR':
        scrolledtext1.insert(END,acumulador)
    else:
       for x in range(inicio,fin):
           listaA2=descomponer(lista[x])
           cade3=listaA2[1]
           #scrolledtext2.insert(END, cade3)
           if cade1[0]== cade3[0]:
                listaA2=descomponer(lista[x])
                scrolledtext1.insert(END,'\n')
                scrolledtext1.insert(tk.END,listaA2[2])


def vaya(linea_instrucion1,linea_instrucion2):
    listaA=list()
    listaA2=list()
    listaA=descomponer(linea_instrucion1) ### yava x(itere)
    cade1=listaA[1] 
    listaA2=descomponer(linea_instrucion2) ### etiqueta x(itere) valor
    if listaA[1]==listaA2[1]:
        return int(listaA2[2])
        
      


def vayasi(control,acumulador,linea_instrucion1,linea_instrucion2 ,linea_instrucion3):

    listaA=list()
    listaA2=list()
    listaA3=list()
    listaA=descomponer(linea_instrucion1) ### yavasi x(itere) y(fin)
    cade1=listaA[1] 
    listaA2=descomponer(linea_instrucion2) ### etiqueta x(itere) valor
    listaA3=descomponer(linea_instrucion3) ## etiqueta y(fin)  valor
    #scrolledtext1.insert(END, listaA)
    #scrolledtext1.insert(END, listaA2)
   # scrolledtext1.insert(END,listaA3[2])
    #scrolledtext3.insert(END,'aqui')
    variable=int(acumulador)
    if  variable > 0:
       #if listaA[1]==listaA2[1]:
           #scrolledtext1.insert(END,listaA2[2])
           valor=int(listaA2[2])
           #scrolledtext1.insert(END,valor)
           return valor
    elif  variable < 0:
        scrolledtext3.insert(END, listaA3[2])
        valor= int(listaA3[2])
       
        return valor
    else:
        return control+2
  

def tick():
    sleep(0.5)

def sistema():
    vali=valorKernel.get()
    PC.delete(*PC.get_children())
    PC.insert(parent='', index='end',text=' ') 
    MJ.delete(*MJ.get_children())
    MJ.insert(parent='', index='end',text='MODO SYSTEM') 

   # for x in range(int(vali)):
    
       # PC.delete(*PC.get_children())
       # PC.insert(parent='', index='end',text='**CH-SO_V21**') 
       
def empty_textbox():
    PC.delete(*PC.get_children())
    PC.insert(parent='', index='end',text='MODO USER')
    
def elim():
     Acumulador.delete(*Acumulador.get_children())

                                                                                                                                                                                                          
def ejecutar():
    PC.delete(*PC.get_children())
    sistema()
    control=0
    c1=-2
    c2=-1
    inicio=0
    fin=0 
    
  #  scrolledtext2.insert(END, c1)
   # scrolledtext2.insert(END,c2)
    MJ.delete(*MJ.get_children())
    MJ.insert(parent='', index='end',text='MODO USER')
    global acumulador
   
    control=0
    for x in range(0,cantidadProgramas):
       # scrolledtext1.insert(END, cantidadProgramas)
        c1=c1+2
        c2=c2+2
        cont3e=0
        cambio=0
        for inic in range(0,c1+1):
         #   scrolledtext2.insert(END,' ')

           # scrolledtext2.insert(END,inic)
            inicio=inicio+lista_dimensiones_Programas[cont3e]
            #scrolledtext1.insert(END, lista_dimensiones_Programas[cont3e])
            cont3e=cont3e+1

        scrolledtext1.insert(END, '\n')
        contd=0
        for fini in range(0,c2+1):
          # scrolledtext1.insert(END,fini)
           fin=fin+lista_dimensiones_Programas[contd]
           #scrolledtext1.insert(END, lista_dimensiones_Programas[contd])
           contd=contd+1


        band=0
        #scrolledtext1.insert(END, fin)
        vali2=valorVelocidad.get()
        
        while band!=1:

           

            
            if "cargue" in listaMemoria[control].lower():
               # scrolledtext1.insert(END, inicio)
                ## mirar si los patrametros son por ferencia o por valor en python ???
               
                acumulador=cargue(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
              
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador) ################################################# Cambiar en las demas
                band=0
              
                scrolledtext2.insert(END,acumulador)
       
            elif "almacene" in listaMemoria[control].lower():
                almacene(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                cargar()
                band=0
       
            elif "lea" in listaMemoria[control].lower():
                lea(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                band=0
      
            elif "sume" in listaMemoria[control].lower():
                acumulador=sume(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext2.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
            elif "reste" in listaMemoria[control].lower():
                acumulador=reste(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
              
               # scrolledtext2.insert(END,acumulador)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
               # scrolledtext1.insert(END, acumulador)
                #scrolledtext2.insert(END,acumulador)
                band=0

      
            elif "multiplique" in listaMemoria[control].lower():
                acumulador=multiplicar(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
               
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext1.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
      
            elif "divida" in listaMemoria[control].lower():
                acumulador=dividir(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
               
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext1.insert(END, acumulador)
                band=0
               # scrolledtext2.insert(END,listaMemoria[control])
                #scrolledtext2.insert(END,acumulador)
                   
            elif "potencia" in listaMemoria[control].lower():
                acumulador=potencia(acumulador,listaMemoria,listaMemoria[control],inicio,fin+1)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext1.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
       
            elif "modulo" in listaMemoria[control].lower():
                acumulador=modulo(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext1.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
       
            elif "concatene" in listaMemoria[control].lower():
                acumulador=concatenar(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
                #scrolledtext1.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
        
            elif "elimine" in listaMemoria[control].lower():
                acumulador=eliminar(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
               # Acumulador.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
      
            elif "extraiga" in listaMemoria[control].lower():
                acumulador=extraiga(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                Acumulador.delete(*Acumulador.get_children())
                Acumulador.insert(parent='', index='end',text=acumulador)
               # Acumulador.insert(END, acumulador)
                band=0
                #scrolledtext2.insert(END,acumulador)
        
            elif "Y" in listaMemoria[control]:
                cadena= listaMemoria[control]
                if cadena[0].upper()=='Y':
                    andlogi(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                cargar()

        
            elif "O" in listaMemoria[control]:
                cadena= listaMemoria[control]
                if cadena[0].upper()=='O':
                    acumulador=orlog(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                cargar()

                band=0
                #scrolledtext2.insert(END,acumulador)
        
            elif "NO" in listaMemoria[control]:
                cadena= listaMemoria[control]
                if cadena[0].upper()=='N' and cadena[1].upper()=='O':
                   norl(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                cargar()
                #Acumulador.insert(parent='', index='end',text=acumulador)
               # Acumulador.insert(END, acumulador)
                band=0
          
            elif "muestre" in listaMemoria[control].lower() :
                #scrolledtext2.insert(END,listaMemoria[control])
                muestre(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
                band=0
        
            elif "imprima"  in listaMemoria[control].lower():
                imprima(acumulador,listaMemoria,listaMemoria[control],inicio,fin)
             
                band=0
       
            elif "retorne" in listaMemoria[control]:
                control=fin
                fin=0
                inicio=0
                cambio=cambio+1
                #scrolledtext1.insert(END, control)
                band=1
                break ####################################### salida
        

            
            if "vayasi" in listaMemoria[control]:
               # scrolledtext3.insert(END, 'yufu')
                saltar=vayasi(control,acumulador,listaMemoria[control],listaMemoria[control+1],listaMemoria[control+2])
               
                control= saltar -1
            else:
                control=control+1   
                #control=0
                #control=saltar
               # band=0
            
           
       ##### cuadro de impresion de 
label_coment1=Label(ventana1, text='impresion',font=('Arial',14))
label_coment1.grid(column=0,row=0)

scrolledtext1=st.ScrolledText(ventana1, width=20,height=10)
#scrolledtext1.grid(column=0,row=1,padx=10,pady=10)

scrolledtext1.place(x=540,y=350)
label_coment1.place(x=570,y=320)

        #  Cuadro de Pantalla 
label_coment2=Label(ventana1, text='Pantalla',font=('Arial',14))
label_coment2.grid(column=0,row=2)
scrolledtext2=st.ScrolledText(ventana1, width=30,height=10)
scrolledtext2.grid(column=0,row=3,padx=0,pady=0)
scrolledtext2.place(x=500,y=150)
label_coment2.place(x=570,y=100)
#imagenP=PhotoImage( height=30,width=30, file="descarga_1_.gif")

       # cuadro de cargue
     
scrolledtext3=st.ScrolledText(ventana1, width=30,height=30)
#scrolledtext3.grid(column=0,row=3,padx=0,pady=0)
scrolledtext3.place(x=10,y=210)

filename = Entry(ventana1)
filename.place(x=10,y=185)

    # Cuadro de memoria

memoria=ttk.Treeview(ventana1, height=35,columns=('#1','#2','#3','#4'))
#memoria.grid(row=4, column=0, columnspan=4)
memoria.place(x=770,y=50)

memoria.column('#2',width=70)
memoria.heading('#2',text="variable", anchor=CENTER)
memoria.column('#3',width=35)
memoria.heading('#3',text="Tipo", anchor=CENTER)
memoria.column('#4',width=40)
memoria.heading('#4',text="valor", anchor=CENTER)

memoria.column('#0',width=50)
memoria.column('#1',width=80)
memoria.heading('#0',text="Direccion", anchor=CENTER)
memoria.heading('#1',text=" Instrucion")
label_coment4=Label(ventana1,text='Memoria',font=('Arial',14))
label_coment4.place(x=900,y=10)

       #Cuadro de  variable
variable=ttk.Treeview(ventana1, height=8,columns=('#1'))
variable.place(x=300,y=210)
variable.column('#0',width=70)
variable.column('#1',width=90)
variable.heading('#0',text="Direcc")
variable.heading('#1',text="variable")

       # cuadro de etiquetas
       
etiqueta=ttk.Treeview(ventana1, height=8,columns=('#1'))
etiqueta.place(x=300,y=400)
etiqueta.column('#0',width=70)
etiqueta.column('#1',width=90)
etiqueta.heading('#0',text="Direcc")
etiqueta.heading('#1',text="etiqueta")


Acumulador=ttk.Treeview(ventana1, height=1)
Acumulador.place(x=160,y=100)
Acumulador.column('#0',width=100)
Acumulador.heading('#0',text="ACUMULADOR")

PC=ttk.Treeview(ventana1, height=1)
PC.place(x=263,y=100)
PC .column('#0',width=190)
PC.heading('#0',text="Pc")

MJ=ttk.Treeview(ventana1, height=1)
MJ.place(x=540,y=550)
MJ .column('#0',width=190)
MJ.heading('#0',text="Modo Ejecu")



label_comentKernel=Label(ventana1,text='Memoria',).place(x=10,y=100)
kernel=Spinbox(ventana1,from_=4, to=100, textvariable=valorKernel, width=8).place(x=70,y=130)
label_comentMemoria=Label(ventana1,text='Kernel').place(x=10,y=130)
memoriac=Spinbox(ventana1,from_=59,to=100,textvariable= valorMemoria, width=8).place(x=70,y=100)



label_comentKernel=Label(ventana1,text='velocidad',).place(x=10,y=70)
velocida=Scale(ventana1,from_=1, to=100,variable=valorVelocidad, width=14, orient=HORIZONTAL).place(x=70,y=50)

#############################################
#       BOTONES DE ACCION

 # Abrir un archivo y mostrar
#imagenA=PhotoImage( height=30,width=30, file="descarga_1_.gif")

botonAbrir=Button(ventana1,text="Abrir", command=AbrirCh).place(x=70,y=10)

# Cargar el contenido a  la memoria, aun no se ha hecho la funcion
botonCargar=Button(ventana1,text="Cargar",command=cargar)
botonCargar.place(x=170,y=10)

# ejecutar el programa
botonEjecutar=Button(ventana1,text="Ejecutar",command=ejecutar)
botonEjecutar.place(x=270,y=10)

# ejecutar instrucion por instrucion 
botonPaso=Button(ventana1, text="Paso A Paso")
botonPaso.place(x=370,y=10)

## limpia toda la informacion cargada
botonLimpiar=Button(ventana1, height=2, text="Reiniciar",command=Limpiar)
botonLimpiar.place(x=470,y=3)

# crear archivos con la informacion ingresada en el ScrolledText3
crear=Button(text='Crear',command=save).place(x=130,y=185)


ventana1.mainloop()
  

      





 