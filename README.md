# Shama-Bird-Call-Analysis-and-Classification
![Shama](https://www.nestoftern.com/tern/tern/img/home_page/shama_logo.png)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Overview](#overview)
* [About the Project](#about-the-project)
* [Data](#data)
* [Data Preprocessing](#data-preprocessing)
* [Training](#training)
* [Results](#results)
* [Technology Stack](#technology-stack)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


## Overview
There are roughly around 9,000-10,000 bird species in the world. When out birding a birder is more likely to hear a bird than see it. This leads to difficulty while identifying bird species without being able to see it. However, by using a bird's call or song we can identify the species. If the sound can be used to classify a bird species, researchers and amateur birders alike can have a better idea of which bird specie it is. Automated bird call classification will allow the beginners to easily identify the bird species. Moreover, these automated recordings can be stored and used to compare with bird calls in the future.



<!-- ABOUT THE PROJECT -->
## About The Project
The aim of this project is to build a sound-based bird species classification system by implementing Audio and Image processing using Convolutional Neural Networks.

We searched for 4 classes of Indian birds-
1. Aegithinatiphia
2. Cyornistickelliae
3. Eudynamysscolopaceus
4. Psilopogonhaemacephalus

After gathering the bird calls of the above four bird species. We used [Librosa]((https://librosa.github.io/librosa/index.html)) to transform the sound into Mel-frequency spectrograms. Mel scale is known as an audio scale of sound pitches that seem to be in equal distance from each other for listeners. The idea behind that is connected with the way how humans hear. When we connect those two ideas we get a modified spectrogram (mel-frequency cepstrum) that simply ignores the sounds humans do not hear and plot the most important parts. We processed Mel-frequency spectrograms with Convolutional Neural Networks to classify bird song or call.

## Data 
The data was gathered from the [xeno-canto](http://www.xeno-canto.org/) website which is a website dedicated to sharing bird sounds from all over the world. Data can be downloaded using [this file](https://github.com/nestoftern/Shama-Bird-Call-Analysis-and-Classification/blob/master/bird_call_download.py).

## Data preprocessing
The data should be prepared. Each song is cut into 5 second recordings and preprocessed into Mel spectrograms. The purpose is to normalize the dataset to have the same size along with the whole dataset in one run, and to denoise recordings. Moreover, the data is filtered with a high-pass filter. Data can be preprocessed using [this file](https://github.com/nestoftern/Shama-Bird-Call-Analysis-and-Classification/blob/master/data_preparation.py).

## Training 
We approached the problem of song classification with Convolutional Neural Networks. Model can be trained using [this file](https://github.com/nestoftern/Shama-Bird-Call-Analysis-and-Classification/blob/master/neural_network.py).

## Results
In progress...

## Technology Stack
* [Python](https://www.python.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Keras](https://keras.io/)
* [TensorFlow](https://www.tensorflow.org/)
* [scikit-learn](https://scikit-learn.org/stable/)



<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create!

Steps to contribute-
1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

Any contributions you make, will be **greatly appreciated**.



<!-- LICENSE -->
## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

Organization- T.E.R.N.(Technology, Engineering and Research for Nature)  
Email- tern.nagpur@gmail.com



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Xeno-Canto](https://www.xeno-canto.org/)
* [Bird Species Identification using Convolutional Neural Networks](http://publications.lib.chalmers.se/records/fulltext/249467/249467.pdf)
* [Deep learning for detection of bird vocalisations](https://arxiv.org/ftp/arxiv/papers/1609/1609.08408.pdf)
* [Audio Based Bird Species Identification using Deep Learning Techniques](http://ceur-ws.org/Vol-1609/16090547.pdf)
