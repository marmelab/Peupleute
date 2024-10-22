## Peupleute

Analysis and identification of bird sounds with Python.

### Requirements

- Python 3.9.x

### Installing Dependencies

Installation is as simple as:

```sh
    pip install -r requirements.txt
```

### Notebook

To browse the notebook just run the following command:

```sh
    jupyter notebook
```

Then open your browser at http://localhost:8888/notebooks/notebooks/birdnet.ipynb

### Identification

To identify birds in a record, you can use the birdnet model using:

```sh
    cd birdnet && python analyze.py --i '../notebooks/songs/pic-vert.wav'
```

And then read the result in the generated `result.csv` file.

### Test model

You can test the birdnet model against a bunch of recording of bird songs by following these steps.

First, you have to download some bird songs, you can use the `dowload_bird_songs.py` for it. Feel free to update the list of birds you want to get records from.

```sh
    python dowload_bird_songs.py
```

Otherwise you can just add manually new songs, following this directory structure:

```
- dataset
    - audio
        - HouseSparrow
            - song1.mp3
            - song2.mp3
        - CommonStarling
            - song1.mp3
            - song2.mp3
```

And then test the model against the recordings:

```sh
    python test_model.py
```

> **_NOTE:_** You should name the bird using the vernacular name or scientific name used in the `birdnet/model/labels.txt` file.

### REST API

To start the server that allows bird songs identification throught a REST API, you have to start the server using:

```sh
    fastapi dev ./api/main.py
```

And then make a `POST` request on the http://localhost:8080/identify/ passing a `record` file. You can use http://localhost:8080/docs or Bruno to make the request using an interface.

### TODO

- Try using this tensorflow model into a web browser: https://www.tensorflow.org/js/tutorials/conversion/import_saved_model?hl=fr
- Train the model with new species
- Display a Fourier Transform using Matplotlib
- Implement the MFCCs algorithm and test it against the dataset
- Try other models
  Up to date (and heavier) birdnet model: https://github.com/kahst/BirdNET-Analyzer
  https://github.com/gojibjib/jibjib-model
  https://huggingface.co/dima806/bird_sounds_classification
  https://huggingface.co/dennisjooo/Birds-Classifier-EfficientNetB2
