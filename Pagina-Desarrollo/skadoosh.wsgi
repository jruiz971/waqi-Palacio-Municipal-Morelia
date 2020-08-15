#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/vdelaluz/git/waqi-Palacio-Municipal-Morelia/Pagina-Desarrollo/')
from skadoosh import app as application
application.secret_key = 'nosiginificanadasoloandressabe'
