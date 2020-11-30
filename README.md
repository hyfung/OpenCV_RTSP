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

## Recording RTSP Stream with FFMpeg
```bash
ffmpeg -i rtsp://${C100_USER}:${C100_PASSWORD}@${C100_SERVER}/stream2 FILEMANE.mp4
```
