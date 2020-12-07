# Webcam RTSP with OpenCV and FFMpeg
Sample repo to have fun with TP-Link Tapo C100 IPCAM

## Define environment variables
Add the following lines to your `.bashrc` file or by adding them in your systemd service as `Environment=C100_USER=...`
```bash
export C100_USER=...
export C100_PASSWORD=...
export C100_SERVER=...
```

## Usage
Connects to the cam and display the stream, add `-s 1` to select FHD mode, otherwise 360P is the default (`-s 2`)
```bash
python3 main.py
```

Connects to the cam and display the stream with motion detection
```bash
python3 main.py -m
```

Headless Mode and perform motion detection in the background, does not display the stream
```bash
python3 main.py -m -l
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

Result with motion detection enabled

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/03.png "")

## Recording RTSP Stream with FFMpeg
```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 FILENAME.mp4
```

```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 $(date +%Y%m%d_%H%M%S).mp4
```
## Features to add
* Motion detection
* Screenshot on motion detected
* Record for a duration on motion detected
* Notification on motion detected (e.g. Telegram Bot)
* Logging of events (Motion, disconnection etc)
