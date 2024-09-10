# custom_logging_config.py
from airflow.config_templates.airflow_local_settings import DEFAULT_LOGGING_CONFIG

LOGGING_CONFIG = DEFAULT_LOGGING_CONFIG

LOGGING_CONFIG['handlers']['console']['formatter'] = 'custom_formatter'
LOGGING_CONFIG['formatters']['custom_formatter'] = {
    'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S',
}
