import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the uploaded CSV file
data = pd.read_csv('../Dataset/cache/try_hist.csv')
new_data = pd.read_csv('../Dataset/v2_cam1_cam2/cache/try_hist.csv')
num_epochs = 180

# Set up the figure and axis for two plots with updated colors for better differentiation
fig, axs = plt.subplots(2, 1, figsize=(12, 14))

# Define colors for better visibility and differentiation
colors = {'V1 Train': '#1f77b4', 'V1 Val': '#ff7f0e', 'V2 Train': '#2ca02c', 'V2 Val': '#d62728'}

# Plot training and validation loss for both models with updated labels and colors
axs[0].plot(data['loss'], label='Training Loss of Model trained on V1 Dataset', linestyle='--', color=colors['V1 Train'])
axs[0].plot(data['val_loss'], label='Validation Loss of Model trained on V1 Dataset', linestyle='--', color=colors['V1 Val'])
axs[0].plot(new_data['loss'].iloc[:num_epochs], label='Training Loss of Model trained on V2 Dataset', color=colors['V2 Train'])
axs[0].plot(new_data['val_loss'].iloc[:num_epochs], label='Validation Loss of Model trained on V2 Dataset', color=colors['V2 Val'])
axs[0].set_title('Model Loss Comparison')
axs[0].set_xlabel('Epochs')
axs[0].set_ylabel('Loss')
axs[0].legend()

# Plot training and validation accuracy for both models with updated labels and colors
axs[1].plot(data['accuracy'], label='Training Accuracy of Model trained on V1 Dataset', linestyle='--', color=colors['V1 Train'])
axs[1].plot(data['val_accuracy'], label='Validation Accuracy of Model trained on V1 Dataset', linestyle='--', color=colors['V1 Val'])
axs[1].plot(new_data['accuracy'].iloc[:num_epochs], label='Training Accuracy of Model trained on V2 Dataset', color=colors['V2 Train'])
axs[1].plot(new_data['val_accuracy'].iloc[:num_epochs], label='Validation Accuracy of Model trained on V2 Dataset', color=colors['V2 Val'])
axs[1].set_title('Model Accuracy Comparison')
axs[1].set_xlabel('Epochs')
axs[1].set_ylabel('Accuracy')
axs[1].legend()

# Show plots
plt.tight_layout()
plt.show()
