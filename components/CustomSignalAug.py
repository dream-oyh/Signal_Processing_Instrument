import customtkinter as ctk


class CustomSignalAug(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_text = ctk.CTkLabel(self, text="Custom Signal Generator")
        self.open_file = ctk.CTkButton(
            self, text="Open File", fg_color="lightblue", text_color="black"
        )
        self.add_first_button = ctk.CTkButton(self, text="Add First Group")
        self.add_second_button = ctk.CTkButton(self, text="Add Second Group")

        self.label_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.open_file.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.add_first_button.grid(row=2, column=0, padx=10, pady=10)
        self.add_second_button.grid(row=2, column=1, padx=10, pady=10)
