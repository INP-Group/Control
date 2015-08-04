# -*- encoding: utf-8 -*-

import sys
import asyncio
import asyncio.streams

def main():
    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def client():
        reader, writer = yield from asyncio.streams.open_connection(
            '127.0.0.1', 12345, loop=loop)

        def send(msg):
            print("> " + msg)
            writer.write((msg + '\n').encode("utf-8"))

        def recv():
            msgback = (yield from reader.readline()).decode("utf-8").rstrip()
            print("< " + msgback)
            return msgback

        # send a line
        send("add 1 2")
        msg = yield from recv()

        send("repeat 5 hello")
        msg = yield from recv()
        assert msg == 'begin'
        while True:
            msg = yield from recv()
            if msg == 'end':
                break

        writer.close()
        yield from asyncio.sleep(0.5)

    # creates a client and connects to our server
    try:
        loop.run_until_complete(client())
    finally:
        loop.close()


if __name__ == '__main__':
    main()