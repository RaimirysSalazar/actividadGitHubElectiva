Asignacion #1 Valor 20%
La empresa yabadabadu necesita con urgencia pagar la nomina de sus empleados tal como acostumbra
cada viernes pero justo hoy la plataforma tecnológica se ha visto comprometida por un fallo en uno de
sus servidores por lo que no cuentan con el sistema principal que usan para tal fin. por esta razón se
desea leer un archivo plano que posee una lista de los empleados junto al sueldo base de cada uno,
usted como soporte de sistemas no se encuentra en la empresa pero se le ha dado la tarea de desarrollar
un script en python que pueda correr en el servidor via ssh para lograr el objetivo se necesita:
Desarrollar un script que permita realizar lo siguiente:
1) Reciba dos parámetros por terminal 
ejemplo:
script_pago_nomina.py [bono1] [bono2]
[Bono 1] Bono General = 5%
[Bono 2] Bono Eficiencia = 15% (Empleados que tengan mas de 5 horas extras en la semana)
2) Leer el archivo llamado nomina.txt
3) Realizar las operaciones pertinentes para cada empleado
4) Guardar el archivo con el monto a pagar en otro archivo llamado pago_nomina_12sep2021.py
5) Aprovechando la coyuntura se pide cambiar la fecha de ingreso al formato 'YYYY-MM-DD' 
Ejemplo 23/04/1990 cambiar a 1990-04-23
Archivo nomina.txt
cedula fecha_ingreso empleado sueldo_base horas_extra 
1334521 23/12/1999 Juan Castro 60$ 5
12333444 12/12/2012 Carolina Buitriago 90$ 3
13334434 12/12/2012 Julio Castillo 100$ 15
1334523 23/12/1999 Juana archila 160$ 5
12333444 12/12/2012 Daniel Burgos 90$ 3
13334434 12/12/2012 Cesar Guzman 100$ 15
13345266 23/12/1999 Darielsys Maduro 60$ 5
12333474 12/12/2012 Nestor Tovar 90$ 3
13334484 12/12/2012 Carolys Suniaga 100$ 15
13345213 23/12/1999 Hector Gomez 60$ 5
12333444 12/12/2012 Carolina Vargas 90$ 3
13334111 12/12/2012 Julio Mujica 100$ 15
13334456 12/12/2012 Jonh Chancellor 100$ 15
Puntos a evaluar:
1) Manejo de Git, la asignación debe estar en un repositorio publico en github (5pts)
2) Cada alumno debe tener su cuenta y haber realizado mas de 5 commit en su repositorio (4pts)
3) La entrega final sera el día martes 21 de Septiembre (Sin Prorroga)
4) Funcionalidad del Script (8pts)
5) pep8 y documentación del mismo. (3pts
