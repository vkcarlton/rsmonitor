import socket
import json
import time
import random


def toggleState(target_ip):
    DEVSTATUS_MESSAGE = b'''{"msg":{"cmd":"devStatus","data":{ }}}'''

    # print("UDP target IP: %s" % target_ip)
    # print("UDP target port: %s" % COMMAND_PORT)
    # print("message: %s" % DEVSTATUS_MESSAGE)

    status_sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    status_sock.sendto(DEVSTATUS_MESSAGE, (target_ip, COMMAND_PORT))
    status_sock.close()
    
    
    COMMAND_MESSAGE = ""
    listenData = listen(LISTEN_PORT)
    print(listenData)
    if listenData["msg"]["data"]["onOff"]:
        print("ON > OFF")
        COMMAND_MESSAGE = b'''{"msg":{"cmd":"turn","data":{"value":0}}}'''
    else:
        print("OFF > ON")
        COMMAND_MESSAGE = b'''{"msg":{"cmd":"turn","data":{"value":1}}}'''
    # print(COMMAND_MESSAGE)
    
    command_sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    command_sock.sendto(COMMAND_MESSAGE, (target_ip, COMMAND_PORT))
    command_sock.close()
        
def listen(listen_port):
    listen_sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    listen_sock.bind(("", listen_port))
    listen_sock.settimeout(10)
    
    data, addr = listen_sock.recvfrom(1024) # buffer size is 1024 bytes
    data = json.loads(data.decode())
    if data:
        pass
            # print("received message: " + json.dumps(data))
            # print("from" + json.dumps(addr))
            # print(data["msg"]["data"]["onOff"]) #print(data["data"]["ip"])
    listen_sock.close()
    return data

def changeColor(target_ip, r, g, b):
    colorMessage = f'''{{"msg":{{"cmd":"colorwc","data":{{"color":{{"r":{r},"g":{g},"b":{b}}}}}}}}}'''
    print(colorMessage)
    colorMessage = bytes(colorMessage, "utf-8")
    color_sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    color_sock.sendto(colorMessage, (target_ip, COMMAND_PORT))
    color_sock.close()
    
    
MULTICAST_IP = "239.255.255.250"
MULTICAST_PORT = 4001
LISTEN_PORT = 4002
LIGHT_IP = None
COMMAND_PORT = 4003

MESSAGE = b'''{ "msg": {   "cmd": "scan",   "data": {     "account_topic": "reserve"    }  }}'''



sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.bind(("", LISTEN_PORT))
sock.settimeout(10)

# print("UDP target IP: %s" % MULTICAST_IP)
# print("UDP target port: %s" % MULTICAST_PORT)
# print("message: %s" % MESSAGE)

sock2 = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock2.sendto(MESSAGE, (MULTICAST_IP, MULTICAST_PORT))
sock2.close()

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = json.loads(data.decode())
    if data:
        LIGHT_IP = addr[0]
        sock.close()
        # print("received message: %s" % data)
        # print(data["msg"]["data"]["device"]) #print(data["data"]["ip"])
        break
    
try:
    toggleState(LIGHT_IP)
    time.sleep(2)
    changeColor(LIGHT_IP, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(10):
        time.sleep(.5)
        changeColor(LIGHT_IP, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    time.sleep(2)
    toggleState(LIGHT_IP)
except Exception as e:
    print(e)




# MESSAGE = b'''{"msg":{"cmd":"turn","data":{"value":1}}}'''

# print("UDP target IP: %s" % LIGHT_IP)
# print("UDP target port: %s" % COMMAND_PORT)
# print("message: %s" % MESSAGE)

# sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_DGRAM) # UDP
# sock.sendto(MESSAGE, (LIGHT_IP, COMMAND_PORT))


