import torch


# Check PyTorch version
print(f"PyTorch version: {torch.__version__}")
# Check if CUDA device is recognised
print(f"CUDA device is available: {torch.cuda.is_available()}")
assert torch.cuda.is_available(), ValueError("CUDA device is not recognised.")

device = "cuda"
a = torch.rand(3, 1).to(device)
b = torch.rand(1, 3).to(device)

c = a @ b

print(f"Variable shape: {c.shape}")
print(f"Variable devie: {c.device}")
