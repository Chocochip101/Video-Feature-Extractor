# Feature Object Extraction(2D/3D) to h5 Format
This repo aims at providing an easy to use and efficient code for extracting video features using deep CNN (2D or 3D) and convert to h5 Format.

## Requirments
- Pytorch >= 1.0
- Python >= 3
- ffmpeg-python
- h5py
- numpy  
   
~~~
!pip install -r requirements.txt
~~~

## How To Use ?
First of all you need to generate a csv containing the list of videos you want to process. For instance, if you have video1.mp4 and video2.webm to process, you will need to generate a csv of this form:  
~~~
video_path,feature_path
absolute_path_video1.mp4,absolute_path_of_video1_features.npy
absolute_path_video2.webm,absolute_path_of_video2_features.npy
~~~

You can see the example file at input.csv. 

And then just simply run:
~~~
python extract.py --csv=input.csv --type=2d --batch_size=64 --num_decoding_thread=4
~~~



## Directory

~~~
/result
/SampleVideo
/videocnn
~~~

## Acknowledgements
The code re-used code from [3D-ResNets](https://github.com/kenshohara/3D-ResNets-PyTorch) for 3D CNN and [Video Feature Extractor](https://github.com/antoine77340/video_feature_extractor) for object extraction.