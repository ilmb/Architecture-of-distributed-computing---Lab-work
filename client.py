import socket
import struct


server_add = ("192.168.56.106", 15000)


def get_num(n):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = struct.pack("q", n)
    sock.connect(server_add)
    sock.sendall(data)
    resp = sock.recv(8)
    sock.close()
    (result, ) = struct.unpack("q", resp)
    return result

def read_num():
    n = input("Enter line number for number: ")
    try:
        n = int(n)
        if n <= 0:
            raise ValueError()
        num = get_num(n)
    except (ValueError, struct.error):
        print("Incorrect input")
        return read_num()
    print("Received", num)
    if n >= 0: 
        return n
    else:
        print("Server returned error. Try again.")
        return read_num()

def read_op():
    o = input("Enter next operation: ")
    if o in "+-*/^":
        return o
    else:
        print("Incorrect input")
        return read_op()

def work(value = 0, op = None):
    num = read_num()

    if op == None:
        value = num
    elif op == "+":
        print(value, "+", num, "=", value + num)
        value += num
    elif op == "-":
        print(value, "-", num, "=", value - num)
        value -= num
    elif op == "*":
        print(value, "*", num, "=", value * num)
        value *= num
    elif op == "/":
        print(value, "/", num, "=", value // num)
        value //= num
    elif op == "^":
        print(value, "^", num, "=", value ** num)
        value **= num
    print("Current result:", value)

    op = read_op()

    work(value, op)

work()
