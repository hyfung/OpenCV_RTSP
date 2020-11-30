# Webcam RTSP with OpenCV and FFMpeg
Sample repo to have fun with TP-Link Tapo C100 IPCAM

## Define environment variables
```bash
export C100_USER=...
export C100_PASSWORD=...
export C100_SERVER=...
```

## Usage
```bash
python3 main.py
```

## Playing RTSP Stream with FFmpeg
```bash
ffplay rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream1
```

```bash
ffplay rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2
```
Result:

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/01.png "")

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/02.png "")

## Recording RTSP Stream with FFMpeg
```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 FILENAME.mp4

ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 $(date +%Y%m%d_%H%M%S).mp4
```
## Features to add
* Motion detection
* Screenshot on motion detected
* Record for a duration on motion detected
* Notification on motion detected (e.g. Telegram Bot)
* Logging of events (Motion, disconnection etc)
