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

img = None

def record_on_motion():
    """
    Sibling thread to record for 30 seconds on motion detected
    """
    global is_recording
    is_recording = True
    filename = ".avi"
    cv2.VideoWriter()
    while elapsed < 30:


    pass

def main():
    should_record = False

    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--src", help="Resolution: 1=1080p, 2=360p", type=int, default=2)
    ap.add_argument("-f", "--file", help="file name to save to", type=str)
    ap.add_argument("-m", "--motion", help="Enable motion detection", action="store_true")
    ap.add_argument("-r", "--record-on-motion", help="Record an AVI on motion detected", action="store_true")
    ap.add_argument("-l", "--headless", help="Do not show frame", action="store_true")
    args = vars(ap.parse_args())

    cap = cv2.VideoCapture(streams[args['src']])
    
    if args['file']:
        #TODO: Create VideoWriter object to write frames to
        pass
    
    while True:
        global img
        ret, img = cap.read()
        
        if args['motion']:
            # Motion Detection Algorithm, based on previous 5 frames

            # Calculate "Motion Score" to filter noise

            if should_record:
                record_thread = threading.Thread(record_on_motion)
                record_thread.start()
            pass

        if not args["headless"]:
            cv2.imshow('mat', img)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break    
        

if __name__ == '__main__':
    main()
