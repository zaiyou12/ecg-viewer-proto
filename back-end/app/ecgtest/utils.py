from io import BytesIO
import sys
import json
import pyedflib
import matplotlib.pyplot as plt
import os
from flask import current_app

import numpy as np
from typing import IO, Dict, List, Union

def get_details(details_path: str) -> Union[int, str, str]:
    # Get Detail from Json
    hr = None
    start_time = None
    actual_duration = None
    with open(details_path, "r") as json_file:
        details_json = json.load(json_file)
        hr = 70
        start_time = details_json['start_time']
        actual_duration = details_json['actual_duration']

    return hr, start_time, actual_duration

def get_ecg_data(data_path: str, start: int=0, n: int=None, ) -> np.ndarray:
    # ===== read edf =====
    f = pyedflib.EdfReader(data_path)
    sigbufs = f.readSignal(chn=0, start=start, n=n)
    f._close()
    return sigbufs


def ploting_from_signal(signal_arr: np.ndarray, one_image_len: int) -> IO[bytes]:
    fig = plt.figure(figsize=(15, 2*6), constrained_layout=True)
    axs = fig.subplots(6, 1)
    for idx, ax in enumerate(axs):
        cut_signal = signal_arr[idx*one_image_len:(idx+1)*one_image_len]
        ax.plot(cut_signal, 'b-', label=f'ecg_{idx}')
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
    img = BytesIO()
    fig.savefig(img, format='png', dpi=200)
    img.seek(0)
    return img


def signal_plot_to_png(signal: np.ndarray, id: int, page: int, one_image_len: int, add_name: str="") -> str:
    fig = plt.figure(figsize=(15, 2*6), constrained_layout=True)
    axs = fig.subplots(6, 1)
    for idx, ax in enumerate(axs):
        major_ticks_top=np.arange(0,one_image_len+256,256)
        minor_ticks_top=np.arange(0,one_image_len+256,256/5)
        cut_signal = signal[idx*one_image_len:(idx+1)*one_image_len]

        for_fig_size_arr = cut_signal[cut_signal>1.0]

        qs = np.percentile(for_fig_size_arr, [1, 99], interpolation='nearest')
        q_1 = qs[0]
        q_3 = qs[1]
        iqr = q_3 - q_1
        y_min = q_1 - 0.3*iqr
        y_max = q_3 + 0.3*iqr

        ax.plot(cut_signal, 'b-', label=f'ecg_{idx}')
        ax.set_xticks(major_ticks_top)
        ax.set_xticks(minor_ticks_top, minor=True)
        ax.grid(which="major",alpha=0.8)
        ax.grid(which="minor",alpha=0.3)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_ylim(y_min,y_max)

    file_name = f"{id}_{page}{add_name}.png"
    file_path = os.path.join(current_app.root_path, 'static/ecg_png_cache', file_name)
    fig.savefig(file_path, format='png', dpi=200)
    return file_name



def file_exist_check(id: int, page: int, add_name: str="") -> str:
    file_name = f"{id}_{page}{add_name}.png"
    file_path = os.path.join(current_app.root_path, 'static/ecg_png_cache', file_name)
    if os.path.isfile(file_path):
        return file_name
    else:
        return None
