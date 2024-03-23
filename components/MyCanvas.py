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
        if self.tabs.get() == PROCESS_METHOD[2]:
            self.amplitude()
        if self.tabs.get() == PROCESS_METHOD[3]:
            self.colleration()
        self.master.first_group.generate_button.configure(state="disabled")
        self.master.second_group.generate_button.configure(state="disabled")

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
                "1st signal",
            )
        if not isinstance(self.second_signal, int):
            self._fft_draw(
                (self.tabs.axes[1][0], self.tabs.axes[1][1]),
                self.second_t,
                second_fft,
                "2nd signal",
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

    def _fft_draw(self, ax: tuple, t, signal, label):
        N = self.duration * self.sample_freq
        freq = fftfreq(t.shape[0], 1 / 80)
        ax[0].plot(freq[freq > 0], np.abs(signal[freq > 0] / N), label=label)
        ax[0].legend()
        ax[1].plot(freq[freq > 0], np.angle(signal[freq > 0] / N), label=label)
        ax[1].legend()

    def amplitude(self):
        n = 100
        max1, first_count_list = self._amplitude_analyse(self.first_signal, n)
        print(first_count_list)
        max2, second_count_list = self._amplitude_analyse(self.second_signal, n)
        ax = self.tabs.axes[2]
        Canvas = self.tabs.Canvas[2]
        x1 = np.linspace(-int(max1), int(max1), n, endpoint=False)
        x2 = np.linspace(-int(max2), int(max2), n, endpoint=False)
        if not isinstance(self.first_signal, int):
            ax.bar(range(len(first_count_list)), first_count_list, label="1st signal")
        if not isinstance(self.second_signal, int):
            ax.bar(range(len(second_count_list)), second_count_list, label="2nd signal")
        Canvas.draw()
        ax.legend()

    def colleration(self):
        ax = self.tabs.axes[3]
        Canvas = self.tabs.Canvas[3]
        print(type(self.first_signal))
        print(type(self.second_signal))
        if (not isinstance(self.first_signal, int)) and (
            not isinstance(self.second_signal, int)
        ):
            corr2 = self._autocorr(self.first_signal, self.second_signal)
        elif isinstance(self.first_signal, int) and (
            not isinstance(self.second_signal, int)
        ):
            corr2 = self._autocorr(self.second_signal, self.second_signal)
        elif (not isinstance(self.first_signal, int)) and isinstance(
            self.second_signal, int
        ):
            corr2 = self._autocorr(self.first_signal, self.first_signal)
        ax.plot(corr2)
        Canvas.draw()

    def _amplitude_analyse(self, data, n):
        data_max = np.max(np.abs(data))
        interval_len = data_max * 2 / n
        count_num_list = []
        for i in range(n):
            low = -data_max + i * interval_len
            high = -data_max + (i + 1) * interval_len
            count = self._interval_data_count(data, low, high)
            count_num_list.append(count)
        return data_max, count_num_list

    def _interval_data_count(self, datas, low, high):
        count_num = 0
        if not isinstance(datas, int):
            for data in datas:
                if data >= low and data <= high:
                    count_num += 1
            return count_num
        else:
            return 0

    def _autocorr(self, x, y):
        n = len(x)
        # variance = np.var(x)
        x = x - np.mean(x)
        y = y - np.mean(y)
        r = np.correlate(x, y, mode="full")
        # result = r / (variance * (np.arange(n, 0, -1)))
        return r
