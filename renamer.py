from glob import glob
import subprocess
from pathlib import Path

# input() handles input better if readline is loaded
# e.g. arrow keys work, and backspace works properly with hangeul input
import readline

def prompt(path):
    transcript = None
    while not transcript:
        subprocess.run(["mplayer", str(path)])
        print('Transcribe the audio (leave blank to hear again)')
        transcript = input('> ')
    return transcript


def pad_filename(filename):
    """
    pyAudioAnalysis adds stuff like "131.700-132.850" and "14.200-26.500" to the output filenames
    this doesn't sort properly because the numbers like 131 and 14 are not padded with zeros.
    """
    time_range = Path(filename).stem.replace('2000-essential-korean-words-', '')
    from_timestamp, to_timestamp = (float(ts) for ts in time_range.split('-'))
    return f'{from_timestamp:08.3f}-{to_timestamp:08.3f}'


if __name__ == '__main__':
    for filepath in sorted(glob('output/*_*-*.wav'), key=pad_filename):
        path = Path(filepath)

        transcript = prompt(path)

        # Clean up any repeated spaces. This is to workaround input issues with iterm2
        transcript = transcript.replace('  ', ' ')

        path.rename(Path(path.parent, f'{path.stem}-{transcript}{path.suffix}'))
