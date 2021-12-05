import socket
import os
import time

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CheckSocket(BaseOperator):
    @apply_defaults
    def __init__(self, host, port, **kwargs):
        super(CheckSocket, self).__init__(**kwargs)
        self.host=host
        self.port=port

    def checksocket(self):
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_result = tcp_sock.connect_ex((self.host, self.port))
        tcp_sock.close()
        return tcp_result

    def execute(self, context):
        tcp_result = self.checksocket()
        while tcp_result == 0:
            print("Killing Process")
            os.system(f"fuser -k {self.port}/tcp")
            time.sleep(1)
            tcp_result = self.checksocket()
        print("Now Port is usable")



