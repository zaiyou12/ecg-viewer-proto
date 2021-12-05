import subprocess
import shlex

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CloseSSHTunnel(BaseOperator):
    @apply_defaults
    def __init__(self, local_port, **kwargs):
        super(CloseSSHTunnel, self).__init__(**kwargs)
        self.local_port = local_port

    def execute_bash_command(self):
        bash_command = f"fuser -k {self.local_port}/tcp"
        self.log.info(f"Bash Command is -> {bash_command}")
        args = shlex.split(bash_command)
        tunnel = subprocess.Popen(args)
        self.log.info(f"Closing Tunnel Executed")

    def execute(self, context):
        self.execute_bash_command()

