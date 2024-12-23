import tkinter as tk
import math

class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Standard_Ops(self, op):
        self.current += str(op)
        ent_field.delete(0, tk.END)
        ent_field.insert(tk.END, self.current)

    def Evaluate(self):
        try:
            self.current = str(eval(self.current))
            ent_field.delete(0, tk.END)
            ent_field.insert(tk.END, self.current)
        except Exception as e:
            ent_field.delete(0, tk.END)
            ent_field.insert(tk.END, "Error")

    def Clear(self):
        self.current = ''
        ent_field.delete(0, tk.END)

    def Factorial(self):
        try:
            self.current = math.factorial(int(ent_field.get()))
            ent_field.delete(0, tk.END)
            ent_field.insert(tk.END, self.current)
        except Exception:
            ent_field.delete(0, tk.END)
            ent_field.insert(tk.END, "Error")

if __name__ == '__main__':
    sc_app = SC_Calculator()

    FONT = ('Arial', 14)

    root = tk.Tk()
    root.title("Simple Scientific Calculator")
    root.geometry("400x400")
    root.configure(bg='white')

    ent_field = tk.Entry(root, font=FONT, width=20, justify='right', bg='#f0f0f0', fg='black')
    ent_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

    button_config = {
        'font': FONT, 'width': 6, 'height': 2, 'bg': '#e0e0e0', 'fg': 'black'
    }

    btn_clear = tk.Button(root, text='C', command=sc_app.Clear, **button_config)
    btn_clear.grid(row=1, column=0, padx=5, pady=5)

    btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'), **button_config)
    btn_div.grid(row=1, column=1, padx=5, pady=5)

    btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'), **button_config)
    btn_mul.grid(row=1, column=2, padx=5, pady=5)

    btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'), **button_config)
    btn_sub.grid(row=1, column=3, padx=5, pady=5)

    btn_7 = tk.Button(root, text='7', command=lambda: sc_app.Standard_Ops(7), **button_config)
    btn_7.grid(row=2, column=0, padx=5, pady=5)

    btn_8 = tk.Button(root, text='8', command=lambda: sc_app.Standard_Ops(8), **button_config)
    btn_8.grid(row=2, column=1, padx=5, pady=5)

    btn_9 = tk.Button(root, text='9', command=lambda: sc_app.Standard_Ops(9), **button_config)
    btn_9.grid(row=2, column=2, padx=5, pady=5)

    btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'), **button_config)
    btn_add.grid(row=2, column=3, padx=5, pady=5)

    btn_4 = tk.Button(root, text='4', command=lambda: sc_app.Standard_Ops(4), **button_config)
    btn_4.grid(row=3, column=0, padx=5, pady=5)

    btn_5 = tk.Button(root, text='5', command=lambda: sc_app.Standard_Ops(5), **button_config)
    btn_5.grid(row=3, column=1, padx=5, pady=5)

    btn_6 = tk.Button(root, text='6', command=lambda: sc_app.Standard_Ops(6), **button_config)
    btn_6.grid(row=3, column=2, padx=5, pady=5)

    btn_fact = tk.Button(root, text='!', command=sc_app.Factorial, **button_config)
    btn_fact.grid(row=3, column=3, padx=5, pady=5)

    btn_1 = tk.Button(root, text='1', command=lambda: sc_app.Standard_Ops(1), **button_config)
    btn_1.grid(row=4, column=0, padx=5, pady=5)

    btn_2 = tk.Button(root, text='2', command=lambda: sc_app.Standard_Ops(2), **button_config)
    btn_2.grid(row=4, column=1, padx=5, pady=5)

    btn_3 = tk.Button(root, text='3', command=lambda: sc_app.Standard_Ops(3), **button_config)
    btn_3.grid(row=4, column=2, padx=5, pady=5)

    btn_equal = tk.Button(root, text='=', command=sc_app.Evaluate, **button_config)
    btn_equal.grid(row=4, column=3, padx=5, pady=5)

    btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Standard_Ops(0), **button_config)
    btn_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='we')

    btn_dot = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'), **button_config)
    btn_dot.grid(row=5, column=2, padx=5, pady=5)

    btn_exp = tk.Button(root, text='^', command=lambda: sc_app.Standard_Ops('**'), **button_config)
    btn_exp.grid(row=5, column=3, padx=5, pady=5)

    root.mainloop()
