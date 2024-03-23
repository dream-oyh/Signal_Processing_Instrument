import threading

import customtkinter as ctk

# from components.SignalInfo import SignalInfo
from core.function import (
    cos_wave,
    gaussion_wave,
    generate_x,
    sin_wave,
    square_wave,
    triangle_wave,
    uniform_wave,
)
from utils import sub_window


class SignalFormular(ctk.CTkFrame):
    def __init__(self, master, mode, augs: dict[int]):
        super().__init__(master)
        if mode == "Signal Type":
            text = "The signal type can not be empty."
            sub_window(text)
        else:
            self.check(augs)

        match mode:
            case "Square Wave":
                self.text = f"{augs['weight']} * Square Wave(A={augs['A']},w={augs['w']},Duty Ratio={augs['Duty Ratio']})"
            case "Triangle Wave":
                self.text = (
                    f"{augs['weight']} * Triangle Wave(A={augs['A']},T={augs['T']})"
                )
            case "Sine Wave":
                self.text = f"{augs['weight']}*{augs['A']}*sin(2*pi*{augs['w']}*x+{augs['phi']})"
            case "Cosine Wave":
                self.text = f"{augs['weight']}*{augs['A']}*cos(2*pi*{augs['w']}*x+{augs['phi']})"
            case "Uniform":
                self.text = f"{augs['weight']}*Uniform({augs['low']},{augs['up']})"
            case "Gaussion":
                self.text = f"{augs['weight']}*Gaussion({augs['u']},{augs['sigma']})"
            case "Custom Signal":
                self.text = f"{augs['weight']}*Custom Signal"

        self.label_text = ctk.CTkLabel(self, text=self.text, wraplength=200)
        self.delete_button = ctk.CTkButton(
            self,
            text="—",
            width=10,
            height=20,
            corner_radius=10,
            command=self.master.master.master.master.delete_signal,
        )

        self.label_text.grid(row=0, column=0, padx=5, pady=5)
        self.delete_button.grid(row=0, column=1, padx=5, pady=5)

    def check(self, augs: dict):
        for key, value in augs.items():
            if value == 0 and ((key != "phi") and (key != "low") and (key != "u")):
                text = f'The "{key}" can not equal zero.'
                sub_window(text)
                break


class SignalGroup(ctk.CTkFrame):
    def __init__(self, master, text, height):
        super().__init__(master, width=300, height=height)

        self.label_text = ctk.CTkLabel(self, text=text)
        self.signal_list_frame = ctk.CTkScrollableFrame(self, width=250, height=height)
        self.generate_button = ctk.CTkButton(
            self,
            text="Show",
            command=lambda: threading.Thread(target=self.show_time_domain).start(),
        )

        self.label_text.grid(row=0, column=0, padx=10, pady=10)
        self.signal_list_frame.grid(row=1, column=0, padx=10, pady=10)
        self.generate_button.grid(row=2, column=0, padx=10, pady=10)

        self.signal_list: list[SignalFormular] = []
        self.mode_list: list = []
        self.augs_list: list[dict] = []
        self.num = 0
        self.signal = 0
        self.t = 0

    def add_signal(self, mode: str, augs: dict[int | float]):
        self.num += 1
        to_add_signal = SignalFormular(self.signal_list_frame, mode, augs)

        self.signal_list.append(to_add_signal)
        self.mode_list.append(mode)
        self.augs_list.append(augs)
        to_add_signal.grid(row=self.num, column=0, padx=10, pady=10, sticky=ctk.W)

    def delete_signal(self):
        self.signal_list[-1].grid_forget()
        self.signal_list.pop()
        self.mode_list.pop()
        self.augs_list.pop()
        self.num -= 1

    # def get_signal_info(self):
    #     signal_info_frame = self.master.signal_info
    #     return info_dict

    def show_time_domain(self):
        self.info_dict = self.master.signal_info.get_signal_info()
        duration = int(self.info_dict.get("Duration/s", 0))
        sample_freq = int(self.info_dict.get("Sample Freq/Hz", 0))
        ax = self.master.my_canvas.tabs.axes[0]
        canvas = self.master.my_canvas.tabs.Canvas[0]

        self.t = generate_x(duration, sample_freq)
        for mode, augs in zip(self.mode_list, self.augs_list):
            match mode:
                case "Square Wave":
                    self.signal += square_wave(self.t, augs)
                case "Triangle Wave":
                    self.signal += triangle_wave(duration, sample_freq, augs)
                case "Sine Wave":
                    self.signal += sin_wave(self.t, augs)
                case "Cosine Wave":
                    self.signal += cos_wave(self.t, augs)
                case "Uniform":
                    self.signal += uniform_wave(duration, sample_freq, augs)
                case "Gaussion":
                    self.signal += gaussion_wave(duration, sample_freq, augs)
        ax.plot(self.t, self.signal)
        ax.set_xlim([0, 2])
        ax.set_ylim([-augs.get("A") - 5, augs.get("A") + 5])
        canvas.draw()
        self.generate_button.configure(state="disabled")
