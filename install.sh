#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

mkdir -p ~/.local/bin/
cp ./bin/flatpakurl ~/.local/bin/
chmod +x ~/.local/bin/flatpakurl
mkdir -p ~/.local/share/flatpakurl/
cp ./src/*.py ~/.local/share/flatpakurl/
cp ./data/flatpakurl.desktop ~/.local/share/applications/
sed  -i "s/{{HOME}}/\/home\/$USER/g" ~/.local/share/applications/flatpakurl.desktop
update-desktop-database ~/.local/share/applications
cp ./debian/changelog ~/.local/share/flatpakurl/
mkdir -p ~/.local/share/icons/flatpakurl/
cp ./data/icons/* ~/.local/share/icons/flatpakurl/
