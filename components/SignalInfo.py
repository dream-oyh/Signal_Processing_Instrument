from components.SignalAugment import SignalAugment


class SignalInfo(SignalAugment):
    def __init__(
        self, master, augment_list, augment_default_list, signal_list, label_text
    ):
        super().__init__(
            master, augment_list, augment_default_list, signal_list, label_text
        )
        self.signal_option.grid_forget()
        self.add_first_button.grid_forget()
        self.add_second_button.grid_forget()

    def get_signal_info(self):
        _, info_dict = super().get_signal_info()
        return info_dict
