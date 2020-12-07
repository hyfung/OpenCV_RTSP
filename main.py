#!/usr/bin/python3
import argparse
import os
import cv2
import numpy
import threading

# Throws an error if environment variables weren't defined
USERNAME = os.environ['C100_USER']
PASSWORD = os.environ['C100_PASS']
SERVER = os.environ['C100_IP']

# URI Format for Tapo C100
rtsp_1080p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream1'
rtsp_360p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream2'

streams = {
    1: rtsp_1080p,
    2: rtsp_360p,
}

img = None
last = None
record_thread = None

def record_on_motion():
    """
    Sibling thread to record for 30 seconds on motion detected
    This thread should be called by threading.Thread(record_on_motion)
    """
    global is_recording
    is_recording = True
    filename = ".avi"
    cv2.VideoWriter()
    while elapsed < 30:
        pass

def main():
    global img
    should_record = False

    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--src", help="Stream Resolution: 1=1080p, 2=360p", type=int, default=2)
    ap.add_argument("-t", "--test", help="Test with local camera",  action="store_true")
    ap.add_argument("-f", "--file", help="file name to save to", type=str)
    ap.add_argument("-m", "--motion", help="Enable motion detection", action="store_true")
    ap.add_argument("-r", "--record-on-motion", help="Record an AVI on motion detected", action="store_true")
    ap.add_argument("-l", "--headless", help="Do not show frame", action="store_true")
    args = vars(ap.parse_args())

    if  args['test']:
        # Test locally with webcam
        cap = cv2.VideoCapture(0)
    else:
        # Open a RTSP stream targeting the IP cam
        cap = cv2.VideoCapture(streams[args['src']])

    # Prime "last" by readine a reference frame
    ret, last = cap.read()
    # Convert it to grayscale image
    last = cv2.cvtColor(last, cv2.COLOR_BGR2GRAY)

    # Prime "img" by reading a frame
    ret, img = cap.read()

    if args['file']:
        #TODO: Create VideoWriter object to write frames to
        pass

    while True:
        ret, img = cap.read()

        if args['motion']:
            cur_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cur_gray = cv2.blur(cur_gray, (5,5))
            diff = cv2.absdiff(cur_gray, last)

            # Timer Dimension for 360p: (230, 28)
            # Draw a black rectangle to mask the timer
            cv2.rectangle(diff, (0, 0), (231, 27), (0 ,0, 0), -1)

            # ROI: X > 400
            # ROI: Y > 71 and Y < 335

            # Simple motion detection by thresholding
            ret, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

            # Calculate "Motion Score" to filter noise

            cv2.imshow('motion', diff)

            if should_record:
                record_thread = threading.Thread(record_on_motion)
                record_thread.start()

            last = cur_gray

        if not args["headless"]:
            cv2.imshow('mat', img)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
