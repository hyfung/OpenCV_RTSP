#!/usr/bin/python3
import argparse
import os
import cv2
import numpy
import threading
import time

# Throws an error if environment variables weren't defined
USERNAME = os.environ['C100_USER']
PASSWORD = os.environ['C100_PASS']
SERVER = os.environ['C100_IP']

# URI Format for Tapo C100
rtsp_1080p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream1'
rtsp_360p = f'rtsp://{USERNAME}:{PASSWORD}@{SERVER}/stream2'

# Store the URIs in a dictionary to be addressed by 1 or 2
streams = {
    1: rtsp_1080p,
    2: rtsp_360p,
}

# Define 2 variable to store the frames
img = None
last = None

# Define a variable to store the recording thread if implemented in future
record_thread = None

# Define a timestamp for debouncing
last_detect = int(time.time())

def time_to_string():
    """
    Returns a string of current time suitable for filenames
    20180914_234000
    """
    return str(time.strftime('%Y%m%d_%H%M%S'))

def time_to_string_human():
    """
    Returns a human readible string of current time
    2018-09-14 23:40:00
    """
    return str(time.strftime('%Y-%m-%d %H:%M:%S'))

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
    ap.add_argument("-d", "--dir", help="Directory to save CSV, JPG and AVI", type=str,)
    ap.add_argument("-m", "--motion", help="Enable motion detection, directory must be provided", action="store_true")
    ap.add_argument("-r", "--record", help="Record an AVI on motion detected", action="store_true")
    ap.add_argument("-l", "--headless", help="Perform detection in background, do not display a window", action="store_true")
    args = vars(ap.parse_args())

    if args['motion'] and args['dir']:
        # If logging is specified
        motion_log = open(os.path.join(args['dir'], 'log.txt'), 'a+')

    # Recording will be done in detection algorithm
    # We just check if the directory is defined properly
    if args['record']:
        if args['dir'] is None:
            raise AssertionError("DIR should not be none")

    if  args['test']:
        # Test locally with webcam
        cap = cv2.VideoCapture(0)
    else:
        # Open a RTSP stream targeting the IP cam
        cap = cv2.VideoCapture(streams[args['src']])

    # Prime "last" by reading a frame (Reference Frame)
    ret, last = cap.read()

    # Convert it to grayscale image
    last = cv2.cvtColor(last, cv2.COLOR_BGR2GRAY)

    # Prime "img" by reading a frame (Current Frame)
    ret, img = cap.read()


    while True:
        ret, img = cap.read()

        if args['motion']:
            # Obtain a current frame
            cur_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur it to reduce noise
            cur_gray = cv2.blur(cur_gray, (5,5))
            # Calculate absolute difference
            diff = cv2.absdiff(cur_gray, last)
            # Timer Dimension for 360p: (230, 28)
            # Draw a black rectangle to mask the timer
            cv2.rectangle(diff, (0, 0), (231, 27), (0 ,0, 0), -1)

            # ROI: X > 400
            # ROI: Y > 71 and Y < 335

            # Simple motion detection by thresholding
            # Try to change the threshold to tune performance
            ret, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

            # Display the image if not headless mode
            if not args["headless"]:
                cv2.imshow('motion', diff)

            # Calculate "Motion Score" to filter noise
            # Criteria: Number of contours detected
            contours, hierarchy = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # The first comparison returns length of 350-500 which is false positive
            # Set (3, 250) as detection criteria
            if len(contours) > 3 and len(contours) < 250:
                print(len(contours))
                print("Motion detected")
                
                # If this detect is 10 seconds older than previous one, then fire the events
                if (time.time() - last_detect) > 10:
                    # Update the timer
                    last_detect = int(time.time())
                    if args['dir']:
                        motion_log.write(time_to_string() + '\n')
                    if args['record']:
                        # Use the VideoWriter Object or
                        # Spawn a subprocess asynchronously to record for 10 seconds
                        # Spawn a thread and kill it after 10 seconds
                        pass

            # Updating the reference frame
            last = cur_gray

        # Display the image if not headless mode
        if not args["headless"]:
            cv2.imshow('mat', img)

        # Without an X-session, waitKey() immediately returns -1
        # Should think about how to hold the thread for a bit longer
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Instead of waitKey(), we hang the thread with time.sleep()
        time.sleep(1/30)

if __name__ == '__main__':
    main()
