import logging

import customtkinter as ctk

from utils import sub_window


class SignalFormular(ctk.CTkFrame):
    def __init__(self, master, mode, augs: dict[int]):
        super().__init__(master)
        logging.info(mode)
        logging.info(augs)
        if mode == "Signal Type":
            text = "The signal type can not be empty."
            sub_window(text)
        else:
            self.check(augs)

        match mode:
            case "Square Wave":
                self.text = f"{augs['weight']} * Square Wave(A={augs['A']},T={augs['T']},Duty Ratio={augs['Duty Ratio']})"
            case "Triangle Wave":
                self.text = (
                    f"{augs['weight']} * Triangle Wave(A={augs['A']},T={augs['T']})"
                )
            case "Sine Wave":
                self.text = f"{augs['weight']}*{augs['A']}*sin(2*pi/{augs['T']}*x+{augs['phi']})"
            case "Cosine Wave":
                self.text = f"{augs['weight']}*{augs['A']}*cos(2*pi/{augs['T']}*x+{augs['phi']})"
            case "Uniform":
                self.text = f"{augs['weight']}*Uniform({augs['low']},{augs['up']})"
            case "Gaussion":
                self.text = f"{augs['weight']}*Gaussion({augs['u']},{augs['sigma']})"
            case "Custom Signal":
                self.text = f"{augs['weight']}*Custom Signal"

        self.label_text = ctk.CTkLabel(self, text=self.text, wraplength=450)
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
            if value == "0" and ((key != "phi") and (key != "low") and (key != "u")):
                text = f'The "{key}" can not equal zero.'
                sub_window(text)
                break


class SignalGroup(ctk.CTkFrame):
    def __init__(self, master, text, height):
        super().__init__(master, width=300, height=height)

        self.label_text = ctk.CTkLabel(self, text=text)
        self.signal_list_frame = ctk.CTkScrollableFrame(self, width=350, height=height)
        self.generate_button = ctk.CTkButton(self, text="Show")

        self.label_text.grid(row=0, column=0, padx=10, pady=10)
        self.signal_list_frame.grid(row=1, column=0, padx=10, pady=10)
        self.generate_button.grid(row=2, column=0, padx=10, pady=10)

        self.signal_list: list[SignalFormular] = []
        self.mode_list = []
        self.augs_list = []
        self.num = 0

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
