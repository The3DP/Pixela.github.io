#Text-based animation
import random, os, time

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
width = os.get_terminal_size().columns
rain = [' ']*width

while True:
    rain[random.randint(0, width-1)] = random.choice(chars)
    print(''.join(rain))
    rain = [' ' if random.random() > 0.98 else c for c in rain]
    time.sleep(0.05)
