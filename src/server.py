# -*- encoding: utf-8 -*-

import time
from project.settings import log_debug

def main():
    i = 0

    while i < 500:
        time.sleep(0.01)
        i += 1
        log_debug(i)

if __name__ == '__main__':
    main()