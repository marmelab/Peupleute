## Peupleute

Analysis and identification of bird sounds with Python.

### Requirements

- Python 3.x

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

Then open your browser at http://localhost:8888/notebooks/birdnet.ipynb

### Identification

To identify birds in a record, you can use the birdnet model using:

```sh
cd birdnet && python analyze.py --i '../songs/pic-vert.wav'
```

And then read the result in the generated `result.csv` file.

### Test model

You can test the birdnet model against a bunch of recording of bird songs by following these steps.

First, you have to download some bird songs, you can use the `dowload_bird_songs.py` for it. Feel free to update the list of birds you want to get records from.

```
cd birdnet && python dowload_bird_songs.py
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

```
cd birdnet && python analyze.py
```
