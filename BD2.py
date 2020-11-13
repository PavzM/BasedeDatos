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

#Listas Para Mostrar el Resultado
EMPLOYEE_ID_R = []
FIRST_NAME_R = []
LAST_NAME_R = []
EMAIL_R = []
PHONE_NUMBER_R = []
HIRE_DATE_R = []
JOB_ID_R = []
SALARY_R = []
COMMISSION_PCT_R = []
MANAGER_ID_R = []
DEPARTMENT_ID_R = []
filas = [0]#Renglones
columnas  = [0]
sel = []

###Diccionario
FIELD = []
INI_P = []
TAM_FIELD = []
LENGHT = []
TYPE = []
I_VAL = []
L_VAL = []

def AbrirArchivo():
    """Esta función es para cargar la tabla desde un archivo"""
    archivo = open('c:/Users/Lenovo/Desktop/Python/basededatos.txt','r')
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
def Diccionario():
    archivo = open('c:/Users/Lenovo/Desktop/Python/basededatos.txt','r')
    cadena = archivo.readline().rstrip()
    cadena= cadena.split(',')#aqui estan las palabras de los campos con las posiciones
    lin=[]
    ind=0
    src=0
    i=0
    j=0
    for imp in cadena:
        if imp.isnumeric():
            lin.append(int(imp))
            if ind > 0 and not (ind%2)==0:
                TAM_FIELD.append(str(lin[ind] - (lin[ind-1]-1)))
            ind = ind + 1
        else:
            FIELD.append(imp)
    for port in cadena:
        if port.isnumeric():
            if  (src%2)==0:
                num=int(port)-1
                INI_P.append(str(num))
                src=src+1
            else:
                src=src+1
    """for cas in FIELD:
        print(FIELD[i],end="            ")
        print(INI_P[i],end="             ")
        print(TAM_FIELD[i],end="             ")
        i=i+1
        print("")"""
    #esta parte requiere de los datos pasados a tabla
    # EN DISCUCION DE MOMENTO ESTATICO
    archivo.close()
#------------------------------------------------------------------------------
def imprime(SEL, index):
    for el in SEL:
        if el.upper() == "EMPLOYEE_ID":
            EMPLOYEE_ID_R.append(EMPLOYEE_ID[index])
            filas[0]=len(EMPLOYEE_ID_R)
        elif el.upper() == "FIRST_NAME":
            FIRST_NAME_R.append(FIRST_NAME[index])
            filas[0]=len(FIRST_NAME_R)
        elif el.upper() == "LAST_NAME":
            LAST_NAME_R.append(LAST_NAME[index])
            filas[0]=len(LAST_NAME_R)
        elif el.upper() == "EMAIL":
            EMAIL_R.append(EMAIL[index])
            filas[0]=len(EMAIL_R)
        elif el.upper() == "PHONE_NUMBER":
            PHONE_NUMBER_R.append(PHONE_NUMBER[index])
            filas[0]=len(PHONE_NUMBER_R)
        elif el.upper() == "HIRE_DATE":
            HIRE_DATE_R.append(HIRE_DATE[index])
            filas[0]=len(HIRE_DATE_R)
        elif el.upper() == "JOB_ID":
            JOB_ID_R.append(JOB_ID[index])
            filas[0]=len(JOB_ID_R)
        elif el.upper() == "SALARY":
            SALARY_R.append(SALARY[index])
            filas[0]=len(SALARY_R)
        elif el.upper() == "COMMISSION_PCT":
            COMMISSION_PCT_R.append(COMMISSION_PCT[index])
            filas[0]=len(COMMISSION_PCT_R)
        elif el.upper() == "MANAGER_ID":
            MANAGER_ID_R.append(MANAGER_ID[index])
            filas[0]=len(MANAGER_ID_R)
        elif el.upper() == "DEPARTMENT_ID":
            DEPARTMENT_ID_R.append(DEPARTMENT_ID[index])
            filas[0]=len(DEPARTMENT_ID_R)
#------------------------------------------------------------------------------------------
def select(valor):
    global sel
    sel = valor.split(',')
    columnas[0] = len(sel)
    return sel

