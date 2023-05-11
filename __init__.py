#! /usr/bin/python3

"""
/***************************************************************************
 HistoricalMap
                                 A QGIS plugin
 Mapping old forests from historical  maps
                             -------------------
        begin                : 2016-01-26
        copyright            : (C) 2016 by Karasiak & Lomellini
        email                : karasiak.nicolas@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from __future__ import annotations


# noinspection PyPep8Naming
def classFactory(iface: QgsInterface) -> HistoricalMap:
    """Load HistoricalMap class from file HistoricalMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from HistoricalMap.historical_map import HistoricalMap

    return HistoricalMap(iface)
