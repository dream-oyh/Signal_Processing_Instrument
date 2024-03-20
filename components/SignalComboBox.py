import customtkinter as ctk

from core.ui_control import change_label_name, disable_entry, enable_entry


class SignalComboBox(ctk.CTkComboBox):
    def __init__(self, master, values: list[str]):
        self.x = ctk.StringVar(value="Signal Type")
        super().__init__(
            master,
            values=values,
            variable=self.x,
            command=self.adjust_aug_list,
            text_color="gray",
        )

    def adjust_aug_list(self, values):
        self.configure(text_color="white")
        aug_list: list = self.master.augment_group.augment_entry_list
        enable_entry(aug_list)
        match values:
            case "Triangle Wave":
                disable_entry(aug_list[4], aug_list[5])
            case "Sine Wave" | "Cosine Wave":
                disable_entry(aug_list[5])
            case "Square Wave":
                disable_entry(aug_list[4])
            case "Uniform":
                change_label_name(aug_list[2], "low")
                change_label_name(aug_list[3], "up")
            case "Gaussion":
                change_label_name(aug_list[2], "u")
                change_label_name(aug_list[3], "sigma")
