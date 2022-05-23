def transform(m):
    for a, b in zip(["A#", "C#", "D#", "F#", "G#"], ["T", "U", "I", "O", "P"]):
        m = m.replace(a, b)
    return m


def timeCalc(start, end):
    start_m = int(start[:2]) * 60 + int(start[3:])
    end_m = int(end[:2]) * 60 + int(end[3:])
    return end_m - start_m


def editSongLength(time, song):
    if len(song) == time:
        return song
    elif len(song) > time:
        return song[:time]
    else:
        edited_song = []
        for i in range(time):
            idx = i % len(song)
            edited_song.append(song[idx])
        return ''.join(edited_song)


def containSubMelody(m, song):
    if m in song:
        return True
    else:
        return False


def solution(m, musicinfos):
    candidate = []
    for i in musicinfos:
        split = i.split(',')
        start, end, title, melody = split[0], split[1], split[2], split[3]
        playTime = timeCalc(start, end)
        melody = transform(melody)
        edit = editSongLength(playTime, melody)
        if containSubMelody(transform(m), edit):
            candidate.append([title, len(edit)])
    if len(candidate) == 0:
        return "(None)"
    else:
        candidate.sort(key=lambda x: x[1],reverse=True)
        return candidate[0][0]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
