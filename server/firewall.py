#!/usr/bin/env python3
#
# Copyright (C) 2018  Maurice van der Pot <griffon26@kfk4ever.com>
#
# This file is part of taserver
#
# taserver is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# taserver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with taserver.  If not, see <http://www.gnu.org/licenses/>.
#

import gevent.subprocess as sp


def modify_gameserver_whitelist(add_or_remove, player, server):
    if add_or_remove not in ('add', 'remove'):
        raise RuntimeError('Invalid argument provided')
    ipstring = '%d.%d.%d.%d' % player.ip
    sp.call('..\\scripts\\modifyfirewall.py whitelist %s %s' %
            (add_or_remove, ipstring), shell=True)


def modify_loginserver_blacklist(add_or_remove, player):
    if add_or_remove not in ('add', 'remove'):
        raise RuntimeError('Invalid argument provided')
    ipstring = '%d.%d.%d.%d' % player.ip
    sp.call('..\\scripts\\modifyfirewall.py blacklist %s %s' %
            (add_or_remove, ipstring), shell=True)
