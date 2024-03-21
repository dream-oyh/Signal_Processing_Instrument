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
        self.configure(text_color=("black", "white"))
        aug_list: list = self.master.augment_group.augment_entry_list
        enable_entry(aug_list)
        match values:
            case "Triangle Wave":
                disable_entry(aug_list[2], aug_list[3])
                change_label_name(aug_list[1], "T")
            case "Sine Wave" | "Cosine Wave":
                change_label_name(aug_list[1], "w")
                disable_entry(aug_list[3])
            case "Square Wave":
                change_label_name(aug_list[1], "T")
                disable_entry(aug_list[2])
            case "Uniform":
                change_label_name(aug_list[0], "low")
                change_label_name(aug_list[1], "up")
            case "Gaussion":
                change_label_name(aug_list[0], "u")
                change_label_name(aug_list[1], "sigma")
