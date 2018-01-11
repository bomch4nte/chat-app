#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#


def send(sock, data):
    data = base64.b64encode(data)
    data = struct.pack('>I', len(data)) + data

    sock.send(data)

def _recv_raw_data(sock, buf):
    data = ''

    while len(data) < buf:
        packet = sock.recv(buf - len(data))

        if not packet:
            break

        data += packet

    return data

def recv(sock):
    data_len = _recv_raw_data(sock, 4)

    if not data_len:
        return None
    else:
        data_len = struct.unpack('>I', data_len)[0]

    raw_data = _recv_raw_data(sock, data_len)
    return base64.b64decode(raw_data)
