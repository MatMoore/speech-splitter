.PHONY: clean split

all: clean split

output:
	mkdir -p output

split: output
	for file in `ls input/*.mp3` ; do \
		prefix="$${file%.*}" ; \
		pipenv run python -m pyAudioAnalysis.audioAnalysis silenceRemoval --smoothing 1.0 --weight 0.3 -i $${file} ; \
		mv $${prefix}_*-*.wav output ; \
	done; \

clean:
	rm -rf output/*
