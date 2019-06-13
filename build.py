#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
import os

if __name__ == "__main__":

    builder = build_template_default.get_builder(build_policy="outdated")
    android_api_level = os.getenv("ANDROID_API_LEVEL")
    if android_api_level:
        for it in builder.items:
            it.settings['os'] = 'Android'
            it.settings['compiler.libcxx'] = 'libc++'
            it.settings['os.api_level'] = android_api_level
    builder.run()
