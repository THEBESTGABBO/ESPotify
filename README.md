A simple micropython webserver to play music. Developed for ESP32-WROOM-32.
# Usage
Flash all the files (after inserting your WiFi SSID & Password into boot.py) to your microcontroller and press the "en" button to start execution. Then insert the printed IP address in your browser and start playing music.
# Music info
Due to the little space available in the flash memory of ESP32 the audio files were compressed to mono tracks with 13 kbps bitrate using OPUS codec, this allows to store up to around 20 min of music.
You can replicate this by installing FFmpeg with `apt-get install ffmpeg` and then running `ffmpeg -i input_track.mp3 -ac 1 -c:a libopus -b:a 13k output_track.ogg`.
# Images
![alt text](https://freeimage.host/i/33kGlQn)
