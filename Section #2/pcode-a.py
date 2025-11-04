# Text-based animation
import time, sys

spinner = ['|', '/', '-', '\\']
while True:
    for frame in spinner:
        sys.stdout.write(f'\r{frame} Loading...')
        sys.stdout.flush()
        time.sleep(0.1)
