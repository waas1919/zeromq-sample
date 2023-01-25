import os
import zmq
import time
import logging

logging.basicConfig(filename="output.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info("Starting ZeroMQ Server ...")

context = zmq.Context()
socket = context.socket(zmq.PUSH)
address = os.environ.get('SERVER_LISTEN_URI')
socket.bind(address)
logging.info("Sending to {}...".format(address))
counter = 0
while True:
    msg = "Got it: {0}".format(counter)
    counter = counter + 1
    message = socket.send_string(msg)
    logging.info("Sent message: '{0}'".format(msg))
    time.sleep(1)
