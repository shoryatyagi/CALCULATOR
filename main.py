from tkinter import *

LARGE_FONT_STYLE = ("Arial",40,"bold")
SMALL_FONT_STYLE = ("Arial",16)
DIGITS_FONT_STYLE = ("Arial",24,"bold")
DEFAULT_FONT_STYLE = ("Arial",20)

OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = '#CECECE'
LABELS_COLOR = "black"

class Calculator():
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False,False)

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label,self.label = self.create_display_labels()

        self.digits = {            
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operations = {"/":"\u00F7", "*":"\u00D7",  "-":"-", "+":"+"}

        self.button_frame = self.create_button_frame()
        
        self.button_frame.rowconfigure(0,weight=1)

        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def run(self):
        self.root.mainloop()

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression,anchor=E,bg=LIGHT_GRAY,
                            fg=LABELS_COLOR,font=SMALL_FONT_STYLE,padx=24)
        total_label.pack(expand=TRUE,fill=BOTH) 

        label = Label(self.display_frame, text=self.total_expression,anchor=E,bg=LIGHT_GRAY,
                            fg=LABELS_COLOR,font=LARGE_FONT_STYLE,padx=24)
        label.pack(expand=TRUE,fill=BOTH)

        return total_label,label
   
    def create_display_frame(self):
        frame = Frame(self.root,height=380,width=400,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill=BOTH)
        return frame
    
    def add_to_expression(self,value):
        self.current_expression +=str(value)
        self.update_label()
    
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = Button(self.button_frame,text=str(digit),bg=WHITE,fg=LABELS_COLOR,font=DIGITS_FONT_STYLE,borderwidth=0,
                            command= lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=NSEW)

    def append_opeator(self,operator):
        self.current_expression +=operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            button = Button(self.button_frame,text=symbol,bg=OFF_WHITE,fg=LABELS_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=lambda x=operator: self.append_opeator(x))
            button.grid(row=i,column=4,sticky=NSEW)
            i+=1
    def clear(self):
        self.current_expression =""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = Button(self.button_frame,text="C",bg=OFF_WHITE,fg=LABELS_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,sticky=NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = Button(self.button_frame,text="x\u00b2",bg=OFF_WHITE,fg=LABELS_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.square)
        button.grid(row=0,column=2,sticky=NSEW)

    def square_root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
        
    def create_sqrt_button(self):
        button = Button(self.button_frame,text="\u221a",bg=OFF_WHITE,fg=LABELS_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.square_root)
        button.grid(row=0,column=3,sticky=NSEW)

    def create_equals_button(self):
        button = Button(self.button_frame,text="=",bg=LIGHT_BLUE,fg=LABELS_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=NSEW)

    def create_button_frame(self):
        frame = Frame(self.root)
        frame.pack(expand=True,fill=BOTH)
        return frame
    
    def update_total_label(self):
        expression = self.total_expression
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator,f'{symbol}')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:5])
    


if __name__ =='__main__':
    app = Calculator()
    app.run()
