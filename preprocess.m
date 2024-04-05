% Read the image
originalImage = imread('your_image.jpg');

% Convert to grayscale
grayImage = rgb2gray(originalImage);

% Apply Gaussian filter for noise reduction
% smoothedImage = imgaussfilt(grayImage, 2); % '2' is the standard deviation of the Gaussian kernel

% Display the original and processed images
subplot(1, 2, 1);
imshow(originalImage);
title('Original Image');

subplot(1, 2, 2);
imshow(grayImage);
title('Processed Image');
