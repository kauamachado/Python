import emoji
from time import sleep

for c in range(10, -1, - 1):
    sleep(1)
    print(c)
print(emoji.emojize(':tada:', use_aliases=True))
