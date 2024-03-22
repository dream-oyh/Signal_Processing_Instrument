import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from scipy.fft import fft

from components.SignalGroup import SignalGroup


class MyPlotNavigation(ctk.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        kwargs = {"fg_color": master._fg_color, **kwargs}
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=ctk.CENTER)


class MyCanvas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.f, self.axes = plt.subplots(2, 3)
        self.f = Figure(figsize=(15.2, 13.7), dpi=100)
        self.axes = self.f.subplots(3, 2)
        plt.tight_layout()

        self.axes[0, 0].set_title("Time Domain Curve")
        self.axes[0, 1].set_title("Frequency Norm Domain Curve")
        self.axes[1, 0].set_title("Amplitude Domain Curve")
        self.axes[1, 1].set_title("Frequency Angle Domain Curve")
        self.axes[2, 0].set_title("Time Difference Domain Curve")
        self.axes[2, 1].set_title("Wavelet Analysis Curve")

        self.Canvas = FigureCanvasTkAgg(self.f, self)
        self.toolbar = MyPlotNavigation(self, self.Canvas)
        self.analyse_button = ctk.CTkButton(self, text="Analyse", command=self.analyse)
        self.clear_button = ctk.CTkButton(self, text="Clear")
        self.Canvas.get_tk_widget().grid(
            row=0, column=0, columnspan=3, padx=10, pady=10
        )
        self.analyse_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)
        self.toolbar.grid(row=2, column=2, padx=10, pady=10)

    def analyse(self):
        self.duration, self.sample_freq = self._get_signal_info()
        self.first_t, self.first_signal = self._get_signal(self.master.first_group)
        self.second_t, self.second_signal = self._get_signal(self.master.second_group)
        self.fft_()

    def fft_(self):
        N = self.duration * self.sample_freq
        half_N_index = range(int(N / 2))

        first_fft = self._fft_caculate(self.first_signal)
        second_fft = self._fft_caculate(self.second_signal)

        if not isinstance(self.first_signal, int):
            self.axes[0, 1].plot(
                self.first_t[half_N_index], np.abs(first_fft[half_N_index]) / N
            )
            self.axes[1, 1].plot(
                self.first_t[half_N_index], np.angle(first_fft[half_N_index]) / N
            )
        if not isinstance(self.second_signal, int):
            self.axes[0, 1].plot(
                self.second_t[half_N_index], np.abs(second_fft[half_N_index]) / N
            )
            self.axes[1, 1].plot(
                self.second_t[half_N_index], np.angle(second_fft[half_N_index]) / N
            )

        self.Canvas.draw()

    def _get_signal(self, signal_group: SignalGroup):
        return signal_group.t, signal_group.signal

    def _get_signal_info(self):
        info_dict: dict[int | float] = self.master.signal_info.get_signal_info()
        return info_dict.get("Duration/s", 0), info_dict.get("Sample Freq/Hz", 0)

    def _fft_caculate(self, signal: np.ndarray):
        if not isinstance(signal, int):
            return fft(signal)
        else:
            return 0
