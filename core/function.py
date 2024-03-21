import math

import numpy as np
from scipy import signal


def generate_x(duration, sample_freq):
    t = np.linspace(0, duration, sample_freq * duration, endpoint=False)
    return t


def square_wave(t, augs: dict[int | float]):
    y = signal.square(2 * np.pi / augs["T"] * t)
    return y * augs["weight"]


def triangle_wave(duration, sample_freq, augs: dict[int | float]):
    def Triangle(x: list, w, h):
        r = []
        for xi in x:
            if xi < 0.5 * w:
                r.append(2 * h * xi / w)
            else:
                r.append(-2 * h * xi / w + 2 * h / w * w)
        return r

    T = int(augs["T"])
    A = augs["A"]
    t1 = np.linspace(0, T, sample_freq * T, endpoint=False)

    y = Triangle(t1.tolist(), T, A)
    num = math.floor(duration / T) + 1
    for i in range(num):
        y = np.append(y, y)
    return y[: duration * sample_freq] * augs["weight"]


def sin_wave(t, augs: dict[int | float]):
    y = augs["weight"] * augs["A"] * np.sin(2 * np.pi * augs["w"] * t + augs["phi"])
    return y


def cos_wave(t, augs: dict[int | float]):
    y = augs["weight"] * augs["A"] * np.cos(2 * np.pi * augs["w"] * t + augs["phi"])
    return y


def uniform_wave(duration, sample_freq, augs: dict[int | float]):
    t = np.round(np.random.uniform(augs["low"], augs["up"], duration * sample_freq), 2)
    return t


def gaussion_wave(duration, sample_freq, augs: dict[int | float]):
    t = np.round(np.random.normal(augs["u"], augs["sigma"], duration * sample_freq), 2)
    return t
