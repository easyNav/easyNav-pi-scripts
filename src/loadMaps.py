## This script caches maps in the database. ##

## Version number
VERSION = '0.0.1'

import requests
import logging

HOST_ADDR = 'http://127.0.0.1:1337'

def configLogging():
    logging.getLogger('').handlers = []

    logging.basicConfig(
        # filename = "a.log",
        # filemode="w",
        level = logging.DEBUG)


def resetMap():
    """Resets the map.
    """
    try:
        requests.delete(HOST_ADDR + '/map')
        logging.info('Map deleted.')
    except requests.exceptions.RequestException as e:
        logging.error('Oops!  Failed to delete map.  Is server connected?')


def updateMap(building='COM1', floor='2'):
    """Updates the map on server. 
    """
    try:
        requests.get(HOST_ADDR + '/map/update?building=%s&floor=%s' % (building, floor) )
        logging.info('Map updated. building=%s floor=%s' % (building, floor) )
    except requests.exceptions.RequestException as e:
        logging.error('Oops!  Failed to update map building=%s floor=%s.  Is server connected?'% (building, floor) )


##############
## Main App ##
##############

configLogging()
resetMap()

# updateMap(building='COM1', floor='B1')
updateMap(building='COM1', floor='1')
updateMap(building='COM1', floor='2')
updateMap(building='COM1', floor='3')

