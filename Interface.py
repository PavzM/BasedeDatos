"""

Practica de Bases de Datos. NRC:31505

    Reyes Murrieta Guadalupe     201733820
    Perez Armas Bardo Absalon    201708982
    Espinoza Bigurra Asael       201702598
    Medel Perez Pavel Jesus      201726903
    Tomas Chapital Cesar         201739585

"""
import wx
import wx.grid

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
    """/home/pavz/Documents/GitHub/BaseDeDAtos"""
    """Esta función es para cargar la tabla desde un archivo"""
    archivo = open('/home/pavz/Documents/GitHub/BaseDeDAtos/basededatos.txt','r',)
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
def imprime(sel, index):
    for el in sel:
        if el.upper() == "EMPLOYEE_ID":
            for i in range(0,6-len(EMPLOYEE_ID[index])):
                print(f" ", end='')
            print(f"{EMPLOYEE_ID[index]} | ", end='')
        elif el.upper() == "FIRST_NAME":
            for i in range(0,20-len(FIRST_NAME[index])):
                print(f" ", end='')
            print(f"{FIRST_NAME[index]} | ", end='')
        elif el.upper() == "LAST_NAME":
            for i in range(0,25-len(LAST_NAME[index])):
                print(f" ", end='')
            print(f"{LAST_NAME[index]} | ", end='')
        elif el.upper() == "EMAIL":
            for i in range(0,25-len(EMAIL[index])):
                print(f" ", end='')
            print(f"{EMAIL[index]} | ", end='')
        elif el.upper() == "PHONE_NUMBER":
            for i in range(0,20-len(PHONE_NUMBER[index])):
                print(f" ", end='')
            print(f"{PHONE_NUMBER[index]} | ", end='')
        elif el.upper() == "HIRE_DATE":
            for i in range(0,8-len(HIRE_DATE[index])):
                print(f" ", end='')
            print(f"{HIRE_DATE[index]} | ", end='')
        elif el.upper() == "JOB_ID":
            for i in range(0,10-len(JOB_ID[index])):
                print(f" ", end='')
            print(f"{JOB_ID[index]} | ", end='')
        elif el.upper() == "SALARY":
            for i in range(0,8-len(SALARY[index])):
                print(f" ", end='')
            print(f"{SALARY[index]} | ", end='')
        elif el.upper() == "COMMISSION_PCT":
            for i in range(0,4-len(COMMISSION_PCT[index])):
                print(f" ", end='')
            print(f"{COMMISSION_PCT[index]} | ", end='')
        elif el.upper() == "MANAGER_ID":
            for i in range(0,6-len(MANAGER_ID[index])):
                print(f" ", end='')
            print(f"{MANAGER_ID[index]} | ", end='')
        elif el.upper() == "DEPARTMENT_ID":
            for i in range(0,6-len(DEPARTMENT_ID[index])):
                print(f" ", end='')
            print(f"{DEPARTMENT_ID[index]} | ", end='')
    print()

#------------------------------------------------------------------------------------------
def select():
    listas = input(">> ").split()
    sel = listas[1].split(',')
    return sel

def toda(index):
    print ("{0:6s} | {1:20s} | {2:25s} | {3:25s} | {4:20s} | {5:8s} | {6:10s} | {7:8s} | {8:4s} | {9:6s} | {10:6s} |".format(EMPLOYEE_ID[index],FIRST_NAME[index],LAST_NAME[index],EMAIL[index],PHONE_NUMBER[index],HIRE_DATE[index],JOB_ID[index],SALARY[index],COMMISSION_PCT[index],MANAGER_ID[index],DEPARTMENT_ID[index]))

def where(campos):#Forma de introducir: where department_id=9;
    si = input(">> ").replace(";","").split()
    si = si[1].split('=')
    for index in range(0,len(EMPLOYEE_ID)):
        if si[0].upper() == "EMPLOYEE_ID":
            if EMPLOYEE_ID[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "FIRST_NAME":
            if FIRST_NAME[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "LAST_NAME":
            if LAST_NAME[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "EMAIL":
            if EMAIL[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "PHONE_NUMBER":
            if PHONE_NUMBER[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "HIRE_DATE":
            if HIRE_DATE[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "JOB_ID":
            if JOB_ID[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "SALARY":
            if SALARY[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "COMMISSION_PCT":
            if COMMISSION_PCT[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "MANAGER_ID":
            if MANAGER_ID[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                    imprime(campos,index)
        elif si[0].upper() == "DEPARTMENT_ID":
            if DEPARTMENT_ID[index] == si[1]:
                if campos[0]=="*":
                    toda(index)
                else:
                   imprime(campos,index)


def diccionario():
#yo
    pass

#----------------------TABLA--------------------------------------------#
#Pag 159: http://index-of.co.uk/Tutorials/wxPython%20in%20Action.pdf


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(106, 11)
    #------------------------------------------------------Columnas
        self.SetColLabelValue(0, "EMPLOYEE_ID")
        self.SetColLabelValue(1, "FIRST_NAME")
        self.SetColLabelValue(2, "LAST_NAME")
        self.SetColLabelValue(3, "EMAIL")
        self.SetColLabelValue(4, "PHONE_NUMBER")
        self.SetColLabelValue(5, "HIRE_DATE")
        self.SetColLabelValue(6, "JOB_ID")
        self.SetColLabelValue(7, "SALARY")
        self.SetColLabelValue(8, "COMMISSION_PCT")
        self.SetColLabelValue(9, "MANAGER_ID")
        self.SetColLabelValue(10, "DEPARTMENT_ID")
    #-------------------------------------------------------------
        for i in range(0,len(EMPLOYEE_ID)):
            self.SetCellValue(i, 0, EMPLOYEE_ID[i])
            self.SetCellValue(i, 1, FIRST_NAME[i])
            self.SetCellValue(i, 2, LAST_NAME[i])
            self.SetCellValue(i, 3, EMAIL[i])
            self.SetCellValue(i, 4, PHONE_NUMBER[i])
            self.SetCellValue(i, 5, HIRE_DATE[i])
            self.SetCellValue(i, 6, JOB_ID[i])
            self.SetCellValue(i, 7, SALARY[i])
            self.SetCellValue(i, 8, COMMISSION_PCT[i])
            self.SetCellValue(i, 9, MANAGER_ID[i])
            self.SetCellValue(i, 10, DEPARTMENT_ID[i])

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()


class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)
        grid.AutoSize()
        grid.EnableEditing(False)
        grid.DisableDragGridSize()

if __name__ == '__main__':
    AbrirArchivo()
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()



#inst1 = input(">> ").split()
#sel = inst1[1].split(',')
#inst3 = input(">> ").split()
num = select()
where(num)

#---------------------------------------------------------------------------------
