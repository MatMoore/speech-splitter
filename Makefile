.PHONY: clean split rename

all: clean split rename

output: clean
	mkdir -p output

split: output
	for file in `ls input/*.mp3` ; do \
		prefix="$${file%.*}" ; \
		pipenv run python -m pyAudioAnalysis.audioAnalysis silenceRemoval --smoothing 1.0 --weight 0.3 -i $${file} ; \
		mv $${prefix}_*-*.wav output ; \
	done; \

rename:
	pipenv run python renamer.py

clean:
	rm -rf output/*
