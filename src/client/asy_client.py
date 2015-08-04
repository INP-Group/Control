# -*- encoding: utf-8 -*-

import asyncio
import asyncio.streams
import json


def make_package(command_name, data):
    return json.dumps({
        'command': command_name,
        'data': data
    })


def _clojure_send(writer):
    client_writer = writer

    def send(msg):
        print("> " + msg)
        client_writer.write((msg + '\n').encode("utf-8"))

    return send


def _clojure_recv(reader):
    client_reader = reader

    def recv():
        msgback = (yield from client_reader.readline()).decode("utf-8").rstrip()
        print("< " + msgback)
        return msgback

    return recv


@asyncio.coroutine
def client(loop):
    reader, writer = yield from asyncio.streams.open_connection(
        '127.0.0.1', 12345, loop=loop)

    send = _clojure_send(writer)
    recv = _clojure_recv(reader)
    # send a line

    send(make_package('SUM2', {
        'arg1': 1,
        'arg2': 2
    }))
    msg = yield from recv()

    # send('add 1 2')
    # msg = yield from recv()
    #
    # send("repeat 5 hello")
    # msg = yield from recv()
    # assert msg == 'begin'
    # while True:
    #     msg = yield from recv()
    #     if msg == 'end':
    #         break
    #
    writer.close()
    yield from asyncio.sleep(0.5)


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(client(loop))
    finally:
        loop.close()


if __name__ == '__main__':
    main()