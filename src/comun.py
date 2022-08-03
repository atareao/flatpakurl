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
import sys


def is_package():
    return __file__.find('src') < 0


APP = 'flatpakurl'
APPNAME = 'flatpakurl'
APP_CONF = APP + '.conf'
# check if running from source
if is_package():
    ROOTDIR = os.path.expanduser('~/.local')
    APPDIR = os.path.join(ROOTDIR, 'share/flatpakurl')
    LANGDIR = os.path.join(ROOTDIR, 'locale-langpack')
    BINDIR = os.path.join(ROOTDIR, 'bin')
    ICONDIR = os.path.join(ROOTDIR, 'share/icons')
    CHANGELOG = os.path.join(APPDIR, 'changelog')
else:
    ROOTDIR = os.path.dirname(__file__)
    LANGDIR = os.path.normpath(os.path.join(ROOTDIR, '../template1'))
    APPDIR = ROOTDIR
    ICONDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/icons'))
    DEBIANDIR = os.path.normpath(os.path.join(ROOTDIR, '../debian'))
    CHANGELOG = os.path.join(DEBIANDIR, 'changelog')
#
ICON = os.path.join(ICONDIR, 'flatpakurl.svg')
#
f = open(CHANGELOG, 'r')
line = f.readline()
f.close()
pos = line.find('(')
posf = line.find(')', pos)
VERSION = line[pos + 1:posf].strip()
if not is_package():
    VERSION = VERSION + '-src'
####

try:
    current_locale, encoding = locale.getdefaultlocale()
    language = gettext.translation(APP, LANGDIR, [current_locale])
    language.install()
    if sys.version_info[0] == 3:
        _ = language.gettext
    else:
        _ = language.ugettext
except Exception as e:
    print(e)
    _ = str
