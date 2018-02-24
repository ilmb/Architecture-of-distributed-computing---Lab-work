import socket
import struct


address = ('', 15000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)
sock.listen(1)


def serve():
    conn, addr = sock.accept()
    recv = conn.recv(8)
    print("Received:", recv, "from", addr)
    try:
        line, = struct.unpack("q", recv)
    except:
        conn.close()
        return serve()
    err = False
    num = 0
    try:
        with open("nums.txt", "r") as nums_file:
            num_s = nums_file.readlines()[line - 1]
        num = int(num_s)
    except:
        err = True
    data = struct.pack("q", -1 if err else num)
    conn.send(data)
    conn.close()
    print("Sent", data)
    serve()

serve()
