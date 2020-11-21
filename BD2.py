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

nombre_tabla = [0]
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
filas = [0]
columnas  = [0]
sel = [0]
seltoda = ["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "EMAIL", "PHONE_NUMBER", "HIRE_DATE", "JOB_ID", "SALARY", "COMMISSION_PCT", "MANAGER_ID", "DEPARTMENT_ID"]

###Diccionario
FIELD = []
INI_P = []
TAM_FIELD = []
LENGHT = []
TYPE = []
I_VAL = []
L_VAL = []

def AbrirArchivo():
    global nombre_tabla
    """Esta función es para cargar la tabla desde un archivo"""
    archivo = open('','r')
    """ASAEL"""#C:/Users/User/OneDrive/Escritorio/python-course/Progs/BasedeDatos/basededatos.txt
    """BARDO"""#c:/Users/Lenovo/Desktop/Python/basededatos.txt
    formato = archivo.readline().rstrip()
    formato = formato.split(',')
    nombre_tabla[0]=(formato[0])
    formato.pop(0)
    lin = []
    tam = []
    ind = 0
    for part in formato:
        if part.isnumeric():
            lin.append(int(part))
            if ind > 0 and not (ind%2)==0:
                tam.append(lin[ind] - (lin[ind-1]-1))
            ind = ind + 1
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
        laCompleta.clear()

    archivo.close()
#------------------------------------------------------------------------------------------
def Diccionario():
    archivo = open('','r')
    """ASAEL"""#C:/Users/User/OneDrive/Escritorio/python-course/Progs/BasedeDatos/basededatos.txt
    """BARDO"""#c:/Users/Lenovo/Desktop/Python/basededatos.txt
    cadena = archivo.readline().rstrip()
    cadena= cadena.split(',')#aqui estan las palabras de los campos con las posiciones
    cadena.pop(0)
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
    #esta parte requiere de los datos pasados a tabla
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
    filas[0]=len(DEPARTMENT_ID_R)
    columnas[0]=11

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
        if sel[0]=="*":
            self.HazTabla(seltoda)
        else:
            self.HazTabla(sel)
        self.AutoSize()
        self.EnableEditing(False)
        self.DisableDragGridSize()

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()

    def HazTabla(self,renglones):
        for i in range(0,columnas[0]):
            self.SetColLabelValue(i, renglones[i].upper())
            for j in range(0,filas[0]):
                if renglones[i].upper() == "EMPLOYEE_ID":
                    self.SetCellValue(j, i, EMPLOYEE_ID_R[j])
                elif renglones[i].upper() == "FIRST_NAME":
                    self.SetCellValue(j, i, FIRST_NAME_R[j])
                elif renglones[i].upper() == "LAST_NAME":
                    self.SetCellValue(j, i, LAST_NAME_R[j])
                elif renglones[i].upper() == "EMAIL":
                    self.SetCellValue(j, i, EMAIL_R[j])
                elif renglones[i].upper() == "PHONE_NUMBER":
                    self.SetCellValue(j, i, PHONE_NUMBER_R[j])
                elif renglones[i].upper() == "HIRE_DATE":
                    self.SetCellValue(j, i, HIRE_DATE_R[j])
                elif renglones[i].upper() == "JOB_ID":
                    self.SetCellValue(j, i, JOB_ID_R[j])
                elif renglones[i].upper() == "SALARY":
                    self.SetCellValue(j, i, SALARY_R[j])
                elif renglones[i].upper() == "COMMISSION_PCT":
                    self.SetCellValue(j, i, COMMISSION_PCT_R[j])
                elif renglones[i].upper() == "MANAGER_ID":
                    self.SetCellValue(j, i, MANAGER_ID_R[j])
                elif renglones[i].upper() == "DEPARTMENT_ID":
                    self.SetCellValue(j, i, DEPARTMENT_ID_R[j])


#------------------------TABLA RESULTADOS--------------------------------
class Tabla_Select(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        ##----------------------Columnas
        if sel[0]=="*":
            self.CreateGrid(len(EMPLOYEE_ID),11)
            self.HazTabla(seltoda)
        else:
            self.CreateGrid(len(EMPLOYEE_ID),columnas[0])
            self.HazTabla(sel)
        self.AutoSize()
        self.EnableEditing(False)
        self.DisableDragGridSize()

    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()

    def DisableDragGridSize(self):
        return super().DisableDragGridSize()

    def HazTabla(self,renglones):
        for i in range(0,len(renglones)):
            self.SetColLabelValue(i, renglones[i].upper())
            for j in range(0,len(EMPLOYEE_ID)):
                if renglones[i].upper() == "EMPLOYEE_ID":
                    self.SetCellValue(j, i, EMPLOYEE_ID[j])
                elif renglones[i].upper() == "FIRST_NAME":
                    self.SetCellValue(j, i, FIRST_NAME[j])
                elif renglones[i].upper() == "LAST_NAME":
                    self.SetCellValue(j, i, LAST_NAME[j])
                elif renglones[i].upper() == "EMAIL":
                    self.SetCellValue(j, i, EMAIL[j])
                elif renglones[i].upper() == "PHONE_NUMBER":
                    self.SetCellValue(j, i, PHONE_NUMBER[j])
                elif renglones[i].upper() == "HIRE_DATE":
                    self.SetCellValue(j, i, HIRE_DATE[j])
                elif renglones[i].upper() == "JOB_ID":
                    self.SetCellValue(j, i, JOB_ID[j])
                elif renglones[i].upper() == "SALARY":
                    self.SetCellValue(j, i, SALARY[j])
                elif renglones[i].upper() == "COMMISSION_PCT":
                    self.SetCellValue(j, i, COMMISSION_PCT[j])
                elif renglones[i].upper() == "MANAGER_ID":
                    self.SetCellValue(j, i, MANAGER_ID[j])
                elif renglones[i].upper() == "DEPARTMENT_ID":
                    self.SetCellValue(j, i, DEPARTMENT_ID[j])


#----------------------TABLA--------------------------------------------#
class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(107, 11)
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
        Notebook.AddPage(page,nombre_tabla[0])
        Notebook.AddPage(page2,"DICCIONARIO")
        Notebook.AddPage(page3,"RESULTADO")
        panelTabla = SimpleGridEmpty(page)
        panelOper = Operaciones(page)
        page.SplitHorizontally( panelOper, panelTabla)
        page.SetSashGravity(0.35)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        opciones = wx.Menu()
        salir = wx.Menu()
        opciones.Append(wx.ID_ABOUT, 'Opcion A', 'aqui se pone la opcion A')
        self.Bind(wx.EVT_MENU,self.opcionA,id=wx.ID_ABOUT)
        salir.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU,self.salir,id=wx.ID_EXIT)
        menubar.Append(opciones, 'OPCIONES')
        menubar.Append(salir, 'SALIR')
        self.SetMenuBar(menubar)
        self.Centre()

    def opcionA(self,event):#creditos
        ventana=TestFrame(None)
        ventana.Show(True)
        self.Close(True)

    def salir(self,event):#Salir
        salir=wx.MessageDialog(None, 'Chaup :\'(','Salir', style=wx.OK)
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
        Notebook.AddPage(page,nombre_tabla[0])
        Notebook.AddPage(page2,"DICCIONARIO")
        panelTabla = SimpleGrid(page)
        panelOper = Operaciones(page)
        page.SplitHorizontally( panelOper,panelTabla)
        page.SetSashGravity(0.35)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        opciones = wx.Menu()
        salir = wx.Menu()
        #opciones.Append(wx.ID_ABOUT, 'Opcion A', 'aqui se pone la opcion A')
        #self.Bind(wx.EVT_MENU,self.opcionA,id=wx.ID_ABOUT)
        opciones.Append(wx.ID_ADD, 'Opcion B', 'aqui se pone la opcion B')
        self.Bind(wx.EVT_MENU,self.opcionB,id=wx.ID_ADD)
        salir.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU,self.salir,id=wx.ID_EXIT)
        menubar.Append(opciones, 'OPCIONES')
        menubar.Append(salir, 'SALIR')
        self.SetMenuBar(menubar)
        self.Centre()

    def opcionB(self,event):#creditos
        ventanaB=TestFrameB(None)
        ventanaB.Show(True)
        self.Close(True)

    def salir(self,event):#Salir
        salir=wx.MessageDialog(None, 'Chaup :\'(','Salir', style=wx.OK)
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
        self.staticname = wx.TextCtrl(self, style=wx.TE_READONLY ,value=nombre_tabla[0], pos=(65, 65), size=(180,-1))
        lbl3 = wx.StaticText(self, label="WHERE ", pos=(15,110))
        self.Text_Enter_1= wx.TextCtrl(self,2,style=wx.TE_PROCESS_ENTER, pos=(65, 105), size=(180,-1))
        self.Text_Enter_1.SetForegroundColour(wx.BLUE)
        self.Bind(wx.EVT_TEXT_ENTER, self.Txt_Ent, id=2)
    #----------------------------------------------------------------------------
        self.Limpiar = wx.Button(self, label="LIMPIAR",pos=(270,50), size=(180,40))
        self.Limpiar.Bind(wx.EVT_BUTTON,self.OnClicked)

    def OnClicked(self,event):
        global filas
        global columnas
        global sel
        global EMPLOYEE_ID_R
        global FIRST_NAME_R
        global LAST_NAME_R
        global EMAIL_R
        global PHONE_NUMBER_R
        global HIRE_DATE_R
        global JOB_ID_R
        global SALARY_R
        global COMMISSION_PCT_R
        global MANAGER_ID_R
        global DEPARTMENT_ID_R
        EMPLOYEE_ID_R.clear()
        FIRST_NAME_R.clear()
        LAST_NAME_R.clear()
        EMAIL_R.clear()
        PHONE_NUMBER_R .clear()
        HIRE_DATE_R.clear()
        JOB_ID_R.clear()
        SALARY_R.clear()
        COMMISSION_PCT_R.clear()
        MANAGER_ID_R.clear()
        DEPARTMENT_ID_R.clear()
        sel = [0]
        filas = [0]
        columnas = [0]
        self.Text_Enter.Clear()
        self.Text_Enter_1.Clear()
    #------------------------------------------------------------------------------

    def Txt_Ent(self,event):
        msg1=(str(self.Text_Enter.GetValue()))
        msg2=(str(self.Text_Enter_1.GetValue()))
        if msg1 == "" or msg2 == "":
            wx.MessageBox("ERROR: Alguna Casilla Esta Vacia")
        else:
            sel.clear()
            SEL=select(msg1)
            where(SEL,msg2)
            Select=MyPanel4(self)
            Select.Show()
            Res=MyPanel3(self)
            Res.Show()
            #Res.Destroy()

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
      wx.Dialog.__init__(self, parent,-1,title="TABLA RESULTADO DE SELECT Y WHERE",size=(1090, 500))
      grid = Tabla_Resultados(self)
      self.Centre()

class MyPanel4(wx.Dialog):
   def __init__(self, parent):
      wx.Dialog.__init__(self, parent,-1,title="TABLA RESULTADO DE SELECT",size=(1090, 500))
      grid = Tabla_Select(self)
      self.Centre()

if __name__ == '__main__':
    AbrirArchivo()
    Diccionario()
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()
#---------------------------------------------------------------------------------