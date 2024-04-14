# Detection-of-Distracted-Driver-using-CNN

This repository is the implementation codes for our project submission for COMP 6771 Image Processing Course at Concordia Uniservirty. The project title is "Detection of Distracted Driver using Convolutional Neural Network", aiming to replicate and expand upon the paper with the same title by B. Baheti, S. Gajre and S. Talbar on 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW).

The repo includes two notebooks, main_V1 and main_V2, implementing the model for the first and final submission:

- Both these files, have 2 Sections: "Data Preprocessing" and "Run Model"

In Data preprocesnig, we first load the downloaded data, do some proccesiing steps such as normalizing and perchannel mean subtraction. Then, we save them with pickle library so that don't have to procees them each time rnning the model. In this way, We read them from the cache after the first time processing the data. 

In Run Model, we define our hyperparameters based on original papar's setting. Then we define our modified VGG16 model, compile it and fit it on our costomized dataset- in main_V1 and main_v2 we fit our model to the two different versions of our datasetm respectively. Then, we evalate the model on the test sets, showing accuacy, plotting Training and Validation loss and accuracy of models, as well as as confusion matrixes.


The notebook "plot_result" plots both models performence together for better comparison and visualizatioin, showing Training and Validation loss and accuracy of both models together. Also it plots the confusion Matrix of both models for better evaluation. 


MATLAB Submission:

For utilizing matlab in our project, we used it for data augmentation, leveraging its extensive capabilities to enrich our dataset artificially. We first load our dataset and then implement Data augmentation techniques on them to enhance the size and variability the dataset: Rotation by 180 degrees, Horizontal flipping, Brightness adjustment, Addition of Gaussian noise, Image normalization, Gaussian blurring. Last, we save new datas as our more larger dataset for using in model_V2 model for training purpose.
