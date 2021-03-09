# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:33:17 2020

@author: Georgy
"""
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import time
import os
import ast
from collections import deque
palabrasno = ['__name__', 'main']
class FuncCallVisitor(ast.NodeVisitor):
   def __init__(self):
       self._name = deque()

   @property
   def name(self):
       return '.'.join(self._name)

   @name.deleter
   def name(self):
       self._name.clear()

   def visit_Name(self, node):
       self._name.appendleft(node.id)

   def visit_Attribute(self, node):
       try:
           self._name.appendleft(node.attr)
           self._name.appendleft(node.value.id)
       except AttributeError:
           self.generic_visit(node)

def get_func_calls(tree):
   func_calls = []
   for node in ast.walk(tree):
       if isinstance(node, ast.Call):
           callvisitor = FuncCallVisitor()
           callvisitor.visit(node.func)
           func_calls.append(callvisitor.name)
   return func_calls

class Py2Neko(ast.NodeVisitor):
   def generic_visit(self, node):
     ast.NodeVisitor.generic_visit(self, node)

   def visit_Name(self, node):
       if node.id not in palabrasno:
      
               copia_variable.append(node.id)
               line_my_variable.append(node.lineno)
           
               

   def visit_Num(self, node):
       drop=0

   def visit_Str(self, node):
       drop=0

   def visit_Print(self, node):
       drop=0
   def visit_Assign(self, node):

    ast.NodeVisitor.generic_visit(self, node)

   def visit_Expr(self, node):
       drop=0


class my_class(ast.NodeVisitor):
  def generic_visit(self, node):
    ast.NodeVisitor.generic_visit(self, node)
  
  def visit_FunctionDef(self, node): 
         
          copia_def.append(node.name)
          line_my_def.append(node.lineno)
  def visit_Import(self, stmt_import):
      for alias in stmt_import.names:
          copia.append(alias.name)
          line_my.append(stmt_import.lineno)
  def visit_ImportFrom(self, stmt_import):
        
        
        
        for alias in stmt_import.names:
           copia.append(alias.name)
           line_my.append(stmt_import.lineno) 
           copia_importfrom.append(stmt_import.module+"@"+alias.name)
           
        
           
class Xuy(ast.NodeVisitor):
    def generic_visit(self, node):
              ast.NodeVisitor.generic_visit(self, node)
              #print("\n")
      
              xuy =""
              try :
                  uy = str(node)
                  
                  xuy = str(node.lineno) + "@lineno@" + str(uy[uy.find('.')+1:uy.find(' object at ')]) +"@node@"
                  try :
                      xuy = xuy + node.id + "@id@"
                  except:
                      xuy = xuy + "@NOid@"
                  copia_variable_ast.append(xuy)
                 
              except :                     
                  xuy = ""
#######################
palabrasnoA = ['__name__', 'main']                 

countfromsA = 0
class v(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        drop=0
    def visit_FunctionDef(self, node):
        FuncionesDefinidasA.append(node.name)

    def visit_Import(self, stmt_import):
        for alias in stmt_import.names:
            ImportsA.append(alias.name)
            ImportsLA.append(stmt_import.lineno)

class FuncCallVisitorA(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()

    @property
    def name(self):
        return '.'.join(self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Name(self, node):
        self._name.appendleft(node.id)

    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)

        except AttributeError:
            self.generic_visit(node)


def get_func_callsA(tree):
    func_callsA = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            callvisitorA = FuncCallVisitorA()
            callvisitorA.visit(node.func)
            L2 = node.lineno
            if str(callvisitorA.name) == 'input.lower':
                L2+=2
            if callvisitorA.name in CallsA:
                I = CallsA.index(callvisitorA.name)
                CallsLA[I].append(L2)
            else:
                CallsLA.append([])
                CallsA.append(callvisitorA.name)
                CallsLA[CallsA.index(callvisitorA.name)].append(L2)
            func_callsA.append(callvisitorA.name)

    return func_callsA

class Py2NekoA(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        VarA = node.id
        if VarA not in palabrasnoA:
            if VarA in VariablesA:
                I = VariablesA.index(VarA)
                VariablesLA[I].append(node.lineno)
            else:
                VariablesLA.append([])
                VariablesA.append(node.id)
                VariablesLA[VariablesA.index(VarA)].append(node.lineno)

    def visit_Assign(self, node):

        ast.NodeVisitor.generic_visit(self, node)


class ImportNodeVisitorA(ast.NodeVisitor):
    def visit_Import(self, node):
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        FIA.append(node.lineno)
        FromA.append(node.module)
        for alias in node.names:
            ImpA.append(alias.name)
        self.generic_visit(node)


                      
#####################################  #        
class CustomPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)              
        self.cell(0, 5, 'PYTHON CODE ANALYSIS', ln=1)
        self.cell(100)
        self.image('logo1.jpg', 150, 8, 33)      
    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)      
        page = 'Page ' + str(self.page_no()) + '|{nb}'
        self.cell(200)
        self.cell(-30, -10, page, 0, 0, 'C')
class CustomPDF_titol(FPDF):
    def header(self):
        if self.page_no() > 1 :
            self.set_font('Arial', 'B', 15)              
            self.cell(0, 5, 'PYTHON CODE ANALYSIS', ln=1)
            self.cell(100)
            self.image('logo1.jpg', 150, 8, 33)      
while True:
    file_name = (input("input the name of archive with files with witch you want to work: ")) 
    if  os.path.isdir(file_name) :
        break   
    else :
        print("THIS ARCHIVE DO NOT EXSIST")     
pdf_titol =CustomPDF_titol()
pdf_titol.add_page()
pdf_titol.set_font("Arial", size=12)   
fecha = time.strftime("%d/%m/%y")
pdf_titol.image('logo1.jpg', 150, 30, 50)
pdf_titol.cell(21)
pdf_titol.set_font("Arial", size=22)
pdf_titol.cell(-1, 160, 'PYTHON CODE ANALYSIS')
pdf_titol.cell(1)
pdf_titol.cell(-1, 200, 'TecnoCampus')
pdf_titol.cell(1)
pdf_titol.set_font("Arial", size=14)
pdf_titol.cell(-1, 250, fecha)
pdf_titol.cell(1)
pdf_titol.set_font("Arial", size=18)
pdf_titol.set_y(160)
pdf_titol.set_x(150)
pdf_titol.cell(-1, 70, 'Belyakov Georgy')
pdf_titol.cell(1)
pdf_titol.cell(-1, 85, 'Sabater Andres')
pdf_titol.set_font("Arial", size=12)
pdf_titol.set_draw_color(224, 165, 0)
pdf_titol.set_line_width(5)
pdf_titol.line(20, 10, 20, 270)

pdf_titol.set_y(250)
pdf_titol.set_x(30)
pdf_titol.set_font("Arial", 'B' , size=8)
pdf_titol.set_text_color(0, 0, 0)
pdf_titol.multi_cell(155, 3,'The information contained in this document may be privileged and / or confidential. Any dissemination, distribution or copying of this document by anyone other than the original recipients is strictly prohibited. If you received this document in error, please notify the issuer immediately and delete any copies of this document.')

pdf_titol.add_page()  
pdf_titol.set_y(30)
pdf_titol.set_x(10)
pdf_titol.set_font("Arial", size=24)
pdf_titol.cell(-1, 10, 'INDEX',ln=1)
pdf = CustomPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_y(30)
pdf.set_x(10)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '1. Introduction', ln=1)
pdf_titol.set_x(20)
pdf_titol.set_font("Arial", 'B' , size=20)
pdf_titol.cell(-1, 10, '1. Introduction')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10, '%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '1.1. Description', ln=1)
pdf_titol.set_x(30)
pdf_titol.set_font("Arial",  size=20)
pdf_titol.cell(-1, 10, '1.1. Description')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10,'%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.cell(-1, 10, 'This a report document of the code in Python for project %s.The files of the project are:' %file_name, ln=1)
orig_dir = os.getcwd()
os.chdir(file_name)
files = os.listdir()
os.chdir(orig_dir)
i=0
while True :    
    try :
        pdf.set_x(30)
        pdf.cell(10,10, '* %s' %files[i], ln=1)
        i=i+1
    except :
        break
pdf.set_x(10)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '1.2. Objectives', ln=1)
pdf_titol.set_x(30)
pdf_titol.cell(-1, 10, '1.2. Objectives')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10, '%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(190, 10,'The objective of the document is to extract from the project coded in Python the main components, with the functions, the variables. This is the way to have a better understanding of the code,and to shorten the time to manage any improvement or modification of the code.')
pdf.cell(-1, 10, 'The document includes:', ln=1)
pdf.set_x(30)
pdf.cell(-1, 10, '* The functions', ln=1)
pdf.set_x(30)
pdf.cell(-1, 10, '* The variables', ln=1)
pdf.set_x(30)
pdf.cell(-1, 10, '* The relationship between them', ln=1)
pdf.set_x(30)
pdf.cell(-1, 10, '* The imported libraries', ln=1)
pdf.set_x(30)
pdf.cell(-1, 10, '* The list of comments', ln=1)
pdf.add_page()
pdf.set_x(10)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '1.3. The structure of the project', ln=1)
pdf_titol.set_x(30)
pdf_titol.cell(-1, 10, '1.3. The structure of the project')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10,'%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.cell(-1, 10, 'The structure of the code is:', ln=1)
num_file=0
i_num_columna = 1
pdf.set_fill_color(255, 255, 0)
num_prog = 0 
defined_file=[]
while True :    
    try :       
            my_f = open(os.path.join(os.path.dirname(__file__),file_name,files[num_file]),'r') 
            defined_file.append(files[num_file])            
            ii = 0 
            num_prog=num_prog+1
            pdf.set_font("Arial", size=8)
            for line in my_f :
                
                if 'def ' in line :
                    c = line[line.find('def')+4:line.find(':')]
                    pdf.line(7+33*(i_num_columna-1), 55+ii*30 , 10+33*(i_num_columna-1), 55+ii*30)                    
                    pdf.line(7+33*(i_num_columna-1), 55+(ii)*30 , 7+33*(i_num_columna-1), 55+(ii+1)*30)
                    pdf.line(7+33*(i_num_columna-1), 55+(ii+1)*30 , 10+33*(i_num_columna-1), 55+(ii+1)*30)
                    pdf.rect(10+33*(i_num_columna-1), 70+ii*30, 27, 20)
                    pdf.set_y(70+ii*30)
                    pdf.set_x(10+33*(i_num_columna-1)) 
                    pdf.multi_cell(27,5, '%s'%c)
                    ii=1+ii
            if ii == 0 :
                pdf.set_font("Arial", size=12)
                pdf.set_y(30)
                pdf.set_x(80)      
                pdf.multi_cell(35,10, '%s' %files[num_file])
                pdf.rect(80, 30, 35, 10)  
                pdf.line(97, 40 , 97, 45)             
            else:
                pdf.set_font("Arial", size=12)
                pdf.set_y(50)
                pdf.set_x(10+33*(i_num_columna-1)) 
                #pdf.cell(-1,10, '%s' %files[i])
                pdf.multi_cell(27,10, '%s' %files[num_file])
                pdf.line(25+33*(i_num_columna-1), 45 , 97, 45)
                pdf.line(25+33*(i_num_columna-1), 45 ,25+33*(i_num_columna-1), 50)
                pdf.rect(10+33*(i_num_columna-1), 50, 27, 10)  
                i_num_columna = i_num_columna + 1                     
            my_f.close() 
            num_file=num_file+1
    except :
        break
pdf.add_page()
pdf.set_y(30)
pdf.set_x(10)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '2. The programs', ln=1)
pdf_titol.set_x(20)
pdf_titol.set_font("Arial", 'B' , size=20)
pdf_titol.cell(-1, 10, '2. The programs')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10, '%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.cell(-1, 10, 'The list of programs of the project is detailed in the next section', ln=1)
num_file=0

defined_function=0
defined_variable=[]
defined_libraries=[]
defined_lines=0

#print("!!!_%s" %type(num_file))
while True :    
    try : 
        copia = []
        copia_importfrom=[]
        line_my=[] 
        copia_def = []
        line_my_def=[]
        copia_Hash = []
        line_my_Hash=[]
        ImportsA = []
        ImportsLA = []
        FuncionesDefinidasA = []
        VariablesA = []
        VariablesLA = []
        
        FGenericasA = []
        FGenericasLA = []
        
        FVariablesA = []
        FVariablesLA = []
        
        FImportsA = []
        FImportsLA = []
        
        CallsA = []
        CallsLA = []
        
        FromA = []
        ImpA = []
        FIA = []       
        line_my_variable=[]
        copia_variable=[]
        copia_variable_ast=[]
        my_f = open(os.path.join(os.path.dirname(__file__),file_name,files[num_file]),'r') 
        
        
        pdf.set_x(10)
        pdf.set_font("Arial", size=20)
        pdf.set_text_color(224, 165, 0)
        pdf.cell(-1, 10, '2.%d. %s' %(num_file+1,files[num_file]) , ln=1)
        pdf_titol.set_x(30)
        pdf_titol.set_font("Arial", size=20)
        pdf.set_text_color(0, 0, 0)
        pdf_titol.cell(-1, 10, '2.%d. %s' %(num_file+1,files[num_file]) )
        pdf_titol.set_x(-30)
        pdf_titol.cell(-1, 10, '%d' %pdf.page_no() ,ln=1)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0) 
        pdf.cell(-1, 10, 'Imported libraries are:' , ln=1)

        
        tree = ast.parse(my_f.read())     
        calls = get_func_calls(tree)
        #################################
        P = get_func_callsA(tree)
        xx = v()
        xx.visit(tree)
        for z in range(len(ImportsA)):
            palabrasnoA.append(ImportsA[z])
        for y in range(len(CallsA)):
            palabrasnoA.append(CallsA[y])
        Ass = Py2NekoA()
        Ass.visit(tree)    
        
        for x in range(len(VariablesLA)):
            VariablesLA[x] = list(set(VariablesLA[x]))
            VariablesLA[x] = sorted(VariablesLA[x])
        T = ImportNodeVisitorA()
        T.visit(tree)    
        
        for l in range(len(ImportsA)):
            ImpA.append(ImportsA[l])
            FIA.append([])
            FIA.append(ImportsLA[l])
        #####################
        x = my_class()
        x.visit(tree) 
        Imports=[]
        for z in range(len(Imports)):
            palabrasno.append(Imports[z])
        for y in range(len(calls)):
            palabrasno.append(calls[y])
        variabless = Py2Neko()
        variabless.visit(tree)
        u_xuy = Xuy()
        u_xuy.visit(tree)
        Sinrepetidos = []
        
        cont =0
        for i in copia:
            if i not in Sinrepetidos:
                pdf.set_x(30)
                pdf.set_font("Arial", size=12)
                pdf.set_text_color(0, 0, 0)
                er= False
                try : 
                    
                    for o in copia_importfrom : 
                        
                        if i in o[o.find("@"):] : 
                                pdf.cell(-1, 10, '%s imported from %s: line %d' %(i , o[:o.find("@")] , line_my[cont]), ln=1) 
                                er=True
                        else:    
                                pdf.cell(-1, 10, '%s: line %d' %(i , line_my[cont]), ln=1)  
                                er=True
                except:
                     er=True
                     pdf.cell(-1, 10, '%s: line %d' %(i , line_my[cont]), ln=1)  
                if er !=True :
                    pdf.cell(-1, 10, '%s: line %d' %(i , line_my[cont]), ln=1) 
                     
                Sinrepetidos.append(i)
                
                
                if (i+".py") not  in defined_file and  i not in defined_libraries  :
                    defined_libraries.append(i) 
                    
            cont = cont + 1 
        pdf.set_text_color(0, 0, 0) 
        pdf.set_x(10)
        pdf.cell(-1, 10, 'Defined functions are:' , ln=1)    
        Sinrepetidos = []
        cont =0
        my_error = False 
        for i in copia_def:
            if i not in Sinrepetidos:
                pdf.set_x(30)
                pdf.set_font("Arial", size=12)
                pdf.set_text_color(0, 0, 0) 
                pdf.cell(-1, 10, '%s(): line %d' %(i , line_my_def[cont]), ln=1)               
                Sinrepetidos.append(i)
                my_error = True
            cont = cont + 1 
        if my_error == False : 
             pdf.set_x(30)
             pdf.cell(-1, 10, 'There are no defined functions' , ln=1)
        pdf.set_x(10)
        pdf.set_text_color(0, 0, 0) 
        pdf.cell(-1, 10, 'The comments on code are:' , ln=1)
        Sinrepetidos = []
              
        my_error = False 
        my_f.close()
        my_f = open(os.path.join(os.path.dirname(__file__),file_name,files[num_file]),'r') 
        cont =0
        lines=[]
        for line in my_f :
                lines.append(line)
                cont=cont+1               
                if '#' in line :                                   
                    pdf.set_font("Arial", size=12)
                    pdf.set_text_color(0, 0, 0)
                    pdf.cell(-1,5,'',ln=1)
                    pdf.set_x(30)
                    pdf.multi_cell(150, 5, '%s: line%d' %(line[line.find('#')+1:line.find('\n')] ,cont))                                 
                    my_error = True      
        if my_error == False : 
             pdf.set_x(30)
             pdf.cell(-1, 10, 'There are no comments' , ln=1)
        pdf.set_x(10)
        pdf.set_text_color(0, 0, 0) 
        pdf.cell(-1, 10, 'The used variables are:' , ln=1)
        Sinrepetidos = []
        cont =0       
        my_error = False 
        
        
        
        ##################################
        for i in copia_variable: 
            if  (i not in Sinrepetidos and i not in copia ):
                mis_datos=[]
                mis_func=[]
                mis_func_def=[]
                my_text = ""
                iii=""
                if i not in defined_variable:
                    defined_variable.append(i)
                Sinrepetidos.append(i)
                for ii in copia_variable_ast :
                    if "@id@" in ii :
                        
                        for o in copia:
                            if ii not in mis_datos  and o in iii and i == ii[ii.find("@node@")+6:ii.find("@id@")]:                                      
                                 
                                 mis_datos.append(ii)                                
                        if  ii not in mis_datos   and "Attribute" in iii    and i == ii[ii.find("@node@")+6:ii.find("@id@")]:                                 
                            
                            mis_datos.append(ii)
                        elif ii not in mis_datos   and i == ii[ii.find("@node@")+6:ii.find("@id@")]:     
                            
                            mis_datos.append(ii)
                    iii=ii
                
                try:
                    pdf.set_x(30)
                    pdf.set_font("Arial", size=12)
                    pdf.set_text_color(0, 0, 0) 
                    pdf.cell(-1, 10, '%s :' %i , ln=1)
                    pdf.set_x(40)
                    u = mis_datos[0]
                    
                    pdf.cell(-1, 10, 'First use in line %s' %u[:u.find("@lineno@")], ln=1) 
                   
                    
                    
                    if len(mis_datos) >=2:
                        pdf.set_x(40)
                        pdf.cell(-1, 10, 'Next uses:', ln=1)
                        cont_i = 1 
                        text = "line: "
                        while cont_i  < len(mis_datos)-1:                          
                            u = mis_datos[cont_i]
                            text =  text + u[:u.find("@lineno@")] + ", "
                            cont_i=cont_i+1
                        u = mis_datos[len(mis_datos)-1]    
                        text =  text + u[:u.find("@lineno@")] + ";"
                        pdf.set_x(50)
                        pdf.multi_cell(100, 5,'%s' %text)
                           
                except:
                    iii=""
                ##################################
        
        pdf.set_x(10)
        pdf.set_text_color(0, 0, 0) 
        
        Sinrepetidos = []
        Sinrepetidos_2 = []
        iii=""
        iiii=""
        for ii in copia_variable_ast :
                    if "@id@" in ii :
                        for o in copia_def :
                            if o in ii and ii not in mis_func_def :
                                mis_func_def.append(ii)
                        for o in copia : 
                             if o in ii and ii not in mis_func:
                                 mis_func.append(ii)
                        #if iii not in Sinrepetidos and  "@NOid@" in iii and  ii not in mis_func_def and ii not in  mis_func :
        y=0  
        repe=[]             
        for line in lines : 
          try: 
            y=y+1
            xxx=""
            yyy=""
            if "in enumerate(" in line :
                
                yyy="enumerate()@" + str(y) 
                
               
                Sinrepetidos.append(yyy)
                
            if " int(" in line :
                
                yyy= "int()@" + str(y)
                
                Sinrepetidos.append(yyy)   
            if "input(" in line :
                yyy="intput()@" + str(y)
               
                Sinrepetidos.append(yyy) 
            if "len(" in line :
                yyy="len()@" + str(y) 
               
                Sinrepetidos.append(yyy)    
            if ".format(" in line :
                yyy="format()@" + str(y) 
                
                Sinrepetidos.append(yyy)    
            if "range(" in line :
                yyy="range()@" +str(y) 
               
                Sinrepetidos.append(yyy)    
            if ".stripped_strings" in line :
                xxx=".stripped_strings@" + str(y)
                
                Sinrepetidos_2.append(xxx)    
            if ".append(" in line :
                xxx=".append@" + str(y)
                
                Sinrepetidos_2.append(xxx)  
            if ".replace(" in line :
                yyy="replace@" + str(y)
               
                Sinrepetidos.append(yyy)      
            if "lower(" in line :
                yyy="lower()@" + str(y)
                
                Sinrepetidos.append(yyy) 
            if "print(" in line :
                yyy="print()@" + str(y)
                
                Sinrepetidos.append(yyy) 
           
          except:      
              yyy=""  
              xxx="" 
                    
                    
        pdf.set_x(10)
        pdf.set_text_color(0, 0, 0) 
        pdf.cell(-1, 10, 'The used functions are:' , ln=1)
        pdf.set_x(30)
        if len(mis_func_def)!=0:
            
            pdf.cell(-1, 10, "From %s: " %files[num_file] , ln=1)
        
        
        for p in mis_func_def:
            pdf.set_x(40)
            pdf.cell(-1, 10, "%s(): line %s" %(p[p.find("@node@")+6:p.find("@id@")]  , p[:p.find("@lineno@")]) ,ln=1)
        pdf.set_x(40)
                                   
        text = " "
        n = []
        
        lnn=""
        for p in mis_func:
            
            if p[p.find("@node@")+6:p.find("@id@")] not in n:
                
                pdf.set_x(40)
                if text != " ":
                     text = text[:len(text)-2] +";"
                     pdf.cell(-1, 10, "%s() line: %s" %(lnn , text) ,ln=1)
                     
                     #print("%s"%text)
                    
                    
                text=" "
                pdf.set_x(30)
                ############################################################
                
                er= 0
                err=[]
                try : 
                    
                    for o in copia_importfrom : 
                        
                        if p[p.find("@node@")+6:p.find("@id@")] in o[o.find("@"):] : 
                                pdf.cell(-1, 10, "From %s library: " %o[:o.find("@")]  , ln=1)
                                err.append(o[o.find("@")+1:])
                                er=1
                        else:    
                                pdf.cell(-1, 10, "From %s library: " %p[p.find("@node@")+6:p.find("@id@")]  , ln=1)
                                er=2
                except:
                     er=3
                     pdf.cell(-1, 10, "From %s library: " %p[p.find("@node@")+6:p.find("@id@")]  , ln=1)
                if er == 0 :
                    pdf.cell(-1, 10, "From %s library: " %p[p.find("@node@")+6:p.find("@id@")]  , ln=1) 
                
                
                
                
                ############################################################
                #pdf.cell(-1, 10, "From %s library: " %p[p.find("@node@")+6:p.find("@id@")]  , ln=1)
                text = text + p[:p.find("@lineno@")] +", "
                n.append(p[p.find("@node@")+6:p.find("@id@")])
                
                try:
                    o= int(p[:p.find("@lineno@")])
                    ln = lines[o-1] 
                    
                    lnn=ln[ln.find(p[p.find("@node@")+6:p.find("@id@")])+len(p[p.find("@node@")+6:p.find("@id@")]):ln.find("(")]
                    if er == 1 :
                        for o in err:
                            if o in p :
                                lnn=o
                                
                    
                except:
                    print(" ")
            else:               
                text = text + p[:p.find("@lineno@")] +", "
                try:
                    o= int(p[:p.find("@lineno@")])
                    ln = lines[o-1] 
                    
                    lnn=ln[ln.find(p[p.find("@node@")+6:p.find("@id@")])+len(p[p.find("@node@")+6:p.find("@id@")]):ln.find("(")]
                    if er == 1 :
                        for o in err:
                            if o in p :
                                lnn=o
                except:
                    print(" ")
                
                
        pdf.set_x(40)        
        text = text[:len(text)-2] +";"
        pdf.cell(-1, 10, "%s() line: %s" %(lnn , text) ,ln=1)
        #print("%s"%text)
        
        
        
        
        """
        n = []
        text = " "
        pdf.set_x(30)
        pdf.cell(-1, 10, "Generic:"  , ln=1)
        Sinrepetidos.sort()
        for p in Sinrepetidos:
            
            
            if p[:p.find("@")] not in n:
                
                pdf.set_x(50)
                if text != " ":
                    text = text[:len(text)-2] +";"
                    pdf.cell(-1, 10, " line: %s" %text,ln=1 )
                text=" "
                pdf.set_x(40)
                pdf.cell(-1, 10, "%s: " %p[:p.find("@")]  , ln=1)
                text = text + p[p.find("@")+1:] +", "
                n.append(p[:p.find("@")])
                
            else:
                
                text = text + p[p.find("@")+1:] +", "
        
        text = text[:len(text)-2] +";" 
        
        pdf.set_x(50)        
        pdf.cell(-1, 10, " line: %s" %text ,ln=1)        
                         
        
        n = []
        text = " "
        pdf.set_x(30)
        pdf.cell(-1, 10, "With variable:"  , ln=1)
        Sinrepetidos_2.sort()
        for p in Sinrepetidos_2:
            
            
            if p[:p.find("@")] not in n:
                
                pdf.set_x(50)
                if text != " ":
                    text = text[:len(text)-2] +";"
                    pdf.cell(-1, 10, " line: %s" %text,ln=1 )
                text=" "
                pdf.set_x(40)
                pdf.cell(-1, 10, "%s: " %p[:p.find("@")]  , ln=1)
                text = text + p[p.find("@")+1:] +", "
                n.append(p[:p.find("@")])
                
            else:
                
                text = text + p[p.find("@")+1:] +", "
        
        text = text[:len(text)-2] +";" 
        
        pdf.set_x(50)        
        pdf.cell(-1, 10, " line: %s" %text ,ln=1)
        """
        GenericA = []
        GenericLA = []
        contGA = 0
        LibreriasA = []
        LibreriasLA = []
        contLA = 0
        VarA = []
        VarLA = []
        contVA = 0

        for a in range(len(CallsA)):
            punto = CallsA[a].find(".")
            #print("%s" %a)
            #print("_%s" %punto)
            
            
            if (punto == -1):
                if CallsA[a] in ImpA:
                    LibreriasA.append(CallsA[a])
                    LibreriasLA.append([])
                    LibreriasLA[contLA].append(CallsLA[a])
                    contLA += 1
                else:
                    if CallsA[a] not in GenericA:
                        GenericA.append(CallsA[a])
                        GenericLA.append([])
                        #print(CallsLA[a])
                        GenericLA[contGA].append(CallsLA[a])
                        contGA += 1
            else:
                z = len(CallsA[a])
                t = 0
                punto2 = CallsA[a].find(".", punto + 1)
                punto3 = CallsA[a].find(".", punto2 + 1)
                punto4 = CallsA[a].find(".", punto3 + 1)
                if punto2 != -1:
                    if punto3 != -1:
                        if punto4 != -1:
                            if CallsA[a] not in GenericA:
                                
                                
                                GenericA.append(CallsA[a][punto3 + 1:punto4])
                                GenericLA.append([])
                                GenericLA[contGA].append(CallsLA[a])
                                contGA += 1
                            t = 3
                        else:
                            if t == 3:
                                if CallsA[a] not in GenericA:
                                    
                                    GenericA.append(CallsA[a][punto3 + 1:len(CallsA[a])])
                                    GenericLA.append([])
                                    GenericLA[contGA].append(CallsLA[a])
                                    contGA += 1
                    else:
                        St = CallsA[a][0:punto3]
                else:
                    St = CallsA[a][0:z]
                   
                if St[0:punto] in ImpA:
                    LibreriasA.append(CallsA[a])
                    LibreriasLA.append([])
                    LibreriasLA[contLA].append(CallsLA[a])
                    contLA += 1
                elif St[0:punto] in VariablesA:
                    if St not in ImpA:
                        if St == 'r.text.replac':
                            St += 'e'
                        VarA.append(St)
                        VarLA.append([])
                        VarLA[contVA].append(CallsLA[a])
                        contVA += 1
                elif St[0:punto] in CallsA:
                    if St not in GenericA:
                        
                        GenericA.append(CallsA[a][punto3 + 1:len(CallsA[a])])
                        GenericLA.append([])
                        GenericLA[contGA].append(CallsLA[a])
                        contGA += 1
        
        F = 0
        
        for BG in range(len(VarA)):
            
            if VarA[BG][:VarA[BG].find('.')] not in defined_libraries :
                A = ''
                punto = VarA[BG].find(".")
                pdf.set_x(30)
                pdf.cell(-1, 10, "With variable %s:" %VarA[BG][0:punto] , ln=1)
                #print('De la Variable: ', VarA[BG][0:punto])
                algo = 0
                
                for Line in range(len(VarLA[BG])):
                    if algo == 0:
                        
                        A = A + str(VarLA[BG][algo]).strip("[]")
                    else:
                        print("%s" %str(VarLA[BG][algo]).strip("[]"))
                        A = A + ', ' + str(VarLA[BG][algo]).strip("[]")
                    algo += 1
                pdf.set_x(40)
                pdf.cell(-1, 10, '# %s() In Lines: %s' %(VarA[BG][punto:len(VarA[BG])], A )  , ln=1)  
                
                #print('     #', VarA[BG][punto:len(VarA[BG])] + '()', 'In Lines: ', A)
                
                
        pdf.set_x(30)
        pdf.cell(-1, 10, "Generic:"  , ln=1)
        
        for D in range(len(GenericA)):
           
            if "main" not in GenericA[D]:
                A = ''
                
                
                algo = 0
                for Line in range(len(GenericLA[D])):
                    #print("%s" %Line)
                    
                    if algo == 0:
                       
                        c=0
                        
                        er=False
                        while str(GenericLA[D]).strip("[]").find(",",c+1) != -1:
                            er = True
                            c=str(GenericLA[D]).strip("[]").find(",",c+1)
                       
                        if er : 
                            
                                
                            if str(GenericLA[D]).strip("[]")[c+2:] in str(GenericLA[D]).strip("[]")[:c]:
                                w = str(GenericLA[D]).strip("[]")[:c].split(", ")
                                w.sort()
                                
                                a=""
                                for m in w:
                                    a+=m+", "
                                A = A + a[:len(a)-2]
                            else:
                                w = str(GenericLA[D]).strip("[]").split(", ")
                                w.sort()
                                
                                a=""
                                for m in w:
                                    a+=m+", "
                                A = A + a[:len(a)-2]
                        else:
                            A = A + str(GenericLA[D]).strip("[]")
                            
                    else:
                        
                       A = A + ', ' + str(GenericLA[D]).strip("[]")
                            
                    algo += 1
                pdf.set_x(40)
                
                pdf.cell(-1, 10, '# %s() In Lines: %s' %(GenericA[D], A )  , ln=1)    
                         





        #################################################################       
        my_f.close()
        num_file=num_file+1
       
        copia = []
        
        
        defined_function=defined_function+len(copia_def)
        
        defined_lines=defined_lines+1+len(lines)
    except :       
        break
pdf.set_x(10)
pdf.set_font("Arial", size=20)
pdf.set_text_color(224, 165, 0)
pdf.cell(-1, 10, '3. Some statistics', ln=1)
pdf_titol.set_x(20)
pdf_titol.set_font("Arial", 'B' , size=20)
pdf_titol.cell(-1, 10, '3. Some statistics')
pdf_titol.set_x(-30)
pdf_titol.cell(-1, 10, '%d' %pdf.page_no() ,ln=1)
pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf_titol.cell(-1, 10, '' ,ln=1)
pdf_titol.set_x(10)
pdf.multi_cell(190, 10, 'The project has %s programs, with %s defined functions. The program define %s variables and import %s libraries (external libraries) on %s lines of python code.' %( num_prog ,defined_function ,len(defined_variable),len(defined_libraries),defined_lines))
  
pdf_titol.output("simple_demo_titol.pdf")
pdf.output("simple_demo.pdf")
merger = PdfFileMerger()
merger.append('simple_demo_titol.pdf')
merger.append('simple_demo.pdf')
merger.write("BG_SA_Scripting_Lab_2.pdf")
merger.close()
pdf.close()
pdf_titol.close()
os.remove("simple_demo_titol.pdf")
os.remove("simple_demo.pdf")
print("fin")
