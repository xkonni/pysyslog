import time
import socket
import sys

IP = "0.0.0.0"
PORT = 8514
BUFFERSIZE = 1024
# log to file
# FILE_PRE = "syslog_"
# FILE_POST = ".log"

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((IP, PORT))


def main():
    while (True):
        # log to file
        # FILE = f"{FILE_PRE}{time.strftime('%Y%m%d')}{FILE_POST}"

        bytesAddressPair = UDPServerSocket.recvfrom(BUFFERSIZE)
        message = bytesAddressPair[0].decode().replace("\r", "").replace("\n", "")
        address = bytesAddressPair[1]
        # log to file
        # with open(FILE, 'a') as f:
        #     f.write(f"{message}\n")

        # print to stderr
        print(message, file=sys.stderr)


if __name__ == "__main__":
    main()
