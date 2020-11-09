"""

Practica de Bases de Datos. NRC:31505

    Reyes Murrieta Guadalupe     201733820
    Perez Armas Bardo Absalon    201708982
    Espinoza Bigurra Asael       201702598
    Medel Perez Pavel Jesus      201726903
    Tomas Chapital Cesar         201739585

"""

EMPLOYEE_ID = []
FIRST_NAME = []
LAST_NAME = []
EMAIL = []
PHONE_NUMBER = []
HIRE_DATE = []
JOB_ID = []
SALARY = []
COMMISSION_PCT = []
MANAGER_ID = []
DEPARTMENT_ID = []

def AbrirArchivo():
    """Esta función es para cargar la tabla desde un archivo"""
    archivo = open('c:/Users/Lenovo/Desktop/Python/basededatos.txt','r',)
    formato = archivo.readline().rstrip()
    formato = formato.split(',')
    lin = []
    tam = []
    ind = 0
    for part in formato:
        if part.isnumeric():
            lin.append(int(part))
            if ind > 0 and not (ind%2)==0:
                tam.append(lin[ind] - (lin[ind-1]-1))
            ind = ind + 1
    #print("{0:11s} | {1:20s} | {2:25s} | {3:25s} | {4:20s} | {5:8s} | {6:10s} | {7:8s} | {8:4s} | {9:6s} | {10:6s} |".format("EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","PHONE_NUMBER","HIRE_DATE","JOB_ID","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"))
    laCompleta = []
    while True:
        linea = archivo.readline().rstrip()#Debemos leer por número de caracteres
        if not linea: #Fin del Archivo
            break
        i=0
        for ind,campo in enumerate(tam):
            laCompleta.append(linea[i:(i+tam[ind])])
            i=i+tam[ind]
        EMPLOYEE_ID.append(laCompleta[0].replace(' ', ''))
        FIRST_NAME.append(laCompleta[1].replace(' ', ''))
        LAST_NAME.append(laCompleta[2].replace(' ', ''))
        EMAIL.append(laCompleta[3].replace(' ', ''))
        PHONE_NUMBER.append(laCompleta[4].replace(' ', ''))
        HIRE_DATE.append(laCompleta[5].replace(' ', ''))
        JOB_ID.append(laCompleta[6].replace(' ', ''))
        SALARY.append(laCompleta[7].replace(' ', ''))
        COMMISSION_PCT.append(laCompleta[8].replace(' ', ''))
        MANAGER_ID.append(laCompleta[9].replace(' ', ''))
        DEPARTMENT_ID.append(laCompleta[10].replace(' ', ''))
        #print ("{0:1s} | {1:1s} | {2:1s} | {3:1s} | {4:1s} | {5:9s} | {6:1s} | {7:1s} | {8:14s} | {9:10s} | {10:1s} |".format(laCompleta[0],laCompleta[1],laCompleta[2],laCompleta[3],laCompleta[4],laCompleta[5],laCompleta[6],laCompleta[7],laCompleta[8],laCompleta[9],laCompleta[10]))
        laCompleta.clear()

    archivo.close()
#------------------------------------------------------------------------------------------
def select():#forma de introducir elementos:>>select employee_id,first_name
    listas = input(">> ").split()
    sel = listas[1].split(',')
    if listas[1] == "*":
        pass
    else:
        for index in range(0,len(EMPLOYEE_ID)):
            for el in sel:
                if el.upper() == "EMPLOYEE_ID":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"        {EMPLOYEE_ID[index]} | ", end='')
                elif el.upper() == "FIRST_NAME":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{FIRST_NAME[index]} | ", end='')
                elif el.upper() == "LAST_NAME":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{LAST_NAME[index]} | ", end='')
                elif el.upper() == "EMAIL":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{EMAIL[index]} | ", end='')
                elif el.upper() == "PHONE_NUMBER":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{PHONE_NUMBER[index]} | ", end='')
                elif el.upper() == "HIRE_DATE":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{HIRE_DATE[index]} | ", end='')
                elif el.upper() == "JOB_ID":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{JOB_ID[index]} | ", end='')
                elif el.upper() == "SALARY":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{SALARY[index]} | ", end='')
                elif el.upper() == "COMMISSION_PCT":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{COMMISSION_PCT[index]} | ", end='')
                elif el.upper() == "MANAGER_ID":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{MANAGER_ID[index]} | ", end='')
                elif el.upper() == "DEPARTMENT_ID":
                    if index==0:
                        print("EMPLOYEE_ID | ")
                    print(f"{DEPARTMENT_ID[index]} | ", end='')
            print()

def where():
    pass

def diccionario():
#yo
    pass



AbrirArchivo()
#inst1 = input(">> ").split()
#sel = inst1[1].split(',')
#inst3 = input(">> ").split()
select()
where()

#---------------------------------------------------------------------------------
