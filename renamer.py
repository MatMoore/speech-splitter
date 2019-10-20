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


if __name__ == '__main__':
    for filepath in sorted(glob('output/*_*-*.wav')):
        path = Path(filepath)

        transcript = prompt(path)

        # Clean up any repeated spaces. This is to workaround input issues with iterm2
        transcript = transcript.replace('  ', ' ')

        path.rename(Path(path.parent, f'{path.stem}-{transcript}{path.suffix}'))
