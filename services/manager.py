# -*- encoding: utf-8 -*-
import os

import subprocess

from nameko.rpc import rpc

from project.settings import VENV_PYTHON, BASE_DIR


class ProcessManagerService(object):
    name = "process_manager"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

    @rpc
    def run_test(self):
        os.chdir(BASE_DIR)
        command = "cd {} && {} -m {}".format(
            BASE_DIR,
            VENV_PYTHON,
            'src.server'
        )
        subprocess.Popen(command, shell=True)
