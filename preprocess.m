% Define the directory containing the images
imageDir = './dataset';
files = dir(fullfile(imageDir, '*.jpg'));  % Adjust file type if necessary

% Define directories for saving processed images
outputDirs = {'Rotated', 'Flipped', 'BrightnessAdjusted', 'Noisy', 'Normalized', 'GaussianBlurred'};
for i = 1:length(outputDirs)
    if ~exist(fullfile(imageDir, outputDirs{i}), 'dir')
        mkdir(fullfile(imageDir, outputDirs{i}));
    end
end

% Process each image in the directory
for idx = 1:length(files)
    % Read each image
    img = imread(fullfile(imageDir, files(idx).name));

    % 1. Rotate the image by 30 degrees
    rotated_img = imrotate(img, 30);

    % 4. Flip the image horizontally
    flipped_img = flip(img, 2);

    % 7. Adjust brightness by scaling intensities
    brightnessAdjusted_img = imadjust(img, [], [], 1.2);

    % 8. Add Gaussian noise
    noisy_img = imnoise(img, 'gaussian');

    % 9. Normalize the image
    normalized_img = double(img) / 255;

    % 14. Apply Gaussian blur
    GaussianBlur_img = imgaussfilt(img, 2);

    % Save the processed images to their respective folders
    imwrite(rotated_img, fullfile(imageDir, outputDirs{1}, files(idx).name));
    imwrite(flipped_img, fullfile(imageDir, outputDirs{2}, files(idx).name));
    imwrite(brightnessAdjusted_img, fullfile(imageDir, outputDirs{3}, files(idx).name));
    imwrite(noisy_img, fullfile(imageDir, outputDirs{4}, files(idx).name));
    imwrite(normalized_img, fullfile(imageDir, outputDirs{5}, files(idx).name));
    imwrite(GaussianBlur_img, fullfile(imageDir, outputDirs{6}, files(idx).name));
end

disp('Processing complete.');