def toda(index):
    #print ("{0:6s} | {1:20s} | {2:25s} | {3:25s} | {4:20s} | {5:8s} | {6:10s} | {7:8s} | {8:4s} | {9:6s} | {10:6s} |".format(EMPLOYEE_ID[index],FIRST_NAME[index],LAST_NAME[index],EMAIL[index],PHONE_NUMBER[index],HIRE_DATE[index],JOB_ID[index],SALARY[index],COMMISSION_PCT[index],MANAGER_ID[index],DEPARTMENT_ID[index]))
    EMPLOYEE_ID_R.append(EMPLOYEE_ID[index])
    FIRST_NAME_R.append(FIRST_NAME[index])
    LAST_NAME_R.append(LAST_NAME[index])
    EMAIL_R.append(EMAIL[index])
    PHONE_NUMBER_R.append(PHONE_NUMBER[index])
    HIRE_DATE_R.append(HIRE_DATE[index])
    JOB_ID_R.append(JOB_ID[index])
    SALARY_R.append(SALARY[index])
    COMMISSION_PCT_R.append(COMMISSION_PCT[index])
    MANAGER_ID_R.append(MANAGER_ID[index])
    DEPARTMENT_ID_R.append(DEPARTMENT_ID[index])

def where(campos,valor2):#Forma de introducir: where department_id=9; Campos recibe de Select, valor2 del cuadro
    si = valor2.replace(";","").split('=')
    for index in range(0,len(EMPLOYEE_ID)):
        if si[0].upper() == "EMPLOYEE_ID":
            if EMPLOYEE_ID[index] == si[1]:
                if campos[0]=="*":
                    toda(index)#Crea el Grid de 11
                else:
                    imprime(campos,index)#Crea el grid de n*m
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

