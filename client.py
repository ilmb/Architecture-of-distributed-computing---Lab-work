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

op = None
value = 0
while True:
    while True:
        n = input("Enter line number for number: ")
        try:
            n = int(n)
            if n <= 0:
                raise ValueError()
            num = get_num(n)
        except (ValueError, struct.error):
            print("Incorrect input")
            continue
        print("Received", num)
        if n >= 0: 
            break
        else:
            print("Server returned error. Try again.")

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

    while True:
        op = input("Enter next operation: ")
        if op in "+-*/^":
            break
        else:
            print("Incorrect input")
            continue

       