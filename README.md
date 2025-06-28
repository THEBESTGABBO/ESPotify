A simple micropython webserver to play music. Developed for ESP32-WROOM-32.
# Usage
Insert your WiFi SSID & Password into boot.py.
Flash all the files to your microcontroller and press the "en" button to start execution.
Then insert the IP address that gets printed on the serial interface in your browser and start playing music.
# Music info
Due to the little space available in the flash memory of ESP32 the audio files were compressed to mono tracks with 13 kbps bitrate using OPUS codec, this allows to store up to around 20 min of music.
You can replicate using FFmpeg with `ffmpeg -i input_track.mp3 -ac 1 -c:a libopus -b:a 13k output_track.ogg`.
# Images
![Interface](<https://media-hosting.imagekit.io//5949ddafc56a41f5/Screenshot_20250303-192720.png?Expires=1835703301&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=OQs34YFQIiYmcxrlZq1IWxfjVU5sSnK2nbqWz5N7QCmW-DuceyzahLgA3gAZOjT0Fr01mxxZRnZ5EwSxw19sTWo5reOdjJppI6~fh0gFOqahQwP-bKiPMQLuYL13ZkXG6k5ttOFTd6SllTAKgONNqvU--iEdfdzkJGWJTMPqjJJUYtOMsKeag3uh-HYBJdQxoEWbIvDOt0W-LbQ4WFKBx1FIgy-Ok39NeJx7j-lnrG4auymwi1rOZ7GTn-p4xP0IQ9Kof5i9ugcVlqki1~T6I~b8S4FkLeecAudbD384mVkWfyFjxC32h69jGBGE1eELEODvWiQ9iFmFYVlIUFh~RA__>)
