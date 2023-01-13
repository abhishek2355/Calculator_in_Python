import tkinter as tk

LABEL_BACKGROUND_COLOR = "#000000"
BUTTON_BACKGROUND_COLOR = "#333333"
TEXT_COLOR = "#FFFFFF"
FONT_TUPLE_CURRENT_LABLE = ("Comic Sans MS", 20, "bold")
FONT_TUPLE_TOTAL_LABLE = ("Comic Sans MS", 15, "bold")
FONT_TUPLE_BUTTON = ("Comic Sans MS", 13, "bold")


DIGIT_DICTIONARY = {
    7:(1,1), 8:(1,2), 9:(1,3),
    4:(2,1), 5:(2,2), 6:(2,3),
    1:(3,1), 2:(3,2), 3:(3,3),
    0:(4,1)
}

OPERATIONS = {
    "AC":(0,1), "DEL":(0, 3), "/":(0,4),
    "X":(1,4),
    "+":(2,4),
    "-":(3,4),
    ".":(4,3),
    "=":(4,4)
}

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_label_value = ""
        self.current_label_value = "0"

        self.display_label_frame = self.add_label_frame()
        self.display_buttons_frame = self.add_button_frame()

        self.total_label, self.current_label = self.add_current_label()

        self.buttons = self.create_buttons()

        self.display_buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.display_buttons_frame.rowconfigure(i, weight=1)
            self.display_buttons_frame.columnconfigure(i, weight=1)
        
        

    def run(self):
        self.window.mainloop()
    
    def add_label_frame(self):
        frame = tk.Frame(self.window, background=LABEL_BACKGROUND_COLOR, height=100)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_button_frame(self):
        frame = tk.Frame(self.window, background=BUTTON_BACKGROUND_COLOR, height=567)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_current_label(self):
        total_label = tk.Label(self.display_label_frame, background = LABEL_BACKGROUND_COLOR, anchor=tk.E, text=self.total_label_value, font=FONT_TUPLE_TOTAL_LABLE,foreground=TEXT_COLOR)
        total_label.pack(expand=True, fill="both")

        current_label = tk.Label(self.display_label_frame, background = LABEL_BACKGROUND_COLOR, anchor=tk.E, text=self.current_label_value, font=FONT_TUPLE_CURRENT_LABLE, foreground=TEXT_COLOR)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label
    
    def create_buttons(self):
        for digit, position in DIGIT_DICTIONARY.items():
            button = tk.Button(self.display_buttons_frame, text=str(digit), command= lambda x=digit: self.add_button_value(str(x)),bg=BUTTON_BACKGROUND_COLOR, foreground=TEXT_COLOR,font=FONT_TUPLE_BUTTON)
            if digit == 0:
                button.grid(row=position[0], column=position[1], sticky=tk.NSEW, columnspan=2)
            else:
                button.grid(row=position[0], column=position[1], sticky=tk.NSEW)
            
        
        for operation, position in OPERATIONS.items():
            if operation == "=":
                button = tk.Button(self.display_buttons_frame, text=operation, command= lambda x=operation: self.tap_equal(),bg=BUTTON_BACKGROUND_COLOR, foreground=TEXT_COLOR,font=FONT_TUPLE_BUTTON)
            elif operation == "AC":
                button = tk.Button(self.display_buttons_frame, text=operation, command= lambda x=operation: self.tap_AC(),bg=BUTTON_BACKGROUND_COLOR, foreground=TEXT_COLOR,font=FONT_TUPLE_BUTTON)
                button.grid(row=position[0], column=position[1], sticky=tk.NSEW, columnspan=2)
                continue
            elif operation == "DEL":
                button = tk.Button(self.display_buttons_frame, text=operation, command= lambda x=operation: self.tap_DEL(),bg=BUTTON_BACKGROUND_COLOR, foreground=TEXT_COLOR,font=FONT_TUPLE_BUTTON)
            else:
                button = tk.Button(self.display_buttons_frame, text=operation, command= lambda x=operation: self.add_operation_value(str(x)),bg=BUTTON_BACKGROUND_COLOR, foreground=TEXT_COLOR,font=FONT_TUPLE_BUTTON)
            button.grid(row=position[0], column=position[1], sticky=tk.NSEW)

    def add_button_value(self, value):
        self.total_label_value += value
        if(self.current_label_value == "0"):
            self.current_label_value = ""
        self.current_label_value += value
        self.update_current_label_value()
        self.update_total_label_value()
    
    def add_operation_value(self, value):
        self.total_label_value += value
        self.current_label_value = ""
        self.update_current_label_value()
        self.update_total_label_value()
    
    def update_total_label_value(self):
        self.total_label.configure(text=self.total_label_value)
    
    def update_current_label_value(self):
        self.current_label.configure(text=self.current_label_value)
    
    def tap_equal(self):
        self.total_label_value = self.total_label_value.replace("X", "*")
        result = eval(self.total_label_value)
        self.current_label_value = str(result)
        self.total_label_value = str(result)
        self.update_current_label_value()
        self.update_total_label_value()

    def tap_AC(self):
        self.current_label_value = "0"
        self.total_label_value = ""
        self.update_current_label_value()
        self.update_total_label_value()
    
    def tap_DEL(self):
        self.current_label_value = self.current_label_value[:len(self.current_label_value)-1]
        self.total_label_value = self.total_label_value[:len(self.total_label_value)-1]
        self.update_current_label_value()
        self.update_total_label_value()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()