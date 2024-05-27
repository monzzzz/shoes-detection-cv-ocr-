# Welcome to Shoes Detection Project (Thai / Non-Latin Language) 

## Objective

detect the color of the shoes and text below it from the image with an accuracy of 99 percent by applying object detection and optical character recognition

## Optical Character Recognition

### Main Procedures
- synthesizing the image by utilizing synthtiger (https://github.com/clovaai/synthtiger)
- train it with deep text recognition benchmark (https://github.com/clovaai/deep-text-recognition-benchmark?tab=readme-ov-file)

### Synthesizing

- follow the instructions in synthtiger GitHub page including installing fonts and corpus for your preferred language (don't forget the extract the font)
- setup and activate conda env by installing the necessary library (Pillow and raqm)
- to install raqm, you need to follow the pillow document (https://pillow.readthedocs.io/en/stable/installation/basic-installation.html), and then check the of raqm availbility by running `python3 -m PIL` or `check.py` file
- clone the fork GitHub repository of synthtiger (https://github.com/eikaramba/synthtiger/tree/pillow10), and make sure to clone it from branch pillow 10. Subsequently, use this command `export PYTHONPATH=/path/to/your/forked/synthtiger:$PYTHONPATH
` to set it as your default Synthtiger Library in the env.
- lastly, ensure that all the files are in the correct path, and then run command `synthtiger -o results -w 4 -v examples/synthtiger/template.py SynthTiger config.yaml`

### Training

- generating two types of data both ST and MJ.

#### MJ
- download preferred fonts and datasets in form of txt file
- MJ is generated by running `easy_ocr_text_train/main.py`

#### ST
- this is acquired from synthesizing method

to be continue

## Object Detection

to be continued

## Support
If you have any question, feel free to reach out in discussion section.
