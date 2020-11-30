#!/usr/bin/python3
import argparse
import os
import cv2
import numpy

USERNAME = os.environ.get('C100_USER')
PASSWORD = os.environ.get('C100_PASS')
SERVER = os.environ.get('C100_IP')

rtsp_1080p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream1'
rtsp_360p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream2'

streams = {
    1: rtsp_1080p,
    2: rtsp_360p,
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--src", help="Resolution: 1=1080p, 2=360p", type=int, default=2)
    ap.add_argument("-f", "--file", help="file name to save to", type=str)
    args = vars(ap.parse_args())

    cap = cv2.VideoCapture(streams[args['src']])
    
    if args['file']:
        #TODO: Create VideoWriter object to write frames to
        pass
    
    while True:
        ret, img = cap.read()
        cv2.imshow('mat', img)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break    
        

if __name__ == '__main__':
    main()
