from preprocess import utils


def bandwith_process(signal):
    processed_signal = utils.final_filter(signal, fs=256, order=5)
    return processed_signal




process_module = {
    "bandwith_process": bandwith_process
}