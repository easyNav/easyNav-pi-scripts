## This script caches maps in the database. ##

## Version number
VERSION = '0.0.2'

import requests
import logging
import time

HOST_ADDR = 'http://127.0.0.1:1337'

def configLogging():
    logging.getLogger('').handlers = []

    logging.basicConfig(
        # filename = "a.log",
        # filemode="w",
        level = logging.INFO)


def resetMap():
    """Resets the map.
    """
    try:
        requests.delete(HOST_ADDR + '/map')
        logging.info('Map deleted.')
    except requests.exceptions.RequestException as e:
        logging.error('Oops!  Failed to delete map.  Is server connected?')


def updateMap(building='<COM></COM>1', floor='2'):
    """Updates the map on server. 
    """
    try:
        requests.get(HOST_ADDR + '/map/update?building=%s&floor=%s' % (building, floor) )
        logging.info('Map updated. building=%s floor=%s' % (building, floor) )
    except requests.exceptions.RequestException as e:
        logging.error('Oops!  Failed to update map building=%s floor=%s.  Is server connected?'% (building, floor) )


def createEdge(source, target, suid, weight=1):
    """Creates an edge.  Useful for linking floors 
    """
    try:
        requests.post(HOST_ADDR + '/edge/?source=%s&target=%s&SUID=%s&weight=1' % (source, target, suid) )
        logging.info('Created edge source=%s target=%s SUID=%s' % (source, target, suid) )
    except requests.exceptions.RequestException as e:
        logging.error('Oops!  Failed to create edge source=%s target=%s SUID=%s.  Is server connected?'% (source, target, suid) )




##############
## Main App ##
##############

configLogging()
logging.info('== Map script updater v%s ==' % VERSION)
resetMap()

## COM1 map ##
updateMap(building='COM1', floor='2')

## COM2 map ##
updateMap(building='COM2', floor='2')
updateMap(building='COM2', floor='3')

## Create edges to link floors and buildings ##

# Inter-building links
createEdge(1231, 221, 'edge0')

# COM1 floor links

# COM2 floor links
createEdge(2216, 2311, 'edge1')
