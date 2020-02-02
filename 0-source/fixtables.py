#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!c:/Python27/python.exe
# pylint: disable=line-too-long
'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from os import listdir
fullpathlist = list()
MDfolderpath = "/Users/mp/Library/Mobile Documents/com~apple~CloudDocs/malcprentice.github.io/0-source/"
filelist = listdir(MDfolderpath)
for item in filelist:
    if item.endswith("md"):
        fullpath = MDfolderpath+item
        fullpathlist.append(fullpath)
#FIX ALL TABLES WITHOUT LEADING |
"""
for item in fullpathlist:
    tablefucked = 0
    linelist = list()
    with open(item, "r") as f:
        for line in f:
            if "|" in line:
                tablefucked += 1
                if not line.startswith("|"):
                    line = "|"+line
                    linelist.append(line)
                else:
                    linelist.append(line)
            else:
                linelist.append(line)
    if tablefucked > 1:
        with open(item, "w") as f:
            for line in linelist:
                f.write(line)
"""

for item in fullpathlist:
    with open(item, "r") as f:
        for line in f:
            if line.startswith("    "):
                print(item)

