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

Motion Detection With Display
```bash
python3 main.py -m
```

Headless Mode, Motion Detection
```bash
python3 main.py -m -l
```
Headless Mode, Motion Detection, Log to `$PWD`
```bash
python3 main.py -m -l -d $PWD
```

## Playing RTSP Stream with FFmpeg
```bash
# 1080P
ffplay rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream1
```

```bash
# 480P
ffplay rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2
```

If you need even smaller display
```bash
ffplay -vf scale=240:-1 rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2
```

Result:

Installed an IP cam at my door step for this demo

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/04.png "")

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/01.png "")

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/02.png "")

Result with motion detection enabled

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/03.png "")

Old monitor + Raspberry Pi 2B = Clock + CCTV

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/05.png "")

![alt text](https://github.com/hyfung/opencv_rtsp/blob/white/images/06.png "")

## Recording RTSP Stream with FFMpeg
```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 FILENAME.mp4
```

```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 $(date +%Y%m%d_%H%M%S).mp4
```
## Features to add
* ~~Motion detection~~
* ~~Add a motion detection debouncing timer by `time.time()`~~
* Replace `f.write()` with `logger.info()`
* Screenshot on motion detected
* Record for a duration on motion detected
  * Can consider using `subprocess()` and ffmpeg or use VideoWriter
* Notification on motion detected (e.g. Telegram Bot)
  * Request a bot token
  * Add bot token to ENV then retrieve in `main` by `os.environ.get("BOT_TOKEN")`
* Logging of events (Motion, disconnection etc)
  * Local CSV or Webhook to 3rd party HTTP server
