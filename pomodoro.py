#!/usr/bin/python
# -*- coding: utf-8 -*-
#     Pomodoro
#     Developed by Julian Camilo Marin Sanchez - marin.julian@gmail.com - @juliancms
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
import Tkinter, ttk, tkMessageBox

class pomodoro(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        self.intervalo = 1
        self.minutos = 25
        self.segundos = 0
        self.b_minutos = 5
        self.b_segundos = 0
        self.reset = False
        self.stop = False
        self.label_h1 = Tkinter.Label(self, text="POMODORO", font="Arial 15 bold")
        self.label_h1.grid(column=0,row=0,columnspan=2,padx=60,pady=20)
        self.label_contador = Tkinter.Label(self, text="0:00", font="Arial 15")
        self.label_contador.grid(column=0,row=1,columnspan=2)
        self.label_titulo = Tkinter.Label(self, text="Presiona 'INICIAR' para comenzar")
        self.label_titulo.grid(column=0,row=2,columnspan=2,pady=5)
        self.button_start = Tkinter.Button(self,text="INICIAR", command= self.iniciar, width="10")
        self.button_start.grid(column=0,row=3,pady=10,sticky="E")
        self.button_stop = Tkinter.Button(self,text="PARAR", command= self.parar, width="10")
        self.button_stop.grid(column=1,row=3,pady=10,sticky="W")


    def countdown(self, intervalo, minutos, segundos):
        if(self.stop == True):
            self.button_stop = Tkinter.Button(self,text="REANUDAR", command= self.reanudar, width="10")
            self.button_stop.grid(column=1,row=3,pady=10,sticky="W")
            self.r_segundos = segundos
            self.r_minutos = minutos
            self.r_intervalo = intervalo
            self.r_tipo = "countdown"
            return
        self.label_titulo.destroy()
        self.label_contador.destroy()
        if(self.reset == True):
            self.reset = False
            segundos = 0
            minutos = 25
            self.intervalo = 1
        if segundos == 0:
            if minutos == 0:
                if(intervalo % 4 == 0):
                    self.b_minutos = 15
                else:
                    self.b_minutos = 5
                self.breakdown(self.intervalo, self.b_minutos, self.b_segundos)
                self.descanso()
                return
            segundos = 59
            minutos = minutos-1
        self.label_titulo = Tkinter.Label(self, text="Intervalo " + str(intervalo))
        self.label_titulo.grid(column=0,row=2,columnspan=2,pady=5)
        self.label_contador = Tkinter.Label(self, text=str(minutos).zfill(2) + ":" + str(segundos).zfill(2), font="Arial 15")
        self.label_contador.grid(column=0,row=1,columnspan=2)
        self.after(1000, self.countdown, intervalo, minutos, segundos-1)
    def breakdown(self, intervalo, minutos, segundos):
        if(self.stop == True):
            self.button_stop = Tkinter.Button(self,text="REANUDAR", command= self.reanudar, width="10")
            self.button_stop.grid(column=1,row=3,pady=10,sticky="W")
            self.r_segundos = segundos
            self.r_minutos = minutos
            self.r_intervalo = intervalo
            self.r_tipo = "breakdown"
            return
        self.label_titulo.destroy()
        self.label_contador.destroy()
        if(self.reset == True):
            self.label_titulo.destroy()
            self.label_contador.destroy()
            self.countdown(self.intervalo, self.minutos, self.segundos)
            return
        if segundos == 0:
            if minutos == 0:
                self.intervalo = self.intervalo + 1
                self.label_titulo.destroy()
                self.label_contador.destroy()
                self.countdown(self.intervalo, self.minutos, self.segundos)
                self.fin_descanso()
                return
            segundos = 59
            minutos = minutos-1
        self.label_titulo = Tkinter.Label(self, text="Descanso Intervalo " + str(intervalo))
        self.label_titulo.grid(column=0,row=2,columnspan=2,pady=5)
        self.label_contador = Tkinter.Label(self, text=str(minutos).zfill(2) + ":" + str(segundos).zfill(2), font="Arial 15")
        self.label_contador.grid(column=0,row=1,columnspan=2)
        self.after(1000, self.breakdown, intervalo, minutos, segundos-1)
    def iniciar(self):
        self.button_start.destroy()
        self.button_start = Tkinter.Button(self,text="REINICIAR", command= self.reiniciar, width="10")
        self.button_start.grid(column=0,row=3,pady=10,sticky="E")
        self.countdown(self.intervalo, self.minutos, self.segundos)
    def reiniciar(self):
        self.reset = True
        if(self.stop == True):
            self.stop = False
            self.countdown(1, self.minutos, self.segundos)
    def parar(self):
        self.stop = True
        self.button_stop.destroy()
    def reanudar(self):
        self.stop = False
        self.button_stop.destroy()
        self.button_stop = Tkinter.Button(self,text="PARAR", command= self.parar, width="10")
        self.button_stop.grid(column=1,row=3,pady=10,sticky="W")
        if(self.r_tipo == "countdown"):
            self.countdown(self.r_intervalo, self.r_minutos, self.r_segundos)
        else:
            self.breakdown(self.r_intervalo, self.r_minutos, self.r_segundos)
    def descanso(self):
        tkMessageBox.showinfo("Descanso", "¡Es momento de un descanso :D!")
    def fin_descanso(self):
        tkMessageBox.showinfo("Intervalo", "Terminó el descanso ¡A trabajar =D!")
if __name__ == "__main__":
    app = pomodoro(None)
    app.title('Pomodoro')
    app.mainloop()
