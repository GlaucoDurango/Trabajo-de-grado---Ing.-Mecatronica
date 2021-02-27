from pyOpenBCI import OpenBCIGanglion
import numpy as np

def print_raw(sample):
    print(sample.start_time)

def return_data(sample):
    print (sample.id)

board = OpenBCIGanglion(mac=None)

board.start_stream(return_data)

#print(board.find_mac)