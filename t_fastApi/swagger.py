# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-14 23:47:50
@describe TODO
"""

from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html


def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        # swagger_js_url="https://unpkg.zhimg.com/swagger-ui-dist@3.29/swagger-ui-bundle.js",
        # swagger_css_url="https://unpkg.zhimg.com/swagger-ui-dist@3.29/swagger-ui.css"
        swagger_js_url="https://cdn.staticfile.org/swagger-ui/5.9.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.org/swagger-ui/5.9.0/swagger-ui.min.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch
