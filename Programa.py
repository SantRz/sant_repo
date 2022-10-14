from tkinter import *
from tkinter import messagebox

def starting():

    archivo_texto = open("boot.log","r") #Abrimos el archivo que queremos leer
    archivo_starting = open("starting.txt", "w")
    archivo_started = open("started.txt", "w")
    archivo_failed = open("failed.txt", "w")
    archivo_reached = open("reached.txt", "w")
    archivo_listening = open("listening.txt", "w")
    archivo_mounted = open("mounted.txt", "w")
    archivo_fdevice = open("found_device.txt", "w")
    archivo_actswap = open("activated_swap.txt", "w")
    archivo_actingswap = open("activating_swap.txt", "w")
    archivo_mounting = open("mounting.txt", "w")
    archivo_createdslice = open("created_slice.txt", "w")
    archivo_stopped = open("stopped.txt", "w")

    lineas = archivo_texto.readlines()

    archivo_texto.close()

    conjunto_textos = set()
    conjunto_textos2 = set()
    conjunto_textos3 = set()
    conjunto_textos4 = set()
    conjunto_textos5 = set()
    conjunto_textos6 = set()
    conjunto_textos7 = set()
    conjunto_textos8 = set()
    conjunto_textos9 = set()
    conjunto_textos10 = set()
    conjunto_textos11 = set()
    conjunto_textos12 = set()

    for texto in lineas:
        if "Started" in texto: #Si se encuentra "Started" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable1 = texto.split("Started")[1]
            conjunto_textos.add(variable1[10:-6])

        if "Failed to start" in texto: #Si se encuentra "Failed" en boot.log, en variable2 se almacena lo que haya un lugar despues de ese texto
            variable2 = texto.split("Failed to start")[1]
            conjunto_textos2.add(variable2[10:-6])

        if "Reached target" in texto: #Si se encuentra "Reached" en boot.log, en variable3 se almacena lo que haya un lugar despues de ese texto
            variable3 = texto.split("Reached target")[1]
            conjunto_textos3.add(variable3[10:-6])

        if "Listening" in texto: #Si se encuentra "Listening" en boot.log, en variable3 se almacena lo que haya un lugar despues de ese texto
            variable4 = texto.split("Listening")[1]
            conjunto_textos4.add(variable4[13:-6])

        if "Mounted" in texto: #Si se encuentra "Mounted" en boot.log, en variable3 se almacena lo que haya un lugar despues de ese texto
            variable5 = texto.split("Mounted")[1]
            conjunto_textos5.add(variable5[10:-6])

        if "Found device" in texto: #Si se encuentra "Found device" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable6 = texto.split("Found device")[1]
            conjunto_textos6.add(variable6[10:-6])

        if "Starting" in texto: #Si se encuentra "Starting" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable7 = texto.split("Starting")[1]
            conjunto_textos7.add(variable7[10:-8])

        if "Activating swap" in texto: #Si se encuentra "Activating swap" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable8 = texto.split("Activating swap")[1]
            conjunto_textos8.add(variable8[10:-8])
        
        if "Activated swap" in texto: #Si se encuentra "Activated swap" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable9 = texto.split("Activated swap")[1]
            conjunto_textos9.add(variable9[10:-8])
        
        if "Mounting" in texto: #Si se encuentra "Mounting" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable10 = texto.split("Mounting")[1]
            conjunto_textos10.add(variable10[10:-8])

        if "Created slice" in texto: #Si se encuentra "Creating slice" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable11 = texto.split("Created slice")[1]
            conjunto_textos11.add(variable11[10:-6])
        
        if "Stopped" in texto: #Si se encuentra "Stopped" en boot.log, en variable1 se almacena lo que haya un lugar despues de ese texto
            variable12 = texto.split("Stopped")[1]
            conjunto_textos12.add(variable12[10:-6])

    for i_started in conjunto_textos:
        archivo_started.write("STARTED: " + i_started + "\n")

    for i_failed in conjunto_textos2:
        archivo_failed.write("FAILED TO START: " + i_failed + "\n")

    for i_reached in conjunto_textos3:
        archivo_reached.write("REACHED TARGET: " + i_reached + "\n")

    for i_listening in conjunto_textos4:
        archivo_listening.write("LISTENING: " + i_listening + "\n")
    
    for i_mounted in conjunto_textos5:
        archivo_mounted.write("MOUNTED: " + i_mounted + "\n")

    for i_fdevice in conjunto_textos6:
        archivo_fdevice.write("FOUND DEVICE: " + i_fdevice + "\n")

    for i_starting in conjunto_textos7:
        archivo_starting.write("STARTING: " + i_starting + "\n")

    for i_actingswap in conjunto_textos8:
        archivo_actingswap.write("ACTIVATING SWAP: " + i_actingswap + "\n")

    for i_actswap in conjunto_textos9:
        archivo_actswap.write("ACTIVATED SWAP: " + i_actswap + "\n")

    for i_mounting in conjunto_textos10:
        archivo_mounting.write("MOUNTING: " + i_mounting + "\n")
    
    for i_cslice in conjunto_textos11:
        archivo_createdslice.write("CREATED SLICE: " + i_cslice + "\n")
    
    for i_stopped in conjunto_textos12:
        archivo_stopped.write("STOPPED: " + i_stopped + "\n")

    archivo_started.close()
    archivo_failed.close()
    archivo_reached.close()
    archivo_listening.close()
    archivo_mounted.close()
    archivo_fdevice.close()
    archivo_starting.close()
    archivo_actswap.close()
    archivo_actingswap.close()
    archivo_mounting.close()
    archivo_createdslice.close()
    archivo_stopped.close()

    messagebox.showinfo('Mensaje', 'Archivos generados con éxito.')
