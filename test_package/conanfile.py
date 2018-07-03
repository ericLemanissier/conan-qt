#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        for req in self.requires:
            self.run("qmake %s/%s" % (self.source_folder ,req))
            if self.settings.os == "Windows":
                if self.settings.compiler == "Visual Studio":
                    make = find_executable("jom.exe")
                    if not make:
                        make = "nmake.exe"                
                    self.run("%s && %s" % (tools.vcvars_command(self.settings), make))
                else:
                    # Workaround for configure using clang first if in the path
                    new_path = []
                    for item in os.environ['PATH'].split(';'):
                        if item != 'C:\\Program Files\\LLVM\\bin':
                            new_path.append(item)
                    os.environ['PATH'] = ';'.join(new_path)
                    # end workaround
                    self.run("mingw32-make")
            else:
                self.run("make")
            return
        self.output.error("No test package for %s" % self.requires)

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            bin_path = os.path.join(str(self.settings.build_type).lower(), "test_package")
            if self.settings.os == "Windows":
                self.run(bin_path)
            elif self.settings.os == "Macos":
                self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ.get('DYLD_LIBRARY_PATH', ''), bin_path))
            else:
                self.run("LD_LIBRARY_PATH=%s %s" % (os.environ.get('LD_LIBRARY_PATH', ''), bin_path))
