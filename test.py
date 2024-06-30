import torch


# Check PyTorch version
print(f"PyTorch version: {torch.__version__}")
# Check if CUDA device is recognised
print(f"CUDA device is available: {torch.cuda.is_available()}")
assert torch.cuda.is_available(), ValueError("CUDA device is not recognised.")
