from collections import OrderedDict
import numpy as np
from datetime import datetime
import os

class EDFhandler():
    
    # Start_Index, Size
    # All ascii -> .decode("ascii").strip()
    file_header = {
        'version': [0, 8],
        'patient': [8, 80],
        'recording': [88, 80],
        'startdate': [168, 8],
        'starttime': [176, 8],
        'n_bytes': [184, 8],
        'reserved': [192, 44],
        'n_records': [236, 8],
        'duration': [244, 8],
        'n_signals': [252, 4]
    }

    # Cum_Index, Size
    # All ascii -> .decode("ascii").strip()
    signal_header = {
        'label': [0, 16],
        'transducer': [16, 80],
        'dimension': [96, 8],
        'pmin': [104, 8],
        'pmax': [112, 8],
        'dmin': [120, 8],
        'dmax': [128, 8],
        'prefilter': [136, 80],
        'n_samples': [216, 8],
        'reserved': [224, 32],
    }

    def __init__(self):
        self.blob = None
        self.record_start_idx = None
        self.n_signals = None
        self.n_records = None
        self.startdate = None
        self.starttime = None

        self.header_byte = None
        self.signal_header_byte = None
        self.record_data_byte = None

    def read_blob(self, blob):
        self.blob = blob
        self.get_data_from_header()
        self.header_byte = self.blob[:256]
        self.signal_header_byte = self.blob[256:256+self.n_signals*256]
        self.record_data_byte = self.blob[256+self.n_signals*256:]

    # Return Byte Class
    def get_byte_from_header(self, target):
        start_idx = EDFhandler.file_header[target][0]
        end_idx = start_idx + EDFhandler.file_header[target][1]
        return self.blob[ start_idx : end_idx ]

    # Return Byte Class
    def get_byte_from_signal_header(self, target, ch):
        # file header size + before info size + target channel
        start_idx = 256 + (EDFhandler.signal_header[target][0]*self.n_signals) + (ch*EDFhandler.signal_header[target][1])
        end_idx = start_idx + EDFhandler.signal_header[target][1]
        return self.blob[ start_idx : end_idx ]

    
    def get_data_from_header(self):
        self.n_signals = "" if self.get_byte_from_header('n_signals').decode('ascii').strip() == "" else int(self.get_byte_from_header('n_signals').decode('ascii').strip())
        self.record_start_idx = 256 + (256*self.n_signals)
        self.n_records = "" if self.get_byte_from_header('n_records').decode('ascii').strip() == "" else int(self.get_byte_from_header('n_records').decode('ascii').strip())
        self.startdate = self.get_byte_from_header('startdate').decode('ascii').strip()
        self.starttime = self.get_byte_from_header('starttime').decode('ascii').strip()


    def read_signal_header(self, ch):
        ns = self.n_signals
        if ch >= ns:
            print("No signal...")
            return -1

        n_samples = int(self.get_byte_from_signal_header('n_samples', ch).decode("ascii").strip())
        pmin = float(self.get_byte_from_signal_header('pmin', ch).decode("ascii").strip())
        pmax = float(self.get_byte_from_signal_header('pmax', ch).decode("ascii").strip())
        dmin = float(self.get_byte_from_signal_header('dmin', ch).decode("ascii").strip())
        dmax = float(self.get_byte_from_signal_header('dmax', ch).decode("ascii").strip())

        return n_samples, pmin, pmax, dmin, dmax

    def get_info_from_signalheader(self, target, ch):
        return self.get_byte_from_signal_header(target, ch).decode("ascii").strip()


    def get_signal(self, ch, in_float=True):
        if self.n_signals == "" or self.n_records == "":
            return -1
        ns = self.n_signals
        if ch >= ns:
            print("No signal...")
            return -1

        # Record data 시작점
        record_start_idx = self.record_start_idx

        # Single Lead 일경우 효율을 위해서...
        if ns == 1:
            if in_float:
                # Get info from header
                n_samples, pmin, pmax, dmin, dmax = self.read_signal_header(ch=ch)
                m = (pmax - pmin) / (dmax - dmin)
                b = pmax / (m - dmax)
                # For collect
                sig_dum = []
                for i in range(record_start_idx, len(self.blob), 2):
                    byte_buf = self.blob[ i:i+2 ]
                    data=int.from_bytes(byte_buf, byteorder='little', signed=True)
                    data = m * (data+b)
                    sig_dum.append(data)
                return np.array(sig_dum)
            else:
                return self.blob[record_start_idx:]

        if in_float:
            # Get info from header
            n_samples, pmin, pmax, dmin, dmax = self.read_signal_header(ch=ch)
            m = (pmax - pmin) / (dmax - dmin)
            b = pmax / (m - dmax)

            # For collect
            sig_dum = []
            for rec_i in range(self.n_records):
                for sample_idx in range(n_samples):
                    byte_buf=self.blob[ record_start_idx+(ch*2):record_start_idx+((ch+1)*2) ]
                    record_start_idx += ns*2

                    data=int.from_bytes(byte_buf, byteorder='little', signed=True)
                    data = m * (data+b)
                    sig_dum.append(data)

            return np.array(sig_dum)
        else:
            byte_dum = b''
            for i in range(record_start_idx+(ch*2), len(self.blob), 2*ns):
                byte_dum += self.blob[i:i+2]
            return byte_dum


    def get_start_datetime(self):
        date_ = self.startdate
        time_ = self.starttime

        day_ = int(date_[:2])
        month_ = int(date_[3:5])
        year_ = int(str(datetime.today().year)[:2]+date_[6:8])

        hour_ = int(time_[:2])
        minute_ = int(time_[3:5])
        second_ = int(time_[6:8])

        time_obj = datetime(year=year_, month=month_, day=day_, hour=hour_, minute=minute_, second=second_)

        return time_obj

    def check_data_status(self):
        if self.n_signals=="" or self.n_records=="" or self.startdate=="" or self.starttime=="":
            return -1
        else:
            return 0

    def return_header(self):
        return self.header_byte

    def return_signal_header(self):
        return self.signal_header_byte



    #########################
    ##### Create Part
    def set_header(self, byte_data):
        self.header_byte = byte_data
        n_signals_from_header = self.header_byte[ EDFhandler.file_header['n_signals'][0] : EDFhandler.file_header['n_signals'][0]+EDFhandler.file_header['n_signals'][1] ].decode("ascii").strip()
        self.n_signals = "" if n_signals_from_header=="" else int(n_signals_from_header)

    def set_signal_header(self, byte_data):
        self.signal_header_byte = byte_data

    def set_record_data(self, byte_data):
        self.record_data_byte = byte_data

    def change_header(self, target, val_in_str):
        start_idx = EDFhandler.file_header[target][0]
        end_idx = start_idx + EDFhandler.file_header[target][1]
        before_data = self.header_byte[ start_idx:end_idx ]

        val_in_ascii = val_in_str.encode('ascii')
        if len(val_in_ascii) > len(before_data):
            return -1
        else:
            blank = ' '
            blank_in_byte = blank.encode('ascii')
            val_in_ascii += blank_in_byte*int(len(before_data)-len(val_in_ascii))

        self.header_byte = self.header_byte[:start_idx] + val_in_ascii + self.header_byte[end_idx:]

    def change_datetime_header(self, datetime_):
        str_datetime_ = datetime_.strftime("%y_%m_%d_%H_%M_%S")
        year_, month_, day_, hour_, minute_, second_ = str_datetime_.split("_")

        date_ = day_ + "." + month_  + "." + year_
        time_ = hour_ + "." + minute_  + "." + second_

        
        date_start_idx = EDFhandler.file_header['startdate'][0]
        date_end_idx = date_start_idx + EDFhandler.file_header['startdate'][1]
        time_start_idx = EDFhandler.file_header['starttime'][0]
        time_end_idx = time_start_idx + EDFhandler.file_header['starttime'][1]

        self.header_byte = self.header_byte[:date_start_idx] + date_.encode('ascii') + self.header_byte[date_end_idx:]
        self.header_byte = self.header_byte[:time_start_idx] + time_.encode('ascii') + self.header_byte[time_end_idx:]

    def change_signal_header(self, target, ch, val_in_str):
        start_idx = (EDFhandler.signal_header[target][0]*self.n_signals) + (ch*EDFhandler.signal_header[target][1])
        end_idx = start_idx + EDFhandler.signal_header[target][1]
        before_data = self.signal_header_byte[ start_idx:end_idx ]

        val_in_ascii = val_in_str.encode('ascii')
        if len(val_in_ascii) > len(before_data):
            return -1
        else:
            blank = ' '
            blank_in_byte = blank.encode('ascii')
            val_in_ascii += blank_in_byte*int(len(before_data)-len(val_in_ascii))

        self.signal_header_byte = self.signal_header_byte[:start_idx] + val_in_ascii + self.signal_header_byte[end_idx:]


    def make_data_in_edf_format(self):
        if self.header_byte is None or self.signal_header_byte is None or self.record_data_byte is None:
            return -1

        self.blob = self.header_byte + self.signal_header_byte + self.record_data_byte

    def save_edf_format(self, path):
        result = self.make_data_in_edf_format()
        if result != -1:
            if os.path.exists(path):
                # print("This file already exists.")
                return -1
            with open(path, 'wb') as f:
                f.write(self.blob)



    

    














