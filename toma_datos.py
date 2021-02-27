import argparse
import time
import numpy as np
import random
import csv
import pandas as pd
import cv2
import multiprocessing

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

move=""



def create_df():
    df=pd.DataFrame(columns = ['channel1','channel2','channel3','channel4','move'])

    return (df)

def write_df(df,channel1,channel2,channel3,channel4,move):
    
    df2=pd.DataFrame({'channel1':channel1,'channel2':channel2,'channel3':channel3,'channel4':channel4,'move':move})
    df3=df.append(df2,ignore_index=True)
    return df3
    
def convert_csv(df):
    df.to_csv('prueba3.csv')

def save_data():
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
    time_stream=3.0 #tiempo de toma de datos
    
    while 1==1:
        
        if move!="":
            print('Tomando datos')
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

            #Storage data channel by channel
            channel1=data_arr[:,0]
            channel2=data_arr[:,1]
            channel3=data_arr[:,2]
            channel4=data_arr[:,3]
            #Create and save data in a DataFrames
            df1=create_df()#Create first dataframe
            df2=write_df(df1,channel1,channel2,channel3,channel4,move)
            convert_csv(df2)

        
            board.stop_stream()
        
    board.release_session()

def play_video():
    move=""
    while 1==1:
        numero=np.random.random_integers(1,60)
        print(numero)
        if numero in range(1, 20):
            captura = cv2.VideoCapture('pre_mano.mp4')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
            captura.release()
        
            cv2.destroyAllWindows()
            move="mano"
            captura = cv2.VideoCapture('Grabar.mp4')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
                captura.release()
        
            cv2.destroyAllWindows()
            
        
        elif numero in range(20, 40):
            captura = cv2.VideoCapture('pre_pie')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
                captura.release()
        
            cv2.destroyAllWindows()
            move="pie"
            captura = cv2.VideoCapture('Grabar.mp4')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
                captura.release()
        
            cv2.destroyAllWindows()
        else:
            captura = cv2.VideoCapture('pre_nada.mp4')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
                captura.release()
        
            cv2.destroyAllWindows()
            move="nada"
            captura = cv2.VideoCapture('nada.mp4')
            while (captura.isOpened()):
                ret, imagen = captura.read()
                if ret == True:
                    cv2.imshow('video', imagen)
                    if cv2.waitKey(30) == ord('s'):
                        break
                else: break
                captura.release()
        
            cv2.destroyAllWindows()

class Line:
    def __init__(self):
        global number
        number.get_
    def line_design1(self):
        for i in range(3): 
            number+=2
            print("+"*number)
            
    def line_design2(self):
        for i in range(3): 
            number+=8
            print("#"*number)       

    def pepito(self,data,name=''):
        print(data,data.value)
        data.value+=1
            

def main():
    linea=Line()
    manager=multiprocessing.Manager()
    x=manager.Value('i',0)
    y=multiprocessing.Value('i',0)
    for i in range(5):
        p1=multiprocessing.Process(target=linea.line_design1)
        p2=multiprocessing.Process(target=linea.line_design2)    
        p1.start()
        p2.start() 


    
    

if __name__ == "__main__":

    main()