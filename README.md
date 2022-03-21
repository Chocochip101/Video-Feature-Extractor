# Extracting Video Object Features to h5 format
This repo aims at providing to use and efficient code for extracting video object features using deep CNN (ResNet 2D or 3D) and converting to h5 Format.  
![Architecture](/Architecture.png)  
1. Split video to image by 1 FPS
2. Extract object feature by CNN and save to separate .npy file
3. Merge files to .h5 format

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
### Dataset
First of all you need to generate a csv containing the list of videos you want to process. For instance, if you have video1.mp4 and video2.webm to process, you will need to generate a csv of this form:  
~~~
video_path,feature_path
absolute_path_video1.mp4,absolute_path_of_video1_features.npy
absolute_path_video2.webm,absolute_path_of_video2_features.npy
~~~

You can see the example file at input.csv. 
### Numpy Extraction

Just simply run:
~~~ 
!python extract.py --csv=input.csv --type=2d --batch_size=64 --num_decoding_thread=4
~~~
Then at the result directory you can see the .npy file extracted from the video by ResNet.
### h5 Convertion
If you want the feature extraction file as a format of h5, run convert.py.
~~~
!python convert.py --numpy_dir=/NumpyResult --output_dir=/h5Result --ouput_filename=SampleVideo
~~~
As running the above code, you can see the converted SampleVideo.h5 file at h5Result directory.

### Check data
You can briefly check the h5 data file by this code.
~~~ python
import h5py
# h5 file dir
a = h5py.File("./h5Result/SampleVideo.h5", "r")
with a:
  # Check the keys
  print(a.keys())
  a_group_key = list(a.keys())[0]

  # Get the data
  data = list(a[a_group_key])
  print(data)
~~~

## Directory

~~~
/h5Result
/NumpyResult
/SampleVideo
/videocnn
extract.py
convert.py
model.py
preprocessing.py
video_loader.py
~~~

## Acknowledgements
The code re-used code from [3D-ResNets](https://github.com/kenshohara/3D-ResNets-PyTorch) for 3D CNN and [Video Feature Extractor](https://github.com/antoine77340/video_feature_extractor) for object extraction.