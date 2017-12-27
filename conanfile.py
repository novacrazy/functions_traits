#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile

class functionTraits(ConanFile):
    name = "function_traits"
    # the project does not have released versions specified, so generated
    # a minimum version appended with the output of 'git describe --always'
    version = "0.0.1-41428b4"
    url     = "https://github.com/novacrazy/function_traits"
    exports = ("include*")

    #Header only
    settings = None

    def package(self):
        self.copy("*", src="include", dst="include")
