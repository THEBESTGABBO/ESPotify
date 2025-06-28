A simple micropython webserver to play music. Developed for ESP32-WROOM-32.
# Usage
1) Insert your WiFi SSID & Password into boot.py
2) Flash all the files except `Screenshot_20250303-192720.png` to your microcontroller and press the "en" button to start execution.
3) Insert the IP address that gets printed on the serial interface in your browser and start playing music.
# Music info
Due to the little space available in the flash memory of ESP32 the audio files were compressed to mono tracks with 13 kbps bitrate using OPUS codec, this allows to store up to around 20 min of music.
You can replicate using FFmpeg with `ffmpeg -i input_track.mp3 -ac 1 -c:a libopus -b:a 13k output_track.ogg`.
# Images
![Interface](<Screenshot_20250303-192720.png>)
