from pyOpenBCI import OpenBCIGanglion

def print_raw(sample):
    print(sample.channels_data)

board = OpenBCIGanglion(mac=None)

board.start_stream(print_raw)