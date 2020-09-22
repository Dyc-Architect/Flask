"""
文件名：factory.py
功能：
代码历史：2020/9/22: 杜艺创
"""
import yaml
import os
from flask import Flask
import logging
import logging.config


def create_app(config_name=None, config_path=None):
    app = Flask(__name__)
    # 读取配置文件
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config/config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)
    if not os.path.exists(app.config['LOGGING_PATH']):
        # 日志文件目录
        os.mkdir(app.config['LOGGING_PATH'])
        # 日志设置
    with open(app.config['LOGGING_CONFIG_PATH'], 'r', encoding='utf-8') as f:
        dict_conf = yaml.safe_load(f.read())
    print(dict_conf)
    logging.config.dictConfig(dict_conf)  # 载入日志配置
    return app


def read_yaml(config_name, config_path):
    """
    config_name:需要读取的配置内容
    config_path:配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r') as f:
            conf = yaml.safe_load(f.read())  # yaml.load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')

    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')