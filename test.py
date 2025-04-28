import torch

# Check if PyTorch detects the GPU and CuDNN
print(torch.cuda.is_available())
print(torch.backends.cudnn.enabled)

print(torch.cuda.is_available())  # Should return True if GPU is available
# print(torch.cuda.current_device())  # Returns the current GPU device ID
# print(torch.cuda.get_device_name(0))  # Prints the name of the GPU

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
