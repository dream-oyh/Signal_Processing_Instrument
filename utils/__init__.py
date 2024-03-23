import customtkinter as ctk

SIGNAL_INFO = ["Duration/s", "Sample Freq/Hz"]
SIGNAL_INFO_VALUE = [10, 100]
PERIO_AUG_OPTION: list[str] = [
    "A",
    "w",
    "phi",
    "Duty Ratio",
    "weight",
]
PERIO_DEFAULT_VALUE: list[str] = [1, 1, 0, 0.5, 1]
PERIO_SIGNAL_LIST: list[str] = [
    "Square Wave",
    "Triangle Wave",
    "Sine Wave",
    "Cosine Wave",
]
RANDOM_AUG_OPTION: list[str] = [
    "low",
    "up",
    "weight",
]
RANDOM_DEFAULT_VALUE: list[int | float] = [0, 1, 1]
RANDOM_SIGNAL_LIST: list[str] = ["Uniform", "Gaussion"]
PROCESS_METHOD = ["Time Domain", "FFT", "Amplitude Domain", "Time Difference Domain"]


def sub_window(text):
    window = ctk.CTk()
    window.title("Tip")
    window.geometry("300x100+500+400")
    window.attributes("-topmost", 1)

    label = ctk.CTkLabel(window, text=text)
    label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    button = ctk.CTkButton(window, text="Confirm", command=lambda: window.destroy())
    button.grid(row=1, column=2, padx=10, pady=10)
    window.mainloop()
