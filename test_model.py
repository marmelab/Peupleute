from birdnet.analyze import identify 
import os

DEBUG=False

def isBirdIdentified (birdname, identifications):
    for identification in identifications:
        if areNamesEquals(birdname, identification['vernacularName'], identification['scientificName'], ):
            return True
    return False


VERNACULAR_TO_SCIENTIFIC = {
    'EuropeanGreenWoodpecker': 'Picus viridis',
    'CommonStarling': 'Sturnus vulgaris',
    'EuropeanCrestedTit': 'Lophophanes cristatus',
    'CommonBlackbird': 'Turdus merula',
    'EurasianCollaredDove': 'Streptopelia decaocto',
    'CommonWoodPigeon': 'Columba palumbus',
}

def areNamesEquals (recordedName, identifiedName, scientificBirdName):
    return recordedName.replace(' ', '') == identifiedName.replace(' ', '') or VERNACULAR_TO_SCIENTIFIC.get(recordedName) == scientificBirdName

DATASET_DIR='./dataset/audio'

nbTotalOfMatchs = 0
nbTotalOfSongs = 0
for dirPath, _, filenames in os.walk(DATASET_DIR):
    nbOfSongs = len(filenames)
    nbTotalOfSongs += nbOfSongs
    nbOfMatchs = 0
    birdname = dirPath.rsplit('/').pop()
    for filename in filenames:
        filepath = os.path.join(dirPath, filename)
        identifications = identify(filepath)
        if isBirdIdentified(birdname, identifications):
            nbOfMatchs+=1
            nbTotalOfMatchs+=1
        elif DEBUG:
            print('\n', filepath, 'not correctly identified', identifications)
    print('\n\n\n', 'Result for', birdname, '=', nbOfMatchs, '/', nbOfSongs)

print('\n', 'Total =', nbTotalOfMatchs, '/', nbTotalOfSongs)
