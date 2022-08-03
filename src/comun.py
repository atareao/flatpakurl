#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of flatpakurl
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

import os
import locale
import gettext


APP = 'flatpakurl'
APPNAME = 'flatpakurl'
APP_CONF = APP + '.conf'
# check if running from source
ROOTDIR = os.path.expanduser('~/.local')
APPDIR = os.path.join(ROOTDIR, 'share/flatpakurl')
LANGDIR = os.path.join(ROOTDIR, 'locale-langpack')
BINDIR = os.path.join(ROOTDIR, 'bin')
ICONDIR = os.path.join(ROOTDIR, 'share/icons/flatpakurl')
CHANGELOG = os.path.join(APPDIR, 'changelog')
ICON = os.path.join(ICONDIR, 'flatpakurl.svg')

f = open(CHANGELOG, 'r')
line = f.readline()
f.close()
pos = line.find('(')
posf = line.find(')', pos)
VERSION = line[pos + 1:posf].strip()

try:
    current_locale, encoding = locale.getdefaultlocale()
    language = gettext.translation(APP, LANGDIR, [current_locale])
    language.install()
    _ = language.gettext
except Exception as e:
    print(e)
    _ = str
