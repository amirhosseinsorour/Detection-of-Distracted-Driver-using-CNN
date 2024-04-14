
## Detection of Distracted Drivers using CNN

### Overview
This repository hosts the codebase for the "Detection of Distracted Driver using Convolutional Neural Networks (CNN)," a project crafted for the COMP 6771 Image Processing Course at Concordia University. Inspired by the pivotal work presented by B. Baheti, S. Gajre, and S. Talbar at the 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), our aim was to not only replicate but also build upon the concepts detailed in their paper.

### Repository Structure
The code repository is organized into several key components:

- **main_V1.ipynb**: Initial model implementation for the project's first phase.
- **main_V2.ipynb**: Refined model for the final project submission.

Both notebooks are structured into two main sections: *Data Preprocessing* and *Model Execution*.

#### Data Preprocessing
This phase entails:
- Loading the dataset obtained for the project.
- Applying preprocessing steps like normalization and mean subtraction per channel.
- Utilizing the `pickle` library to cache processed data, thereby avoiding redundant processing on subsequent model executions.

#### Model Execution
Here, we:
- Establish hyperparameters in line with the original paper's configurations.
- Modify and employ the VGG16 architecture to suit our custom dataset.
- Compile and fit our model to two distinct dataset versions in `main_V1` and `main_V2`.
- Evaluate the model's performance on test sets, providing insights through accuracy metrics, loss and accuracy plots during training and validation phases, and confusion matrices.

- **plot_result.ipynb**: Compares performances by plotting training/validation losses and accuracies alongside confusion matrices for both model versions.

### MATLAB Integration
Our project leverages MATLAB's sophisticated data processing tools to augment our dataset, enhancing its size and variability. The script `preprocess.m` encapsulates this process, performing several augmentation techniques to enrich the dataset:

- Rotating images by 180 degrees.
- Applying horizontal flips to images.
- Adjusting image brightness.
- Injecting Gaussian noise.
- Normalizing images.
- Applying Gaussian blurring.

The result is a diversified dataset, which we subsequently utilize for training the `model_V2` notebook, thus ensuring our model benefits from a more extensive and varied set of training examples.

---

