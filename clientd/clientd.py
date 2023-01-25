import os
import zmq
import logging

logging.basicConfig(filename="output.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info("Starting ZeroMQ Client ...")

context = zmq.Context()
socket = context.socket(zmq.PULL)
address = os.environ.get('SERVER_CONNECT_URI')
socket.connect(address)
logging.info("Listening to {}...".format(address))
while True:
    message = socket.recv_string()
    logging.info("Client got message! {}".format(message))
