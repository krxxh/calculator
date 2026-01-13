import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(expand=True, fill="both", padx=10, pady=20)
        
        # Input field
        input_field = tk.Entry(
            display_frame,
            font=font.Font(size=32, weight="bold"),
            textvariable=self.input_text,
            bd=0,
            bg="#2d2d2d",
            fg="#ffffff",
            justify="right",
            insertbackground="#ffffff"
        )
        input_field.pack(ipady=30, fill="both")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=(0, 10))
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '':
                    continue
                    
                # Button styling based on type
                if btn_text in ['C', '⌫']:
                    bg_color = "#ff6b6b"
                    fg_color = "#ffffff"
                elif btn_text in ['/', '*', '-', '+', '=', '%']:
                    bg_color = "#4ecdc4"
                    fg_color = "#ffffff"
                else:
                    bg_color = "#3d3d3d"
                    fg_color = "#ffffff"
                
                btn = tk.Button(
                    buttons_frame,
                    text=btn_text,
                    font=font.Font(size=20, weight="bold"),
                    bg=bg_color,
                    fg=fg_color,
                    bd=0,
                    activebackground=bg_color,
                    activeforeground=fg_color,
                    cursor="hand2",
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                
                # Make '0' button span 2 columns
                if btn_text == '0':
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                else:
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()