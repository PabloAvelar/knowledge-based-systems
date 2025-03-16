from pyswip import Prolog
import customtkinter as ctk


class Station(ctk.CTkButton):
    def __init__(self, master, state, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(width=40, height=2, border_width=2, text_color="black",
                       fg_color="#4672c3" if state == "ocupada" else "white")


class Light(ctk.CTkButton):
    def __init__(self, master, state, direction, **kwargs):
        super().__init__(master, **kwargs)
        self.direction = direction
        self.master = master
        bg_color = "white"

        if state is None:
            bg_color = "gray"
        elif state == "rojo":
            bg_color = "red"
        elif state == "verde":
            bg_color = "green"

        # Applying the configuration color
        self.configure(width=20, height=2, border_width=2, corner_radius=10, text_color="black",
                       fg_color=bg_color)

        # Draw the vector
        self.after(300, self.draw_vector)

    def draw_vector(self):
        x = self.winfo_x() + 10
        y = self.winfo_y() - 20 if self.direction[1] == "up" else self.winfo_y() + 25
        direction_text = "→" if self.direction[0] == "right" else "←"

        ctk.CTkLabel(self.master, text=direction_text, font=('Arial', 14, 'bold'), height=0).place(x=x, y=y)


class Canvas(ctk.CTkCanvas):

    def __init__(self, facts):
        super().__init__()
        self.facts = facts
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def get_widget_position(self, widget):
        self.update_idletasks()
        return [widget.winfo_x(), widget.winfo_y()]

    def create_widgets(self):
        # Stations
        h_x = 10
        s1 = Station(self, text='S1', state=self.facts.get('S1'))
        s1.place(x=h_x, y=100)

        s2 = Station(self, text='S2', state=self.facts.get('S2')).place(x=h_x, y=300)

        h_x += 370
        s3 = Station(self, text='S3', state=self.facts.get('S3')).place(x=h_x, y=100)

        h_x += 370
        s4 = Station(self, text='S4', state=self.facts.get('S4'))
        s4.place(x=h_x, y=100)
        s5 = Station(self, text='S5', state=self.facts.get('S5')).place(x=h_x, y=300)

        # Lights
        h_x = 80
        u1 = Light(self, direction=('right', 'up'), text='U1', state=self.facts.get('U1'))
        u1.place(x=h_x, y=80)
        l1 = Light(self, direction=('right', 'down'), text='L1', state=self.facts.get('L1'))
        l1.place(x=h_x, y=310)

        h_x += 80
        u2 = Light(self, direction=('left', 'up'), text='U2', state=self.facts.get('U2'))
        u2.place(x=h_x, y=170)

        l2 = Light(self, direction=('left', 'down'), text='L2', state=self.facts.get('L2'))
        l2.place(x=h_x, y=240)

        h_x += 80
        u3 = Light(self, direction=('right', 'up'), text='U3', state=self.facts.get('U3'))
        u3.place(x=h_x, y=170)
        l3 = Light(self, direction=('right', 'down'), text='L3', state=self.facts.get('L3'))
        l3.place(x=h_x, y=240)

        h_x += 80
        u7 = Light(self, direction=('left', 'up'), text='U7', state=self.facts.get('U7'))
        u7.place(x=h_x, y=80)
        h_x += 120
        u8 = Light(self, direction=('right', 'up'), text='U8', state=self.facts.get('U8'))
        u8.place(x=h_x, y=80)

        h_x += 80
        u4 = Light(self, direction=('left', 'up'), text='U4', state=self.facts.get('U4'))
        u4.place(x=h_x, y=170)
        l4 = Light(self, direction=('left', 'down'), text='L4', state=self.facts.get('L4'))
        l4.place(x=h_x, y=240)

        h_x += 80
        u5 = Light(self, direction=('right', 'up'), text='U5', state=self.facts.get('U5'))
        u5.place(x=h_x, y=170)
        l5 = Light(self, direction=('right', 'down'), text='L5', state=self.facts.get('L5'))
        l5.place(x=h_x, y=240)

        h_x += 80
        u6 = Light(self, direction=('left', 'up'), text='U6', state=self.facts.get('U6'))
        u6.place(x=h_x, y=80)
        l6 = Light(self, direction=('left', 'down'), text='L6', state=self.facts.get('L6'))
        l6.place(x=h_x, y=310)

        # Draw the lines #

        # Upper line
        x0 = self.get_widget_position(s1)[0] + 40
        y0 = self.get_widget_position(s1)[1] + 10
        x1 = x0 + 50
        y1 = y0
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0 + 200, x1, y1 + 200, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u2)[0]
        y1 = self.get_widget_position(u2)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0 + 200, x1, y1, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u3)[0] + 40
        y1 = self.get_widget_position(u3)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u7)[0]
        y1 = self.get_widget_position(u7)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0, x1, y1 + 200, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u8)[0] + 40
        y1 = self.get_widget_position(u8)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0 + 200, x1, y1 + 200, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u4)[0]
        y1 = self.get_widget_position(u4)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0 + 200, x1, y1, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u5)[0] + 40
        y1 = self.get_widget_position(u5)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(u6)[0]
        y1 = self.get_widget_position(u6)[1] + 40
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0, x1, y1 + 200, width=6)

        # Upper line
        x0 = x1
        y0 = y1
        x1 = self.get_widget_position(s4)[0] + 40
        y1 = self.get_widget_position(s4)[1] + 20
        self.create_line(x0, y0, x1, y1, width=6)
        # Lower line
        self.create_line(x0, y0 + 200, x1, y1 + 200, width=6)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Trenes')
        self.geometry('800x600')
        self.resizable(0, 0)

        # Initial facts
        self.facts = {
            "S1": "ocupada",
            "S3": "ocupada",
            "S5": "ocupada",
            "U1": "verde"
        }

        self.results = self.prolog_consult()

        # Merging initial facts with results
        self.facts.update(self.results)

        #

        print("facts results")
        print(self.facts)

        self.create_widgets()

    def prolog_consult(self):
        prolog = Prolog()

        data_path = r'trenes.pl'

        # Reading the knowledge base
        prolog.consult(data_path)

        # Create initial facts in prolog
        for key, value in self.facts.items():
            prolog.assertz(f"{key.lower()}({value})")

        query = "recorrido(Conclusiones)"
        results = list(prolog.query(query))

        dict_results = {}

        for result in results:
            # Convert list of tuples to dict
            conclusiones_dict = {k.upper(): v for k, v in result["Conclusiones"]}
            # Update the dict with the new values
            dict_results.update(conclusiones_dict)

        print("dict_results")
        print(dict_results)

        return dict_results

    def create_widgets(self):
        self.create_title()
        self.create_canvas()

    def create_title(self):
        ctk.CTkLabel(self, text='Sistema de control de tráfico ferroviario ', font=('Arial', 20)).pack(pady=20)
        ctk.CTkLabel(self, text='Pablo Avelar Armenta', font=('Arial', 14)).pack(pady=20)

    def create_canvas(self):
        canvas = Canvas(self.facts)
        canvas.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
