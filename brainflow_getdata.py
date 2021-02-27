import argparse
import time
import numpy as np
import csv


import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations



def main():
    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                        default=0)
    parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False,
                        default=0)
    parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='')
    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
    parser.add_argument('--streamer-params', type=str, help='streamer params', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
                        required=True)
    parser.add_argument('--file', type=str, help='file', required=False, default='')
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file

    board = BoardShim(args.board_id, params)
    board.prepare_session()
    time_stream=float(3)#tiempo de toma de datos
    # board.start_stream () # use this for default options
    board.start_stream(45000, args.streamer_params)
    time.sleep(time_stream) #Tiempo en el que la ganglion toma datos - debe ser 3s
    egg_channels=board.get_eeg_channels(1)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    datos=int(time_stream/(1/200))
    # at 3 seconds that generate 600 samples by each channel
    # have to create a zeros array of 600 F,4 Columns
    data_arr=np.zeros((datos,4))
    for channels in egg_channels:
        for i in range(datos):
            data_arr[i,channels-1]=data[channels,i] #Se inicia desde channels-1 dado a que al primer dato no es de la adquisicion

    print(data)
    print('///////////////')
    print(data_arr)
    '''
    # crear conexion con base de datos
    conexion=sql.connect(host='localhost',user='root',password='0',database='prueba1')
    cursor=conexion.cursor()
    consulta="INSERT INTO prueba1 (channel1,channel2,channel3,channel4,action) VALUES(%s,%s,%s,%s)"
    for i in range(data_arr):
        cursor.execute(consulta,(data_arr[i,0],data_arr[i,1],data_arr[i,2],data_arr[i,3],'accion'))
    
    cursor.fetchall()
        conexion.commit()
    conexion.close()
    '''
    board.stop_stream()
    board.release_session()



if __name__ == "__main__":
    main()