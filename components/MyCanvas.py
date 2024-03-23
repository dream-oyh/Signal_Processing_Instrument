import customtkinter as ctk
import numpy as np
from scipy.fftpack import fft, fftfreq

from components.ProcessTab import ProcessTab
from components.SignalGroup import SignalGroup
from utils import PROCESS_METHOD


class MyCanvas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.f, self.axes = plt.subplots(2, 3)
        # self.f = Figure(figsize=(15.2, 13.7), dpi=100)
        # self.axes = self.f.subplots(3, 1)
        self.tabs = ProcessTab(self)
        self.analyse_button = ctk.CTkButton(self, text="Analyse", command=self.analyse)
        self.clear_button = ctk.CTkButton(self, text="Clear")

        self.tabs.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.analyse_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def analyse(self):
        self.duration, self.sample_freq = self._get_signal_info()
        self.first_t, self.first_signal = self._get_signal(self.master.first_group)
        self.second_t, self.second_signal = self._get_signal(self.master.second_group)
        if self.tabs.get() == PROCESS_METHOD[1]:
            self.fft_()

    def fft_(self):
        first_fft = self._fft_caculate(self.first_signal)
        second_fft = self._fft_caculate(self.second_signal)
        Canvas = self.tabs.Canvas[1]
        # self.tabs.set(PROCESS_METHOD[1])
        if not isinstance(self.first_signal, int):
            self._fft_draw(
                (self.tabs.axes[1][0], self.tabs.axes[1][1]),
                self.first_t,
                first_fft,
            )
        if not isinstance(self.second_signal, int):
            self._fft_draw(
                (self.tabs.axes[1][0], self.tabs.axes[1][1]),
                self.second_t,
                second_fft,
            )

        Canvas.draw()

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

    def _fft_draw(self, ax: tuple, t, signal):
        N = self.duration * self.sample_freq
        freq = fftfreq(t.shape[0], 1 / 80)
        ax[0].plot(freq[freq > 0], np.abs(signal[freq > 0] / N))
        ax[1].plot(freq[freq > 0], np.angle(signal[freq > 0] / N))
