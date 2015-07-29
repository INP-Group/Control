# -*- encoding: utf-8 -*-
import os


LOG = True



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


VENV_FOLDER = '/home/warmonger/Develop/venv/inp_control'
VENV_PYTHON = os.path.join(VENV_FOLDER, 'bin/' 'python')



MEDIA_FOLDER = os.path.join(BASE_DIR, 'media')
LOG_FOLDER = os.path.join(MEDIA_FOLDER, 'logs')

from project.functions import *


folders = [MEDIA_FOLDER,
           LOG_FOLDER,
           ]

[check_and_create(x) for x in folders]


try:





    from project.logs import *
    from project.local_settings import *
except ImportError as e:
    print(e)
