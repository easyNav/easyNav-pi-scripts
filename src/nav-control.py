## Script to control Navigation

import sys
from easyNav_pi_dispatcher import DispatcherClient
import time

arg = sys.argv[1:]

if (len(arg) != 1):
    print 'Error.  Invalid arguments.'
    sys.exit(1)

command = arg[0]

DISPATCHER_PORT = 9100
_dispatcherClient = DispatcherClient(port=DISPATCHER_PORT)
_dispatcherClient.start()

### Reset
if (command == 'reset'):
    _dispatcherClient.send(9001, 'reset', {})
    _dispatcherClient.send(9002, 'reset', {})

### Pause
elif (command == 'pause'):
    _dispatcherClient.send(9001, 'pause', {})

### Unpause
elif (command == 'unpause'):
    _dispatcherClient.send(9001, 'unpause', {})

_dispatcherClient.stop()
