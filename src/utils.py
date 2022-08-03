#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of ppaurl
#
# Copyright (C) 2016-2017 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import shlex


def get_version():
    command = 'lsb_release -c'
    result = subprocess.run(shlex.split(command), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, shell=False)
    return result.stdout.decode("utf-8").split(":")[1].strip()


def is_package_installed(package_name):
    command = "flatpak list --app"
    result = subprocess.run(shlex.split(command), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=False)
    output = result.stdout.decode('utf-8')
    return output.find(package_name) > -1


if __name__ == "__main__":
    print(get_version())
    print(is_package_installed("com.github.needleandthread.vocal"))
