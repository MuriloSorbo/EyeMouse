import tkinter as tk
import program
import calibrate

window = tk.Tk()
window.geometry("400x180")

text = tk.Label(window, text='Controle de Mouse com Rosto. Selecione uma das opções abaixo')
btnRun = tk.Button(window, text="Iniciar Programa")
btnCalibration = tk.Button(window, text="Calibrar")

window.title('FabLab Sesi Sorocaba - Controle Mouse')
text.config(pady=20)
btnRun.config(width=40, height=2, command=program.Run)
btnCalibration.config(width=40, height=2, command=calibrate.Run)

text.pack()
btnRun.pack()
btnCalibration.pack()

window.mainloop()