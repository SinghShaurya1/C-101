seconds = int(input('enter time in secs'))
while seconds > 0:
    if seconds < 60:
        mins = 0
    else:
        mins = int(seconds/60)

    secs = int(seconds % 60)

    print(f'{mins}:{secs}')
    seconds -= 1
print('time up')