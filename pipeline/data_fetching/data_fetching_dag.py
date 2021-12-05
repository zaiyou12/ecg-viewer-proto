import airflow
from airflow import DAG

from data_fetching.operators.check_socket import CheckSocket
from data_fetching.operators.open_ssh_tunnel import OpenSSHTunnel
from data_fetching.operators.close_ssh_tunnel import CloseSSHTunnel
from data_fetching.operators.fetching_data import FetchingData, Copy_Org_Site
from data_fetching.operators.validate_data import ValidateData

from data_fetching.config import Config

dag = DAG(
    dag_id="db_pipeline",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

local_host= Config.local_host
local_port= Config.local_port
host_url= Config.host_url
host_port= Config.host_port
user= Config.user
server_ip= Config.server_ip
server_port= Config.server_port
identityfile= Config.identityfile
region= Config.region
recording_db_path= Config.recording_db_path

db_user= Config.db_user
db_password= Config.db_password
db_name= Config.db_name

check_port_usable = CheckSocket(
    task_id='check_port_usable',
    host=local_host,
    port=local_port,
    dag=dag
)


open_ssh_tunnel = OpenSSHTunnel(
    task_id="open_ssh_tunnel",
    local_port=local_port,
    host_url=host_url,
    host_port=host_port,
    server_port=server_port,
    identityfile=identityfile,
    user=user,
    server_ip=server_ip,
    dag=dag,
)


copy_org_site_info = Copy_Org_Site(
    task_id="copy_org_site_info",
    user=db_user,
    password=db_password,
    host=local_host,
    port=local_port,
    database=db_name,
    region="AU",
    dag=dag,
)


fetching_data = FetchingData(
    task_id="fetching_data",
    user=db_user,
    password=db_password,
    host=local_host,
    port=local_port,
    database=db_name,
    region="AU",
    get_type='all',
    dag=dag,
)

close_ssh_tunnel = CloseSSHTunnel(
    task_id="close_ssh_tunnel",
    local_port=local_port,
    dag=dag,
)


validation_data = ValidateData(
    task_id='validation_data',
    dag=dag
)



check_port_usable >> open_ssh_tunnel
open_ssh_tunnel >> copy_org_site_info
copy_org_site_info >> fetching_data
fetching_data >> close_ssh_tunnel
close_ssh_tunnel >> validation_data