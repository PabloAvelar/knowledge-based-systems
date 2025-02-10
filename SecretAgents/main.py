import customtkinter as ctk
import threading
from secretagents import SecretAgents


class InputFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.pack(ipadx=10, ipady=20, fill='x', side='bottom')
        self.create_widgets()

    def create_widgets(self):
        tomas_value = ctk.StringVar()
        tomas_france_check = ctk.CTkCheckBox(self, text='T/F', variable=tomas_value, onvalue="T/F", offvalue="off")
        tomas_france_check.pack(side='left', anchor='center', expand=True)

        tomas_spain_check = ctk.CTkCheckBox(self, text='T/ES', variable=tomas_value, onvalue="T/ES", offvalue="off")
        tomas_spain_check.pack(side='left', anchor='center', expand=True)

        tomas_egypt_check = ctk.CTkCheckBox(self, text='T/EG', variable=tomas_value, onvalue="T/EG", offvalue="off")
        tomas_egypt_check.pack(side='left', anchor='center', expand=True)

        tomas_japan_check = ctk.CTkCheckBox(self, text='T/J', variable=tomas_value, onvalue="T/J", offvalue="off")
        tomas_japan_check.pack(side='left', anchor='center', expand=True)

        button_submit = ctk.CTkButton(self, text='Submit', command=lambda: self.submit(tomas_value))
        button_submit.pack(side='right', anchor='center', expand=True)

    def submit(self, tomas_value):
        # Searching the rule that matches the user input
        user_rule = None
        for rule in self.root.rules:
            if tomas_value.get() in rule:
                user_rule = rule
                break

        # Running the process in a separate thread and showing the result
        self.root.canvas.create_widgets(user_rule)

        threading.Thread(target=self.root.run_process, args=(user_rule, self.root.canvas)).start()


class Canvas(ctk.CTkCanvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.delete("all")

    def create_widgets(self, main_rule):
        # Delete all widgets in the canvas
        self.clear_frame()

        # Main rule
        main_rule_text = list(main_rule.keys())[0]
        main_rule_consequent_text = list(main_rule.values())[0]

        (ctk.CTkButton(self, text=f"{main_rule_text}", width=50, height=50, corner_radius=100,
                       bg_color='transparent', fg_color='#a4d8ff', text_color="#000", border_width=2)
         .place(x=100, y=100))

        # Draw a line to connect nodes
        self.create_line(150, 125, 300, 125, fill='black', width=2)

        (
            ctk.CTkButton(self, text=f"{main_rule_consequent_text}", width=50, height=50, corner_radius=100,
                          bg_color='transparent', fg_color='#a4d8ff', text_color="#000", border_width=2)
            .place(x=300, y=100))


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, text):
        super().__init__()
        self.geometry("400x180")
        self.title("Resultado final")

        self.label = ctk.CTkLabel(self, text=text, font=("Arial", 24))
        self.label.pack(padx=20, pady=50)

        self.focus_force()
        self.grab_set()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Secret Agents')
        self.geometry('800x600')

        self.rules = [
            {'T/F': 'L/-ES'},  # Rule 1
            {'T/-F': 'L/ES'},  # Rule 2
            {'T/ES': 'A/-F'},  # Rule 3
            {'T/-ES': 'A/F'},  # Rule 4
            {'T/EG': 'C/-EG'},  # Rule 5
            {'T/-EG': 'C/EG'},  # Rule 6
            {'T/J': 'C/-F'},  # Rule 7
            {'T/-J': 'C/F'},  # Rule 8
        ]

        input_frame = InputFrame(self, fg_color='white')
        self.canvas = Canvas(self, bg='#eee')
        self.canvas.pack(ipadx=10, ipady=10, fill='both', expand=True)

    def run_process(self, user_rule, canvas):
        print("User rule: ", user_rule)
        secret_agents = SecretAgents(self.rules, canvas, ctk.CTkButton, ctk.CTkToplevel)
        result = secret_agents.chaining_rules(user_rule)

        message = f"La regla {list(user_rule.keys())[0]} -> {list(user_rule.values())[0]} es {result}"
        TopLevelWindow(text=message)

        print("Result: ", result)


if __name__ == '__main__':
    app = App()
    app.mainloop()
