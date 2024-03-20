from components.AugEntry import AugmentEntry


def enable_entry(entry_widgets: list[AugmentEntry]):
    for entry in entry_widgets:
        widget = entry.entry
        widget.configure(state="normal", text_color="white")
        label = entry.augment_label
        label.configure(text_color="white")


def disable_entry(*entry_widgets: tuple[AugmentEntry]):
    for entry in entry_widgets:
        widget = entry.entry
        widget.configure(state="disabled", text_color="gray")
        label = entry.augment_label
        label.configure(text_color="gray")

def change_label_name(entry: AugmentEntry, name:str):
    entry.augment_label.configure(text=name)