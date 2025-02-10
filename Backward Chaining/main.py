import customtkinter as ctk
from inferenceengine import InferenceEngine
from threading import Thread


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, root, text):
        super().__init__(root)
        self.geometry("300x180")
        self.title("Resultado final")

        self.label = ctk.CTkLabel(self, text=text, font=("Arial", 24))
        self.label.pack(padx=20, pady=50)


class UserInput(ctk.CTkInputDialog):
    def __init__(self, text):
        super().__init__(text=text, title='Hecho desconocido')


class Object(ctk.CTkButton):
    def __init__(self, root, size, color, text, text_color):
        super().__init__(master=root, width=size, height=size, text=text, font=('Arial', 24), text_color=text_color,
                         fg_color=color, bg_color='white', border_color='black', border_width=3, corner_radius=100,
                         hover_color=color)


class Canvas(ctk.CTkCanvas):
    def __init__(self, root, facts, rules, goal):
        super().__init__(master=root, width=800, height=600, bg='white')
        self.objects = {}
        self.root = root
        self.create_tree()

        # Marking main goal
        self.objects[goal].configure(border_width=4, border_color='yellow')

        # Marking known facts
        for fact, value in facts.items():
            print(fact, value)
            if value:
                self.objects[fact].configure(fg_color='green')
            else:
                self.objects[fact].configure(fg_color='red')

        # self.objects[goal].configure(fg_color='red')

        # Running inference engine

        goal_label_txt = f'Objetivo principal: {goal}'
        ctk.CTkLabel(self, text=goal_label_txt, font=("Arial", 16, "bold")).place(x=630, y=480)

        start_button = ctk.CTkButton(self, text='Comenzar', font=("Arial", 16),
                                     command=lambda: self.start_engine(rules, facts, goal))

        start_button.place(x=650, y=550)

    def start_engine(self, rules, facts, goal):
        engine = InferenceEngine(rules, facts, self.objects, UserInput)
        inference_thread = Thread(target=self.run_inference_engine, args=(engine, goal,))
        inference_thread.start()

    def run_inference_engine(self, engine, goal):
        result = engine.backward_chaining(goal)
        popup_text = f'¡El valor de {goal} es {result}!'
        TopLevelWindow(self.root, text=popup_text)

    def widget_pos(self, widget):
        self.update_idletasks()
        return [widget.winfo_x(), widget.winfo_y()]

    def create_tree(self):
        size = 50

        # Level 4
        h_space = size
        a = Object(self, size=size, color='white', text='A', text_color='black')
        a.place(x=5, y=10)
        h_space += 20
        b = Object(self, size=size, color='white', text='B', text_color='black')
        b.place(x=5, y=h_space)

        h_space += 50 + size
        d = Object(self, size=size, color='white', text='D', text_color='black')
        d.place(x=5, y=h_space)
        h_space += 20 + size
        e = Object(self, size=size, color='white', text='E', text_color='black')
        e.place(x=5, y=h_space)
        h_space += 20 + size
        f = Object(self, size=size, color='white', text='F', text_color='black')
        f.place(x=5, y=h_space)

        h_space += 50 + size
        h = Object(self, size=size, color='white', text='H', text_color='black')
        h.place(x=5, y=h_space)
        h_space += 20 + size
        i = Object(self, size=size, color='white', text=' I ', text_color='black')
        i.place(x=5, y=h_space)

        # Level 3
        h_space = size
        c = Object(self, size=size, color='white', text='C', text_color='black')
        c.place(x=size + 100, y=35)

        # Drawing lines
        self.create_line(
            (self.widget_pos(a)[0], self.widget_pos(a)[1], self.widget_pos(c)[0], self.widget_pos(c)[1] + 25), width=4,
            fill='black')
        self.create_line(
            (self.widget_pos(b)[0], self.widget_pos(b)[1] + 25, self.widget_pos(c)[0], self.widget_pos(c)[1] + 25),
            width=4, fill='black')

        h_space += 140 + size
        g = Object(self, size=size, color='white', text='G', text_color='black')
        g.place(x=size + 100, y=h_space)

        # Drawing lines
        self.create_line(
            (self.widget_pos(d)[0], self.widget_pos(d)[1], self.widget_pos(g)[0], self.widget_pos(g)[1] + 25), width=4,
            fill='black')
        self.create_line(
            (self.widget_pos(e)[0], self.widget_pos(e)[1] + 25, self.widget_pos(g)[0], self.widget_pos(g)[1] + 25),
            width=4, fill='black')
        self.create_line(
            (self.widget_pos(f)[0], self.widget_pos(f)[1] + 50, self.widget_pos(g)[0], self.widget_pos(g)[1] + 25),
            width=4, fill='black')

        h_space += 140 + size
        j = Object(self, size=size, color='white', text='J', text_color='black')
        j.place(x=size + 100, y=h_space)

        # Drawing lines
        self.create_line(
            (self.widget_pos(h)[0], self.widget_pos(h)[1], self.widget_pos(j)[0], self.widget_pos(j)[1] + 25), width=4,
            fill='black')
        self.create_line(
            (self.widget_pos(i)[0], self.widget_pos(i)[1] + 25, self.widget_pos(j)[0], self.widget_pos(j)[1] + 25),
            width=4, fill='black')

        # Level 2
        h_space = size
        k = Object(self, size=size, color='white', text='K', text_color='black')
        k.place(x=size + 300, y=145)

        # Drawing lines
        self.create_line(
            (self.widget_pos(c)[0], self.widget_pos(c)[1], self.widget_pos(k)[0], self.widget_pos(k)[1] + 25),
            width=4, fill='black', dash='1')

        self.create_line(
            (self.widget_pos(g)[0], self.widget_pos(g)[1] + 50, self.widget_pos(k)[0], self.widget_pos(k)[1] + 25),
            width=4, fill='black', dash='1')

        h_space += 220 + size
        l = Object(self, size=size, color='white', text='L', text_color='black')
        l.place(x=size + 300, y=h_space)

        # Drawing lines
        self.create_line(
            (self.widget_pos(g)[0], self.widget_pos(g)[1], self.widget_pos(l)[0], self.widget_pos(l)[1] + 25),
            width=4, fill='black')

        self.create_line(
            (self.widget_pos(j)[0], self.widget_pos(j)[1] + 50, self.widget_pos(l)[0], self.widget_pos(l)[1] + 25),
            width=4, fill='black')

        # Level 1
        h_space = size
        m = Object(self, size=size, color='white', text='M', text_color='black')
        m.place(x=size + 500, y=225)

        # Drawing lines
        self.create_line(
            (self.widget_pos(k)[0], self.widget_pos(k)[1], self.widget_pos(m)[0], self.widget_pos(m)[1] + 25),
            width=4, fill='black')

        self.create_line(
            (self.widget_pos(l)[0], self.widget_pos(l)[1] + 50, self.widget_pos(m)[0], self.widget_pos(m)[1] + 25),
            width=4, fill='black')

        self.objects['A'] = a
        self.objects['B'] = b
        self.objects['C'] = c
        self.objects['D'] = d
        self.objects['E'] = e
        self.objects['F'] = f
        self.objects['G'] = g
        self.objects['H'] = h
        self.objects['I'] = i
        self.objects['J'] = j
        self.objects['K'] = k
        self.objects['L'] = l
        self.objects['M'] = m

        # App.objects['M'].configure(fg_color='red')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title("Motor de inferencia")
        self.resizable(None, None)

        self.facts = {
            "D": True,
            "F": True,
            "E": True,
            "L": True,
        }

        self.rules = [
            {"premise": ["A", "B"], "conclusion": "C", "operator": 'and'},  # Rule 1
            {"premise": ["D", "E", "F"], "conclusion": "G", "operator": 'and'},  # Rule 2
            {"premise": ["H", "I"], "conclusion": "J", "operator": 'and'},  # Rule 3
            {"premise": ["C", "G"], "conclusion": "K", "operator": 'or'},  # Rule 4
            {"premise": ["G", "J"], "conclusion": "L", "operator": 'and'},  # Rule 5
            {"premise": ["K", "L"], "conclusion": "M", "operator": 'and'},  # Rule 6
        ]

        self.goal = 'M'

        self.create_canvas()

    def create_canvas(self):
        canvas = Canvas(self, self.facts, self.rules, self.goal)
        canvas.place(x=0, y=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