#---------------------------------------

def mails():
    import re
    archivo = open("log.txt","r") 
    lineas = archivo.readlines()
    mails = []
    mailsRepetidos = []

    for texto in lineas:
        mail = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', texto)
        if mail:
            
            repetido = False
            if mail in mailsRepetidos:
                repetido = True

            if repetido == False:
                mailsRepetidos.append(mail)
                mails.append(mail)
            

    print(mails)

    archivo_texto = open("mails.txt", "w")

    for lista in mails:
        for mail in lista:
            archivo_texto.write(mail + "\n")
        
    archivo_texto.close()
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------------------

def commits():
    str = open("log.txt","r").read()
    lista=str.split("commit")
    print(lista[:2])
    print(len(lista)-1)

    archivo_texto = open("commits.txt", "w")

    for commit in lista:
        archivo_texto.write(commit + "\n")
        
    archivo_texto.close()
#---------------------------

def comentarios():
    import re

    def esComentario(linea):
        if linea.find("commit") and linea.find("Author") and linea.find("Date"):
                if re.search('[a-zA-Z]', texto):
                    return True  

        return False

    archivo = open("log.txt","r") 
    lineas = archivo.readlines()
    Comentarios = []

    for texto in lineas:
            temp = []
            if esComentario(texto):
                temp.append(texto)
                indice = lineas.index(texto)
                while (texto != lineas[-1] and esComentario(lineas[indice+1])):
                    if lineas[indice+1] != '\n':
                        temp.append(lineas[indice+1])
                    indice += 1

            if len(temp) != 0:
                Comentarios.append(temp)

    print(Comentarios)
    print(len(Comentarios))

    archivo_texto = open("comentarios.txt", "w")

    for comentario in Comentarios:
        if isinstance(comentario, list):
            for subelemento in comentario:
                archivo_texto.write(subelemento + "\n")
        else:
            archivo_texto.write(comentario + "\n")
        
    archivo_texto.close()
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#----------------------------------------

def fechas():
    from datetime import datetime
    from collections import Counter

    archivo = open("log.txt","r") 
    lineas = archivo.readlines()

    fechasCommits = []

    for linea in lineas:
        if "Date:" in linea:
            stringFecha = linea[8:-1]
            fecha = datetime.strptime(stringFecha, "%a %b %d %X %Y %z")
            fechasCommits.append(fecha.weekday())
            
    cnt = Counter(fechasCommits)
    print(cnt.most_common())
    messagebox.showinfo('Mensaje', 'Datos generados en la consola.')
#----------------------

window = Tk()  
window.geometry('640x480')  

window.title("Procesamiento de logs")

botonautores = Button(window,
	text = 'Crear logs',
    bg = 'LightBlue',
	command = starting)  
botonautores.pack()  

window.mainloop()

