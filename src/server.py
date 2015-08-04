# -*- encoding: utf-8 -*-

# import time
# from project.settings import log_debug
#
# def main():
#     i = 0
#
#     while i < 500:
#         time.sleep(0.01)
#         i += 1
#         log_debug(i)
#
# if __name__ == '__main__':
#     main()

import asyncio


@asyncio.coroutine
def echo_server():
    yield from asyncio.start_server(handle_connection, 'localhost', 8000)


@asyncio.coroutine
def handle_connection(reader, writer):
    while True:
        data = yield from reader.read(8192)
        if not data:
            break

        writer.write(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(echo_server())
try:
    loop.run_forever()
finally:
    loop.close()
