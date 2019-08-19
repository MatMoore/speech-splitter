.PHONY: clean split

all: clean split

output:
	mkdir -p output

split: output
	pipenv run python -m pyAudioAnalysis.audioAnalysis --help

clean:
	rm -rf output/*
