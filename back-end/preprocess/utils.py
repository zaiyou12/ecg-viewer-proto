from scipy.signal import lfilter, sosfilt
from scipy.signal import butter, iirnotch, lfilter


######################## High & Low pass filter ########################
## A high pass filter allows frequencies higher than a cut-off value
def butter_highpass(cutoff, fs, order=5):
    sos = butter(order, cutoff, 'hp', fs=fs, output='sos')
    return sos

## A low pass filter allows frequencies lower than a cut-off value
def butter_lowpass(cutoff, fs, order=5):
    sos = butter(order, cutoff, 'lp', fs=fs, output='sos')
    return sos

def final_filter(data, fs, order=5):
    highpass_sos = butter_highpass(0.5, fs, order=order)
    x = sosfilt(highpass_sos, data)
    lowpass_sos = butter_highpass(2.5, fs, order=order)
    y = sosfilt(lowpass_sos, x)
    return y