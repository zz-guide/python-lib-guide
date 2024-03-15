# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-15 16:17:10
@describe TODO
"""



class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


