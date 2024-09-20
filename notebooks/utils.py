from os import listdir,path
from os.path import isfile, join
import simpleaudio as sa

def loadWavFile(filepath):
    wav = sa.WaveObject.from_wave_file(filepath)
    wav.filepath = filepath
    if wav.num_channels != 1:
        raise Exception('The file located at '+filepath+' is not in mono.')
    return wav

def getSongs():
    dirPath = path.dirname(path.realpath(__file__)) 
    songsDirectory = dirPath+'/songs/'
    songsPaths = [songsDirectory+f for f in listdir(songsDirectory) if isfile(join(songsDirectory, f))]
    return map(loadWavFile, songsPaths)

# def getNormalizedAudio(wave_file):
#     audio = np.frombuffer(wave_obj.audio_data, 'int16')
#     return (audio-np.min(wave_file))/(np.max(audio)-np.min(audio))
