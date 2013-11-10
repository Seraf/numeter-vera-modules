#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: setup.py,v 0.2.3.4 2013-02-27 09:56:56 gaelL Exp $
#
# Copyright (C) 2010-2013  Gaël Lambert (gaelL) <gael@gael-lambert.org>
#
# Numeter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup


if __name__ == '__main__':

    setup(name='numeter-vera-module',
          version='0.0.4',
          description='Numeter Veras Poller module',
          long_description="""A Vera module for Numeter poller.""",
          author='Julien Syx',
          author_email='julien@syx.fr',
          maintainer='Julien Syx',
          maintainer_email='julien@syx.fr',
          keywords=['numeter','graphing','poller','vera','homeautomation'],
          url='https://github.com/Seraf/numeter-vera-module',
          license='MIT',
          packages = [''],
          package_data={'': ['veraModule.py']},
          classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: Advanced End Users',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              'Topic :: System :: Monitoring'
          ],
         )
