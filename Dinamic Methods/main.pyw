from PySide6.QtWidgets import *
import sys 
from form import *
from PySide6 import *
import sympy 
from sympy import*

from tkinter import *
from tkinter import messagebox


import math

class parcial(QMainWindow): # a esto le puedo camiar el nombre de la clase nada más
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() #permitir utilizar todos los objetos del form
        self.ui.setupUi(self)
        #Botones para cada metodo 
        self.ui.btn_resolverBi.clicked.connect(self.Biseccion)
        self.ui.btn_resolver_regula.clicked.connect(self.regula_falsi)
        self.ui.btn_resolverNR.clicked.connect(self.NR) 
        self.ui.btn_resolver_Se.clicked.connect(self.Secante)
        self.ui.btn_resolver_SeMod.clicked.connect(self.SecanteMod)
        #Btones extras para vaciar todas las cajas de texto
        self.ui.btn_borrar.clicked.connect(self.Borrar)
        self.ui.btn_salir.clicked.connect(self.Salir)
    

    def Biseccion(self):
        #usar simbolos X
        x = sympy.symbols('x')
        #Ingreso de la ecuacion dinamica
        ecuacion = (self.ui.txt_fxBi.text())
        #ingreso de valores A y B
        a = float(self.ui.txt_aBi.text())
        b = float(self.ui.txt_bBI.text())
        #Evitar que el valor A sea mayor que B y si no mandar una
        #advetenca y limpiar los contenedores de A y B
        while a > b:
            messagebox.showinfo('Atencion','El valor de A no puede ser mayor al de B')
            self.ui.txt_aBi.clear()
            self.ui.txt_bBI.clear()
            a = float(self.ui.txt_aBi.text())
            b = float(self.ui.txt_bBI.text())
        #Ingreso de tolerancia en forma de porcentaje y la iteracion
        tolerancia = float(self.ui.txt_tolBi.text()) * 100
        iteracion = float(self.ui.txt_iterBi.text())
        #Valor del error y la iteracion estaticos
        error = 100
        iter = 0
        #Iniciar el while donde se comprueva la repeticion del proceso
        #hasta que el error se amyor a la tolerancia o la iteracion estatica
        #sea mayor que la iteracion introducida manualmente
        while abs(error) > tolerancia or iter>iteracion:
            #redondear y hacer los valores de fa fb y fm
            m=round((a+b)/2, 4)
            fa = round(sympy.sympify(ecuacion).subs(x,a), 4)
            fb = round(sympy.sympify(ecuacion).subs(x,b), 4)
            fm = round(sympy.sympify(ecuacion).subs(x,m), 4)
            #el error que mais pois meu hermao
            error=round(((abs(b-a)/2)*100), 4)

            if fa*fm < 0:
                b=m
            else:
                a=m

            iter += 1
            #mostrar resultados en las cajas de texto
            self.ui.txt_raizBi_res.setText(str(m))
            self.ui.txt_iterBi_res_.setText(str(iter))
            self.ui.txt_errorBi_res.setText(str(error))
   
    def regula_falsi(self):
        #usar simbolos X
        x = sympy.symbols('x')
        #Ingreso de la ecuacion dinamica
        ecuacion = (self.ui.txt_funcionRe.text())
        a = float(self.ui.txt_aRe.text())
        b = float(self.ui.txt_bRe.text())
        #Evitar que el valor A sea mayor que B y si no mandar una
        #advetenca y limpiar los contenedores de A y B
        while a > b:
            messagebox.showinfo('Atencion','El valor de A no puede ser mayor al de B')
            self.ui.txt_aRe.clear()
            self.ui.txt_bRe.clear()
            a = float(self.ui.txt_aRe.text())
            b = float(self.ui.txt_bRe.text())
        tolerancia = float(self.ui.txt_toleranciaRe.text()) * 100
        iteracion = int(self.ui.txt_iteracionesRe.text())
        
        #inicio de valores estaticos
        error=100
        iter=0
        xf = 100
        #Fa y Fb se realizan afuera del while para no generar errores
        #como congelamientomde la app o de errores de ecuacion
        fa = round(sympy.sympify(ecuacion).subs(x,a), 4)
        fb = round(sympy.sympify(ecuacion).subs(x,b), 4)
        #Iniciar el while donde se comprueva la repeticion del proceso
        #hasta que el error se amyor a la tolerancia o la iteracion estatica
        #sea mayor que la iteracion introducida manualmente
        while error > tolerancia or iter > iteracion:
            #el paso 1 daba error asi que se omitio, consistia en iniciar
            #xf otra vez pero en modo grafico congela la aplicacion
            #Paso 2
            xi = round(((a*fb)-(b*fa)) / (fb - fa), 4)
            #Paso 3
            fxi = round(sympy.sympify(ecuacion).subs(x,xi), 4)
            #Paso 4
            if iter > 1: 
                error  = round((abs(xi - xf) / xi) * 100, 2)
    
            xf = xi
            if fa*fxi < 0:
                b=xi
            else:
                a=xi
            #iter=iter+1
            iter += 1

        self.ui.txt_raizrefa_res.setText(str(xi))
        self.ui.txt_iterarefa_res.setText(str(iter-1))
        self.ui.txt_errorrefa_res.setText(str(error)) 
  
    def NR(self):

        iter = 0
        error = 1

        x = sympy.symbols("x")
        funcion  = (self.ui.txt_funcionNR.text())
        xi = float(self.ui.txtAproxinicialNR.text())
        tol = float(self.ui.txt_toleranciaNR.text())
        iteracion = int(self.ui.txt_iteracionNR.text())
        derivada = diff(funcion, x)

        while error > tol or iter> iteracion :
            y = round(sympy.sympify(funcion).subs(x,xi),4) #la función normal
            yprima= round(sympy.sympify(derivada).subs(x,xi),4)#la función derivada
            xii=round(xi-(y/yprima),4)
            error= round(abs((xii-xi)/xii),4)
            xi=xii
            iter+=1

        self.ui.txt_raizNR_res.setText(str(xii))
        self.ui.txt_iteraNR_res.setText(str(iter))
        self.ui.txt_errorNR_res.setText(str(error))

    def Secante (self):
        iter = 1
        error = 100

        x = sympy.symbols("x")
        funcion = (self.ui.txt_fxSe.text())
        xo = float(self.ui.txt_xoSe.text())
        xi = float(self.ui.txt_xiSe.text())
        tol = float(self.ui.txt_tolSe.text())*100
        iteracion = int(self.ui.txt_iterSe.text())

        while error>tol or iter>iteracion:
    
            fxo = round(sympy.sympify(funcion).subs(x,xo), 4)
            fxi = round(sympy.sympify(funcion).subs(x,xi), 4)
            x2 = round((xi)-(fxi*(xo-xi)/(fxo-fxi)),4) 
            error = round(abs((x2-xi)/x2)*100, 2)   
            xo = xi
            xi = x2
            iter+=1

        self.ui.txt_raizSe_res.setText(str(x2))
        self.ui.txt_iteraSe_res.setText(str(iter-1))
        self.ui.txt_errorSe_res.setText(str(error))

    def SecanteMod (self):
        ite=1
        error=100

        x=sympy.symbols('x')
        funcion = (self.ui.txt_fxSeMod.text())
        xi = float(self.ui.txt_xiSeMod.text())
        sxi = float(self.ui.txt_SxiSeMod.text())
        tol = float(self.ui.txt_tolSeMod.text())*100
        iteracion = int(self.ui.txt_iterSeMod.text())

        while error>tol or ite>iteracion:
    
            fxi = round(sympy.sympify(funcion).subs(x,xi), 4)
            sxi_more_xi = round(sxi+xi,4)
            FbySxi_More_xi = round(sympy.sympify(funcion).subs(x,sxi_more_xi), 4)
            x1 = round((xi)-(sxi*fxi)/(FbySxi_More_xi-fxi),4) 
            error = round(abs((x1-xi)/x1)*100, 2)
            xi = x1
            ite+=1

        self.ui.txt_raizSeMod_res.setText(str(x1))
        self.ui.txt_iteraSeMod_res.setText(str(ite-1))
        self.ui.txt_errorSeMod_res.setText(str(error))
    
    def Borrar(self):
        #Biseccion
        self.ui.txt_fxBi.clear()
        self.ui.txt_aBi.clear()
        self.ui.txt_bBI.clear()
        self.ui.txt_tolBi.clear()
        self.ui.txt_iterBi.clear()
        self.ui.txt_raizBi_res.clear()
        self.ui.txt_iterBi_res_.clear()
        self.ui.txt_errorBi_res.clear()
        #Regula Falsi
        self.ui.txt_funcionRe.clear()
        self.ui.txt_aRe.clear()
        self.ui.txt_bRe.clear()
        self.ui.txt_toleranciaRe.clear()
        self.ui.txt_iteracionesRe.clear()
        self.ui.txt_raizrefa_res.clear()
        self.ui.txt_iterarefa_res.clear()
        self.ui.txt_errorrefa_res.clear()
        #Newton Rapshon
        self.ui.txt_funcionNR.clear()
        self.ui.txtAproxinicialNR.clear()
        self.ui.txt_toleranciaNR.clear()
        self.ui.txt_iteracionNR.clear()
        self.ui.txt_raizNR_res.clear()
        self.ui.txt_iteraNR_res.clear
        self.ui.txt_errorNR_res.clear()
        #Secante
        self.ui.txt_fxSe.clear()
        self.ui.txt_xoSe.clear()
        self.ui.txt_xiSe.clear()
        self.ui.txt_tolSe.clear()
        self.ui.txt_iterSe.clear()
        self.ui.txt_raizSe_res.clear()
        self.ui.txt_iteraSe_res.clear()
        self.ui.txt_errorSe_res.clear()
        #Secante Modificada
        self.ui.txt_fxSeMod.clear()
        self.ui.txt_xiSeMod.clear()
        self.ui.txt_SxiSeMod.clear()
        self.ui.txt_tolSeMod.clear()
        self.ui.txt_iterSeMod.clear()
        self.ui.txt_raizSeMod_res.clear()
        self.ui.txt_iteraSeMod_res.clear()
        self.ui.txt_errorSeMod_res.clear()
    
    def Salir(self):
        self.close()


      
if __name__=="__main__":
    app=QApplication(sys.argv)
    myapp=parcial()
    myapp.show()
    sys.exit(app.exec_())

    
