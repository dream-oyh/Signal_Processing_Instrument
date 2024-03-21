import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class MyPlotNavigation(ctk.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        kwargs = {"fg_color": master._fg_color, **kwargs}
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=ctk.CENTER)


class MyCanvas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.f = Figure(figsize=(13.8, 13.7), dpi=100)
        self.plot_1 = self.f.add_subplot(221)
        self.plot_2 = self.f.add_subplot(222)
        self.plot_3 = self.f.add_subplot(223)
        self.plot_4 = self.f.add_subplot(224)
        # self.plot_5 = self.f.add_subplot(235)
        # self.plot_6 = self.f.add_subplot(236)

        self.plot_1.set_title("Time Domain Curve")
        self.plot_2.set_title("Frequency Domain Curve")
        self.plot_3.set_title("Amplitude Domain Curve")
        self.plot_4.set_title("Time Difference Domain Curve")



        self.Canvas = FigureCanvasTkAgg(self.f, self)
        self.toolbar = MyPlotNavigation(self, self.Canvas)
        self.analyse_button = ctk.CTkButton(self, text="Analyse")
        self.clear_button = ctk.CTkButton(self, text="Clear")
        self.Canvas.get_tk_widget().grid(
            row=0, column=0, columnspan=3, padx=10, pady=10
        )
        self.analyse_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10,pady=10)
        self.toolbar.grid(row=2, column=2, padx=10, pady=10)
