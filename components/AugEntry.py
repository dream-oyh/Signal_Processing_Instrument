import customtkinter as ctk


class AugmentEntry(ctk.CTkFrame):
    def __init__(self, master, augment: str, value: int | float):
        super().__init__(master)

        self.augment_label = ctk.CTkLabel(
            self, text=augment, width=10, fg_color="transparent"
        )
        self.augment_label.grid(row=0, column=0, padx=10, sticky=ctk.E)

        self.augment_val = ctk.DoubleVar(value=value)
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=augment,
            textvariable=self.augment_val,
        )
        self.entry.grid(row=0, column=1, padx=10, sticky=ctk.E)


class AugmentEntryGroup(ctk.CTkFrame):
    def __init__(self, master, aug_list: list[str], aug_default: list[int | float]):
        super().__init__(master, fg_color="transparent")

        self.augment_entry_list = []
        index = 0

        assert len(aug_list) == len(
            aug_default
        ), "The augment list number doesn't equal the augment default value number"

        for aug, default in zip(aug_list, aug_default):
            self.augment_entry_list.append(
                AugmentEntry(self, augment=aug, value=default)
            )
            self.augment_entry_list[index].grid(
                row=index, column=0, padx=10, pady=10, sticky=ctk.E
            )
            index += 1
