def web_page():
    html = """
    <html>
    <head> 
        <title>ESPotify</title> 
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,"> 
        <style>
            body {
              background-color: #181818;
            }
            html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center; }
            h1 { color: #1DB954; padding: 2vh; text-shadow: 0 0 15px #fff}
            p { font-size: 1rem; color: #fff}
            audio {
                width: 95%;
                height: 60px;
                background: #2a2a2a;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 7px;
                padding: 10px;
                box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.4);
            }

            audio::-webkit-media-controls-panel {
                background-color: #1DB954;
                border-radius: 30px;
            }

            audio::-webkit-media-controls-play-button,
            audio::-webkit-media-controls-pause-button {
                filter: invert(0); /* White icons */
            }

            audio::-webkit-media-controls-timeline {
                color: #1DB954; /* Spotify green */
            }

            audio::-webkit-media-controls-current-time-display,
            audio::-webkit-media-controls-time-remaining-display {
                color: #000000;
            }

            audio::-webkit-media-controls-volume-slider {
                background: #1DB954;
                border-radius: 5px;
            }

            audio::-webkit-media-controls-seek-back-button,
            audio::-webkit-media-controls-seek-forward-button {
                filter: invert(1);
            }
            div{
            display: flex;
            width: 90%;
            margin: auto;
            flex-direction: column;
            }
            div:after {
                content: " ";
                display: block;
                margin-top: 10px;
                border-bottom: 2px solid #666666;
                align-items: left;
            }
            footer {
              text-align: left;
              padding: 3px;
              color: white;
            }
        </style>
    </head>
    <body>
        <img src="/ESPotify-03-03-2025.png" alt="ESPotify" width="50%">
        <div>
            <p style="text-align: left;">
                <span style="font-size: 1rem;"><strong>Tomorrow</strong></span>
                <br>
                <span style="font-size: 0.75rem;">by Tyler, The Creator</span>
            </p>
            <audio controls>
                <source src="/Tomorrow.ogg" type="audio/ogg">
                Your browser does not support the audio element.
            </audio>
        </div>
        <div>
            <p style="text-align: left;">
                <span style="font-size: 1rem;"><strong>All Mine</strong></span>
                <br>
                <span style="font-size: 0.75rem;">by Kanye West</span>
            </p>
            <audio controls>
                <source src="/All_Mine.ogg" type="audio/ogg">
                Your browser does not support the audio element.
            </audio>
        </div>

        <div>
            <p style="text-align: left;">
                <span style="font-size: 1rem;"><strong>No Church In The Wild</strong></span>
                <br>
                <span style="font-size: 0.75rem;">by Kanye West</span>
            </p>
            <audio controls>
                <source src="/No_Church_In_The_Wild.ogg" type="audio/ogg">
                Your browser does not support the audio element.
            </audio>
        </div>

        <div>
            <p style="text-align: left;">
                <span style="font-size: 1rem;"><strong>Not Like Us</strong></span>
                <br>
                <span style="font-size: 0.75rem;">by Kendrick Lamar</span>
            </p>
            <audio controls>
                <source src="/Not_Like_Us.ogg" type="audio/ogg">
                Your browser does not support the audio element.
            </audio>
        </div>

        <div>
            <p style="text-align: left;">
                <span style="font-size: 1rem;"><strong>Space Cadet (feat. Gunna)</strong></span>
                <br>
                <span style="font-size: 0.75rem;">by Metro Boomin</span>
            </p>
            <audio controls>
                <source src="/Space_Cadet.ogg" type="audio/ogg">
                Your browser does not support the audio element.
            </audio>
        </div>

        <footer>
            <p>Used space: """+str(sum(os.stat('/songs' + '/' + f)[6] for f in os.listdir('/songs') if not os.stat('/songs' + '/' + f)[0] & 0x4000) // 1024) + "kb"+ " ~" + str(sum(os.stat('/songs' + '/' + f)[6] for f in os.listdir('/songs') if not os.stat('/songs' + '/' + f)[0] & 0x4000)//1625//60)+"min"+"""</p>
            <p>Free space: """+str(os.statvfs("/")[4]*4096/1024)+"kb"+ " ~" + str(round(os.statvfs("/")[4]*4096//1625/60, 2))+"min"+"""</p>
        </footer>
    </body>
    </html>
    """
    return html

import socket
import os

# Initialize socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Serve .ogg file
def serve_ogg_file(conn, file):
    try:
        file_size = os.stat(file)[6]
        with open(file, 'rb') as f:
            conn.send('HTTP/1.1 200 OK\r\n')
            conn.send('Content-Type: audio/ogg\r\n')
            conn.send(f'Content-Length: {file_size}\r\n')
            conn.send('Connection: close\r\n\r\n')
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                conn.sendall(chunk)
    except OSError as e:
        print(e)
        conn.send('HTTP/1.1 404 Not Found\r\n')
        conn.send('Connection: close\r\n\r\n')
    finally:
            try:
                conn.close()
            except:
                pass

# Main server loop
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024).decode('utf-8')
    print('Content = %s' % request)
    
    if '/Tomorrow.ogg' in request:
        serve_ogg_file(conn, '/songs/Tomorrow.ogg')
    elif '/All_Mine.ogg' in request:
        serve_ogg_file(conn, '/songs/All Mine.ogg')
    elif '/No_Church_In_The_Wild.ogg' in request:
        serve_ogg_file(conn, '/songs/No Church In The Wild.ogg')
    elif '/Not_Like_Us.ogg' in request:
        serve_ogg_file(conn, '/songs/Not Like Us.ogg')
    elif '/Space_Cadet.ogg' in request:
        serve_ogg_file(conn, '/songs/Space Cadet.ogg')
    elif '/ESPotify-03-03-2025.png' in request:
        try:
            with open('/ESPotify-03-03-2025.png', 'rb') as f:
                conn.send('HTTP/1.1 200 OK\r\n')
                conn.send('Content-Type: image/png\r\n')
                conn.send('Connection: close\r\n\r\n')
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    conn.sendall(chunk)
        except OSError:
            conn.send('HTTP/1.1 404 Not Found\r\n')
            conn.send('Connection: close\r\n\r\n')
    else:
        response = web_page()
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('Connection: close\r\n\r\n')
        conn.sendall(response)
    
