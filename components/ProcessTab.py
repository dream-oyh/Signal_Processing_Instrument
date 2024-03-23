import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from utils import PROCESS_METHOD


class MyPlotNavigation(ctk.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        kwargs = {"fg_color": master._fg_color, **kwargs}
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=ctk.CENTER)


class ProcessTab(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.fig = []
        self.axes = []
        self.Canvas = []
        self.toolbar = []
        for method in PROCESS_METHOD:
            self.add(method)
            if method == "FFT":
                fig, axes = self._set_ax(
                    2,
                    1,
                    ("Frequency Norm Domain Curve", "Frequency Angle Domain Curve"),
                )
            else:
                fig, axes = self._set_ax(1, 1, method + " Curve")
            canvas, toolbar = self._set_canvas(self.tab(method), fig)
            self._append(fig, axes, canvas, toolbar)
            self._canvas_grid(canvas, toolbar)

    def _set_ax(self, rows: int, columns: int, title: tuple[str]):
        # assert len(title) == rows * columns, "The title is out of index."
        f = Figure(figsize=(14.2, 11.9), dpi=100)
        axes = f.subplots(rows, columns)
        if rows == 1 and columns == 1:
            axes.set_title(title)
        elif (rows == 1 or columns == 1) and rows * columns != 1:
            for i in range(rows * columns):
                axes[i].set_title(title[i])
        else:
            for i in range(rows):
                for j in range(columns):
                    axes[i, j].set_title(title[i * rows + j])
        return f, axes

    def _set_canvas(self, master, figure):
        Canvas = FigureCanvasTkAgg(figure, master)
        toolbar = MyPlotNavigation(master, Canvas)
        return Canvas, toolbar

    def _append(self, fig, axes, canvas, toolbar):
        self.fig.append(fig)
        self.axes.append(axes)
        self.Canvas.append(canvas)
        self.toolbar.append(toolbar)

    def _canvas_grid(self, canvas, toolbar):
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
        toolbar.grid(row=1, column=0, padx=10, pady=10)
