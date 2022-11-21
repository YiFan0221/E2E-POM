#存取實體檔案用

import yaml
import sys,os
sys.path.append(os.getcwd())

os.environ['CONFIG_FILE']='config.yaml'

#讀檔實作
def read_yaml_file(yaml_file: str) -> dict:
    with open(yaml_file, "r") as steam:
        yaml_config = yaml.safe_load(steam)
    return yaml_config


class ConfigHelper:

    def __init__(self):
        self.config = self._read_config()

    @staticmethod #建構式 讀檔
    def _read_config():
        config_path = os.environ["CONFIG_FILE"]
        return read_yaml_file(config_path)
        
    def get_firefix_binary_path(self):
        return self.config["firefox_binary"]

    def get_ig_username(self):
        return self.config["instagram_user"]

    def get_ig_password(self):
        return self.config["instagram_pwd"]
