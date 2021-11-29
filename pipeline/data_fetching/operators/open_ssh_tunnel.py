import subprocess
import shlex

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults



class OpenSSHTunnel(BaseOperator):
    @apply_defaults
    def __init__(self, local_port, host_url, host_port, server_port, identityfile, user, server_ip, **kwargs):
        super(OpenSSHTunnel, self).__init__(**kwargs)
        self.local_port = local_port
        self.host_url = host_url
        self.host_port = host_port
        self.server_port = server_port
        self.identityfile = identityfile
        self.user = user
        self.server_ip = server_ip

    def execute_bash_command(self):
        bash_command = f"ssh -f -N -4 -L {self.local_port}:{self.host_url}:{self.host_port} -o ExitOnForwardFailure=yes -p {self.server_port} -i {self.identityfile} {self.user}@{self.server_ip}"
        self.log.info(f"Bash Command is -> {bash_command}")
        args = shlex.split(bash_command)
        tunnel = subprocess.Popen(args)
        self.log.info(f"Making Tunnel success")


    def execute(self, context):
        self.execute_bash_command()


