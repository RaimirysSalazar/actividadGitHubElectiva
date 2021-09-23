from datetime import datetime
import sys
print(sys.argv)

global bono1
global bono2
global auxBono1
global auxBono2
if (len(sys.argv) == 3):
    bono1 = int(sys.argv[1])
    bono2 = int(sys.argv[2])
    auxBono1=bono1
    auxBono2=bono2
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo:script_pago_nomina.py 5 15')

lista=[]
datos3 = []
monto = []
horasExtras = []
fecha =[]
with open("nomina.txt") as fname:
  for lineas in fname:
      datos3.append(lineas.split())

for index in range(13):
    monto.append(int(datos3[index][4]))
    horasExtras.append(int(datos3[index][5]))
    fecha.append(datos3[index][1])

for index1 in range(13):
    if horasExtras[index1] > 5 :
       monto[index1] =monto[index1] + (monto[index1] * (5 /100) )
    else:
       monto[index1] =monto[index1] + (monto[index1] * (15 /100) )


for i in range(13):
  una_fecha = fecha[i]
  fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
  fecha1= fecha_dt.date()
  lista=fecha1

archi1=open("pago_nomina_12sep2021.txt","w")
for i in range(13):
  una_fecha = fecha[i]
  fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
  fecha1= fecha_dt.date()
  lista=fecha1
  archi1.write("Empleado -> "+str(i+1) +" "+"salario total => "+ str(monto[i]) + "$"+"  "+str(lista)+"\n" )
archi1.close()
