# Speech splitter

A wrapper for [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) to split audio files around silences.

I wrote it to extract short utterrances from mp3s, for language learning.

## Dependencies

```
pipenv install
```

```
brew install libmagic
```

## Usage
Copy some files to the `input` directory and then run `make`.

Output is written to the `output` directory.

## Contributing

I'm not actively maintaining this project. 🤷‍♂️

Consider contributing to the [upstream library](https://github.com/tyiannak/pyAudioAnalysis).

## License
All code is free to use under the [MIT license](https://opensource.org/licenses/MIT).