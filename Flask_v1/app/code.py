# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：code.py
功能：
代码历史：2020/9/24: 杜艺创
"""


class ResponseCode(object):
    SUCCESS = 0  # 成功
    FAIL = -1  # 失败
    NO_RESOURCE_FOUND = 40001  # 未找到资源
    INVALID_PARAMETER = 40002  # 参数无效
    ACCOUNT_OR_PASS_WORD_ERR = 40003  # 账户或密码错误


class ResponseMessage(object):
    SUCCESS = "成功"
    FAIL = "失败"
    NO_RESOURCE_FOUND = "未找到资源"
    INVALID_PARAMETER = "参数无效"
    ACCOUNT_OR_PASS_WORD_ERR = "账户或密码错误"
