import os
import json
import warnings
warnings.filterwarnings('ignore')
import sys
from tqdm import tqdm_notebook as tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import librosa
from mutagen.mp3 import MP3
import noisereduce as no
import wave
import pandas as pd



birds=[] # list of all birds  
for root, dirs, files in os.walk("../TERN/Bird Call Analysis/data/xeno-canto-dataset/"):
    if root == "../TERN/Bird Call Analysis/data/xeno-canto-dataset/":
        birds=dirs
        
birds50=[]              
flist=[] # list of all files
blist=[] # list of files for one bird 
i50=0;
for i, bird in enumerate(birds):
    for root, dirs, files in os.walk("../TERN/Bird Call Analysis/data/xeno-canto-dataset/"+bird):
        for file in files:
            if file.endswith(".mp3"):
                blist.append(os.path.join(root, file))
    if len(blist) > 50:
        i50 = i50+1;
        birds50.append(bird)
        flist.append(blist)



def saveMel2(y, directory,bird,i):
    N_FFT = 1024         # Number of frequency bins for Fast Fourier Transform
    HOP_SIZE = 1024      # Number of audio frames between STFT columns
    SR = 44100           # Sampling frequency
    N_MELS = 30          # Mel band parameters   
    WIN_SIZE = 1024      # number of samples in each STFT window
    WINDOW_TYPE = 'hann' # the windowin function
    FEATURE = 'mel'      # feature representation
    
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)

    plt.rcParams['figure.figsize'] = (10,2)            
    fig = plt.figure(1,frameon=False)
    fig.set_size_inches(4,4)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    spectogram = librosa.display.specshow(
             librosa.core.amplitude_to_db(
                librosa.feature.melspectrogram(
                                y=y, 
                                sr=SR)))
    
    path = directory + str(i)
    print(path)
    fig.savefig(path)
    fig.clear()
    ax.cla()
    plt.clf()
    plt.close('all')



size = {'desired': 10, # [seconds]
        'minimum': 5, # [seconds]
        'stride' : 0, # [seconds]
        'name': 5, #[number of letters]  
        } # stride should not be bigger than desired length

step=1
if step>0:
    for bird, birdList in enumerate(flist):
        i = 1
        for birdnr, path in tqdm(enumerate(birdList)):
            directory="../TERN/Bird Call Analysis/data/xeno-canto-dataset/"+str(bird)+birds50[bird][:size['name']]+"/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            y, sr = librosa.load(path,mono=True)
            y = no.reduce_noise(audio_clip=y, noise_clip=y, verbose=False)  
            step = (size['desired']-size['stride'])*sr 
            nr=0;
            for start, end in zip(range(0,len(y),step),range(size['desired']*sr,len(y),step)):
                nr=nr+1
                if end-start > size['minimum']*sr:
                    melpath= "../TERN/Bird Call Analysis/data/mel_freq_class/"
                    saveMel2(y[start:end],melpath,bird,i)
                    i+=1
        pass
else:    
    print("Error: Stride should be lower than desired length.")
