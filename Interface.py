# import wx

# class MiAplicacion(wx.Frame):
#     def __init__(self,parent,title):
#         wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))



#         self.Centre(True)
#         self.Show()
    
# if __name__=='__main__':
#     app = wx.App()
#     frame = MiAplicacion(None,u"Mi primera Interfaz")
#     app.MainLoop()

#Pag 159: http://index-of.co.uk/Tutorials/wxPython%20in%20Action.pdf
import wx
import wx.grid

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1, pos=(0,150))
        self.CreateGrid(9, 2)
        self.SetColLabelValue(0, "First")
        self.SetColLabelValue(1, "Last")
        self.SetRowLabelValue(0, "CF")
        self.SetCellValue(0, 0, "Bob")
        self.SetCellValue(0, 1, "Dernier")
        self.SetRowLabelValue(1, "2B")
        self.SetCellValue(1, 0, "Ryne")
        self.SetCellValue(1, 1, "Sandberg")
        self.SetRowLabelValue(2, "LF")
        self.SetCellValue(2, 0, "Gary")
        self.SetCellValue(2, 1, "Matthews")
        self.SetRowLabelValue(3, "1B")
        self.SetCellValue(3, 0, "Leon")
        self.SetCellValue(3, 1, "Durham")
        self.SetRowLabelValue(4, "RF")
        self.SetCellValue(4, 0, "Keith")
        self.SetCellValue(4, 1, "Moreland")
        self.SetRowLabelValue(5, "3B")
        self.SetCellValue(5, 0, "Ron")
        self.SetCellValue(5, 1, "Cey")
        self.SetRowLabelValue(6, "C")
        self.SetCellValue(6, 0, "Jody")
        self.SetCellValue(6, 1, "Davis")
        self.SetRowLabelValue(7, "SS")
        self.SetCellValue(7, 0, "Larry")
        self.SetCellValue(7, 1, "Bowa")
        self.SetRowLabelValue(8, "P")
        self.SetCellValue(8, 0, "Rick")
        self.SetCellValue(8, 1, "Sutcliffe")
    
    def EnableEditing(self, edit):
        return super().EnableEditing(edit)

    def AutoSize(self):
        return super().AutoSize()
    
    def DisableDragGridSize(self):
        return super().DisableDragGridSize()

# class TestFrame(wx.Frame):
#     def __init__(self, parent):
#         wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        
#         grid = SimpleGrid(self)
#         grid.AutoSize()
#         grid.EnableEditing(False)
#         grid.DisableDragGridSize()

#if __name__ == '__main__':
#     app = wx.App()
#     frame = TestFrame(None)
#     frame.Show(True)
#     app.MainLoop()

#import wx
 
# app = wx.App()

# self = wx.Frame(None, -1, "Vonceff", size=(600,600))

# Panel = wx.Panel(self)
# Notebook = wx.Notebook(Panel)

# page_1 = SimpleGrid(Notebook)#wx.Panel(Notebook)
# page_2 = wx.Panel(Notebook)

# #a = wx.StaticText(page_1, -1, "Esto esta en la pestaña 1")
# b = wx.StaticText(page_2, -1, "Esto esta en la pestaña 2")

# Notebook.AddPage(page_1, "Tab 1")
# Notebook.AddPage(page_2, "Tab 2")

# sizer = wx.BoxSizer()
# sizer.Add(Notebook, 1, wx.EXPAND)
# Panel.SetSizer(sizer)

# self.Show()

# app.MainLoop()


# import wx
  
# class MyDialog(wx.Dialog): 
#    def __init__(self, parent, title): 
#       super(MyDialog, self).__init__(parent, title = title, size = (250,150)) 
#       panel = wx.Panel(self) 
#       self.btn = wx.Button(panel, wx.ID_OK, label = "ok", size = (50,20), pos = (75,50)) 
     
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title, size = (1090,500))  
      self.InitUI() 
         
   def InitUI(self):    
      nb = wx.Notebook(self) 
      nb.AddPage(MyPanel1(nb),"Editor") 
      nb.AddPage(MyPanel2(nb),"RadioButtons") 
      self.Centre() 
      self.Show(True) 
		
class MyPanel1(wx.Panel): 
   def __init__(self, parent): 
      super(MyPanel1, self).__init__(parent) 
      #text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (250,150)) 
      lbl1 = wx.StaticText(self, label="Position")#, pos=(0,0)
      grid = SimpleGrid(self)
      grid.AutoSize()
      grid.EnableEditing(False)
      grid.DisableDragGridSize()
		
class MyPanel2(wx.Panel): 
   def __init__(self, parent): 
      super(MyPanel2, self).__init__(parent) 
      lblList = ['Value X', 'Value Y', 'Value Z']         
      rbox = wx.RadioBox(self, label = 'RadioBox', pos = (25,10), choices = lblList,
         majorDimension = 1, style = wx.RA_SPECIFY_ROWS) 
     
ex = wx.App() 
Mywin(None,'NoteBook demo') 
ex.MainLoop()