class Diccionario_1(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(len(FIELD),7)
    #------------------------------------------------------Columnas
        self.SetColLabelValue(0, "FIELD_NAME")
        self.SetColLabelValue(1, "INITIAL_POSITON")
        self.SetColLabelValue(2, "LENGHT")
        self.SetColLabelValue(3, "TYPE")
        self.SetColLabelValue(4, "INITIAL_VALUE")
        self.SetColLabelValue(5, "LOWEST_VALUE")
        self.SetColLabelValue(6, "HIGHEST_VALUE")
    #-------------------------------------------------------------
        for i in range(0,len(FIELD)):
            self.SetCellValue(i, 0, FIELD[i])
            self.SetCellValue(i, 1, INI_P[i])
            self.SetCellValue(i, 2, TAM_FIELD[i])
        self.SetCellValue(0, 3,"NUMBER")
        self.SetCellValue(1, 3,"VARCHAR")
        self.SetCellValue(2, 3,"VARCHAR")
        self.SetCellValue(3, 3,"VARCHAR")
        self.SetCellValue(4, 3,"VARCHAR")
        self.SetCellValue(5, 3,"DATE")
        self.SetCellValue(6, 3,"VARCHAR")
        self.SetCellValue(7, 3,"NUMBER")
        self.SetCellValue(8, 3,"NUMBER")
        self.SetCellValue(9, 3,"NUMBER")
        self.SetCellValue(10, 3,"NUMBER")
        self.SetCellValue(0, 4,"0000001")
        self.SetCellValue(5, 4,"01/01/87")
        self.SetCellValue(7, 4,"0000001")
        self.SetCellValue(8, 4,"0.0")
        self.SetCellValue(9, 4,"00001")
        self.SetCellValue(10, 4,"00001")

        self.SetCellValue(0, 5,"0000001")
        self.SetCellValue(5, 5,"01/01/87")
        self.SetCellValue(7, 5,"0000001")
        self.SetCellValue(8, 5,"0.0")
        self.SetCellValue(9, 5,"00001")
        self.SetCellValue(10, 5,"00001")

        self.SetCellValue(0, 6,"1000000")
        self.SetCellValue(5, 6,"10/11/2020")
        self.SetCellValue(7, 6,"1000000")
        self.SetCellValue(8, 6,"1.0")
        self.SetCellValue(9, 6,"10000")
        self.SetCellValue(10, 6,"10000")

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()
#------------------------TABLA RESULTADOS--------------------------------
class Tabla_Resultados(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(filas[0],columnas[0])
        ##----------------------Columnas
        for i in range(0,columnas[0]):
            self.SetColLabelValue(i, sel[i])
            for j in range(0,filas[0]):
                if sel[i] == "EMPLOYEE_ID":
                    self.SetCellValue(j, i, EMPLOYEE_ID_R[j])
                elif sel[i] == "FIRST_NAME":
                    self.SetCellValue(j, i, FIRST_NAME_R[j])
                elif sel[i] == "LAST_NAME":
                    self.SetCellValue(j, i, LAST_NAME_R[j])
                elif sel[i] == "EMAIL":
                    self.SetCellValue(j, i, EMAIL_R[j])
                elif sel[i] == "PHONE_NUMBER":
                    self.SetCellValue(j, i, PHONE_NUMBER_R[j])
                elif sel[i] == "HIRE_DATE":
                    self.SetCellValue(j, i, HIRE_DATE_R[j])
                elif sel[i] == "JOB_ID":
                    self.SetCellValue(j, i, JOB_ID_R[j])
                elif sel[i] == "SALARY":
                    self.SetCellValue(j, i, SALARY_R[j])
                elif sel[i] == "COMMISSION_PCT":
                    self.SetCellValue(j, i, COMMISSION_PCT_R[j])
                elif sel[i] == "MANAGER_ID":
                    self.SetCellValue(j, i, MANAGER_ID_R[j])
                elif sel[i] == "DEPARTMENT_ID":
                    self.SetCellValue(j, i, DEPARTMENT_ID_R[j])
        self.AutoSize()
        self.EnableEditing(False)
        self.DisableDragGridSize()

        def EnableEditing(self, edit):
            return super().EnableEditing(edit)

        def AutoSize(self):
            return super().AutoSize()

        def DisableDragGridSize(self):
            return super().DisableDragGridSize()


#----------------------TABLA--------------------------------------------#
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

        self.AutoSize()
        self.EnableEditing(False)
        self.DisableDragGridSize()

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()


class SimpleGridEmpty(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(10, 11)
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
        self.AutoSize()
        self.EnableEditing(False)
        self.DisableDragGridSize()

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()


class TestFrameB(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "PROYECTO BASE DE DATOS OPCION B ^u^", size=(1090, 500))
        self.InitUI()

    def InitUI(self):
        Notebook = wx.Notebook(self)
        page = wx.SplitterWindow(Notebook)
        page2 = MyPanel2(Notebook)
        page3 = MyPanel3(Notebook)
        Notebook.AddPage(page,"EMPLOYEES")
        Notebook.AddPage(page2,"DICCIONARIO")
        Notebook.AddPage(page3,"RESULTADO")
        panelTabla = SimpleGridEmpty(page)
        panelOper = Operaciones(page)
        page.SplitHorizontally( panelOper, panelTabla)
        page.SetSashGravity(0.35)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        #-------------------------------------------------------------------------
        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        opciones = wx.Menu()
        salir = wx.Menu()
        #-------------------------------------------------------------------------
        opciones.Append(wx.ID_ABOUT, 'Opcion A', 'aqui se pone la opcion A')
        wx.EVT_MENU(self,wx.ID_ABOUT, self.opcionA)

        salir.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        wx.EVT_MENU(self,wx.ID_EXIT, self.salir)

        menubar.Append(opciones, 'OPCIONES')
        menubar.Append(salir, 'SALIR')
        self.SetMenuBar(menubar)

        #self.Bind(wx.EVT_MENU, self.OnQuit, fileSalir)
        self.Centre()

    def opcionA(self,event):#creditos
        ventana=TestFrame(None)
        ventana.Show(True)
        #ventana.ShowModal()

    def salir(self,event):#Salir
        salir=wx.MessageDialog(None, 'Chaup :,(','Salir', style=wx.OK)
        salir.ShowModal()
        self.Close(True)
        #-------------------------------------------------------------------


class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "PROYECTO BASE DE DATOS ^u^", size=(1090, 500))
        self.InitUI()

    def InitUI(self):
        Notebook = wx.Notebook(self)
        page = wx.SplitterWindow(Notebook)
        page2 = MyPanel2(Notebook)
      # page3 = MyPanel3(Notebook)
        Notebook.AddPage(page,"EMPLOYEES")
        Notebook.AddPage(page2,"DICCIONARIO")
        #Notebook.AddPage(page3,"RESULTADO")
        panelTabla = SimpleGrid(page)
        panelOper = Operaciones(page)
        page.SplitHorizontally( panelOper,panelTabla)
        page.SetSashGravity(0.35)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        #-------------------------------------------------------------------------
        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        opciones = wx.Menu()
        salir = wx.Menu()
        #-------------------------------------------------------------------------
        opciones.Append(wx.ID_ABOUT, 'Opcion A', 'aqui se pone la opcion A')
        #wx.EVT_MENU(self,wx.ID_ABOUT, self.opcionA)
        self.Bind(wx.EVT_MENU,self.opcionA,id=wx.ID_ABOUT)

        opciones.Append(wx.ID_ADD, 'Opcion B', 'aqui se pone la opcion B')
        #wx.EVT_MENU(self,wx.ID_ADD, self.opcionB)
        self.Bind(wx.EVT_MENU,self.opcionB,id=wx.ID_ADD)
        salir.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        #wx.EVT_MENU(self,wx.ID_EXIT, self.salir)
        self.Bind(wx.EVT_MENU,self.salir,id=wx.ID_EXIT)

        menubar.Append(opciones, 'OPCIONES')
        menubar.Append(salir, 'SALIR')
        self.SetMenuBar(menubar)

        #self.Bind(wx.EVT_MENU, self.OnQuit, fileSalir)
        self.Centre()

    def opcionA(self,event):#creditos
        ventanaA=TestFrame(None)
        ventanaA.Show(True)
        #ventana.ShowModal()

    def opcionB(self,event):#creditos
        ventanaB=TestFrameB(None)
        ventanaB.Show(True)

    def salir(self,event):#Salir
        salir=wx.MessageDialog(None, 'Chaup :,(','Salir', style=wx.OK)
        salir.ShowModal()
        self.Close(True)
        #-------------------------------------------------------------------




class Operaciones(wx.Panel):
    def __init__(self, parent):
        super(Operaciones, self).__init__(parent)
        wx.StaticBox(self, label='Instrucciones', pos=(0, 0), size=(1060, 145))
        lbl1 = wx.StaticText(self, label="SELECT ", pos=(15,30))#, pos=(0,0)
        self.Text_Enter = wx.TextCtrl(self,2,style=wx.TE_PROCESS_ENTER, pos=(65, 25), size=(180,-1))
        self.Text_Enter.SetForegroundColour(wx.BLUE)
        self.Bind(wx.EVT_TEXT_ENTER, self.Txt_Ent, id=2)
        lbl2 = wx.StaticText(self, label="FROM ", pos=(15,70))
        self.staticname = wx.TextCtrl(self, style=wx.TE_READONLY ,value="EMPLOYEES", pos=(65, 65), size=(180,-1))
        lbl3 = wx.StaticText(self, label="WHERE ", pos=(15,110))
        self.Text_Enter_1= wx.TextCtrl(self,2,style=wx.TE_PROCESS_ENTER, pos=(65, 105), size=(180,-1))
        self.Text_Enter_1.SetForegroundColour(wx.BLUE)
        self.Bind(wx.EVT_TEXT_ENTER, self.Txt_Ent, id=2)

    def Txt_Ent(self,event):
        msg1=(str(self.Text_Enter.GetValue()))
        msg2=(str(self.Text_Enter_1.GetValue()))
        if msg1 == "" or msg2 == "":
            wx.MessageBox("ERROR: Alguna Casilla Esta Vacia")
        else:
            SEL=select(msg1)
            where(SEL,msg2)
            Res=MyPanel3(self)
            Res.ShowModal()
            Res.Destroy()




class MyPanel1(wx.Panel):
   def __init__(self, parent):
      super(MyPanel1, self).__init__(parent)
      grid = SimpleGrid(self)

class MyPanel2(wx.Panel):
   def __init__(self, parent):
      super(MyPanel2, self).__init__(parent)
      grid = Diccionario_1(self)
      grid.AutoSize()
      grid.EnableEditing(False)
      grid.DisableDragGridSize()

class MyPanel3(wx.Dialog):
   def __init__(self, parent):
      #super(MyPanel3, self).__init__(parent)
      #lbl = wx.StaticText(self, label="Aca sale el resultado <3 ", pos=(15,30))
      wx.Dialog.__init__(self, parent,-1,title="Resultado",size=(1090, 500))
      grid = Tabla_Resultados(self)
      self.Centre()

if __name__ == '__main__':
    AbrirArchivo()
    Diccionario()
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()



#inst1 = input(">> ").split()
#sel = inst1[1].split(',')
#inst3 = input(">> ").split()
#num = select()
#where(num)

#---------------------------------------------------------------------------------
