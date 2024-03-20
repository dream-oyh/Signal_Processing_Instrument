import customtkinter as ctk

from components.CustomSignalAug import CustomSignalAug
from components.MyCanvas import MyCanvas
from components.PerioSignalAugment import SignalAugment
from components.SignalGroup import SignalGroup
from utils import (
    PERIO_AUG_OPTION,
    PERIO_DEFAULT_VALUE,
    PERIO_SIGNAL_LIST,
    RANDOM_AUG_OPTION,
    RANDOM_DEFAULT_VALUE,
    RANDOM_SIGNAL_LIST,
)


class APP(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.periodic_signals = SignalAugment(
            self,
            PERIO_AUG_OPTION,
            PERIO_DEFAULT_VALUE,
            PERIO_SIGNAL_LIST,
            "Periodic Signal Generator",
        )
        self.random_signals = SignalAugment(
            self,
            RANDOM_AUG_OPTION,
            RANDOM_DEFAULT_VALUE,
            RANDOM_SIGNAL_LIST,
            "Random Signal Generator",
        )
        self.custom_signal = CustomSignalAug(self)
        self.first_group = SignalGroup(self, "First Combined Signal", height=335)
        self.second_group = SignalGroup(self, "Second Combined Signal", height=375)
        self.my_canvas = MyCanvas(self)

        self.periodic_signals.grid(row=0, column=0, padx=10, pady=5)
        self.random_signals.grid(row=1, column=0, padx=10, pady=5)
        self.custom_signal.grid(row=2, column=0, padx=10, pady=5)
        self.first_group.grid(row=0, column=1, padx=10, pady=5, sticky=ctk.S)
        self.second_group.grid(
            row=1, column=1, rowspan=2, padx=10, pady=5, sticky=ctk.N
        )
        self.my_canvas.grid(row=0, column=2, rowspan=3, padx=10, pady=5)
