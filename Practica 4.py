import datetime
import datetime
from time import ctime
import ntplib
import os
import tkinter as tk
from tkinter import *


if not os.geteuid():
    print()
else:
    exit("No eres root")
servidor_de_tiempo= "time-a-g.nist.gov","time-b-g.nist.gov","time-c-g.nist.gov","time-d-g.nist.gov","time-e-g.nist.gov"
for i in servidor_de_tiempo:
    try:
        t1=datetime.datetime.now()
        cliente_ntp = ntplib.NTPClient()
        respuesta = cliente_ntp.request(i)
        print("Se usara %s para obtener la fecha y hora\n" %i)
        break
    except:
        print(".")
        continue
else:
    exit("No hay servidores disponibles")
print ("hora de inicio de la petición = %s" %t1.time())
t2=datetime.datetime.now()
print ("hora de llegada de la petición = %s " %t2.time())
hs= datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print ("Fecha/hora que se recibió del servidor de tiempo =%s " %hs)
dt=(t2-t1)/2
print ("tiempo de retraso del paquete = %s " %dt)
tf=hs+dt
print ("hora/fecha que se va a cambiar en la computadora local= %s " %tf)
print("La fecha se cambio a:")
os.system('date --set "%s"' %tf)
os.system('hwclock --set --date="%s"' %tf)