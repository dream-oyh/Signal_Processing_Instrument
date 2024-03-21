import customtkinter as ctk

from components.CustomSignalAug import CustomSignalAug
from components.MyCanvas import MyCanvas
from components.SignalAugment import SignalAugment
from components.SignalGroup import SignalGroup
from components.SignalInfo import SignalInfo
from utils import (
    PERIO_AUG_OPTION,
    PERIO_DEFAULT_VALUE,
    PERIO_SIGNAL_LIST,
    RANDOM_AUG_OPTION,
    RANDOM_DEFAULT_VALUE,
    RANDOM_SIGNAL_LIST,
    SIGNAL_INFO,
    SIGNAL_INFO_VALUE,
)


class APP(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.signal_info = SignalInfo(
            self, SIGNAL_INFO, SIGNAL_INFO_VALUE, None, "Signal Basic Info"
        )

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
        self.first_group = SignalGroup(self, "First Combined Signal", height=395)
        self.second_group = SignalGroup(self, "Second Combined Signal", height=315)
        self.my_canvas = MyCanvas(self)

        self.signal_info.grid(row=0, column=0, padx=10, pady=5, sticky=ctk.N)
        self.periodic_signals.grid(row=1, column=0, padx=10, pady=5, sticky=ctk.N)
        self.random_signals.grid(row=2, column=0, padx=10, pady=5, sticky=ctk.N)
        self.custom_signal.grid(row=3, column=0, padx=10, pady=5, sticky=ctk.N)
        self.first_group.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky=ctk.S)
        self.second_group.grid(
            row=2, column=1, rowspan=2, padx=10, pady=5, sticky=ctk.N
        )
        self.my_canvas.grid(row=0, column=2, rowspan=4, padx=10, pady=5)
