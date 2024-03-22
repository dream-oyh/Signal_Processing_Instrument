import customtkinter as ctk

from components.AugEntry import AugmentEntry, AugmentEntryGroup
from components.SignalComboBox import SignalComboBox
from components.SignalGroup import SignalGroup


class SignalAugment(ctk.CTkFrame):
    def __init__(
        self, master, augment_list, augment_default_list, signal_list, label_text
    ):
        super().__init__(master)
        self.augment_list = augment_list
        self.augment_default_value = augment_default_list
        self.signal_list = signal_list
        self.label_text = label_text
        self.add_widgets()

    def add_widgets(self):
        # self.augment_list =  augment_list
        # self.augment_default_value = augment_default_value
        # self.signal_list = signal_list
        # self.label_text = label_text

        self.signal_option = SignalComboBox(self, values=self.signal_list)
        self.signal_label = ctk.CTkLabel(self, text=self.label_text)
        self.augment_group = AugmentEntryGroup(
            self, self.augment_list, self.augment_default_value
        )
        self.add_first_button = ctk.CTkButton(
            self, text="Add First Group", command=self.add_first_group
        )
        self.add_second_button = ctk.CTkButton(
            self, text="Add Second Group", command=self.add_second_group
        )

        self.signal_label.grid(row=0, column=0, columnspan=2, padx=10)
        self.signal_option.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.augment_group.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.add_first_button.grid(row=3, column=0, padx=10, pady=5)
        self.add_second_button.grid(row=3, column=1, padx=10, pady=5)

    def add_first_group(self):
        self._add_group(self.master.first_group)

    def add_second_group(self):
        self._add_group(self.master.second_group)

    def get_signal_info(self):
        aug_list: list[AugmentEntry] = self.augment_group.augment_entry_list
        aug_dict = {}
        for aug in aug_list:
            if aug.entry.cget("state") == "normal":
                key: str = aug.augment_label.cget("text")
                value: int | float = aug.entry.get()
                aug_dict[key] = float(value)
        return aug_dict

    def get_signal_mode(self):
        return self.signal_option.get()

    def _add_group(self, signal_group: SignalGroup):
        mode = self.get_signal_mode()
        aug_dict = self.get_signal_info()
        signal_group.add_signal(mode=mode, augs=aug_dict)
