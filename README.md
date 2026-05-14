# How to install CUDA & cuDNN

Setting up CUDA & cuDNN for Machine Learning can be overwhelming. In this guide, I will walk you through the steps to install CUDA and cuDNN on your system, ensuring your machine is correctly set up for deep learning tasks. 

**System Configuration:**
- **Operating System:** Ubuntu 22.04
- **GPU:** GeForce RTX 3090
- **ML Framework:** PyTorch

## Install NVIDIA drivers
### Update & Upgrade
```bash
sudo apt update && sudo apt upgrade
```

### Remove previous NVIDIA installation
Uninstall the previous NVIDIA and CUDA installation to avoid messing up the new installation.
```bash
sudo apt-get remove --purge -y '*nvidia*' '*cuda*' 'libcudnn*' 'libnccl*' '*cudnn*' '*nccl*'
```

```bash
sudo apt-get autoremove --purge -y
```

```bash
sudo apt-get clean
```

Check if there are any remaining packages or files.

```bash
dpkg -l | grep -E 'nvidia|cuda|cudnn|nccl'
```

### Detecting and Managing Drivers on Ubuntu
```bash
ubuntu-drivers devices
```
We will install the NVIDIA driver tagged recommended, which indicates which drivers are recommended for each piece of hardware based on compatibility and performance.

### Install Ubuntu drivers
```bash
sudo ubuntu-drivers autoinstall
```

### Install NVIDIA drivers
My recommended version is `nvidia-driver-595-open`. If `ubuntu-drivers devices` recommends a different driver on your machine, replace `nvidia-driver-595-open` with that package name.
```bash
sudo apt install nvidia-driver-595-open
```
Reboot the system for these changes to take effect.
```bash
reboot
```

### Check Installation
After reboot, verify that the following command works:
```bash
nvidia-smi
```

## Install CUDA drivers

### Update & Upgrade
Again, check for updates on your OS.
```bash
sudo apt update && sudo apt upgrade
```

### Install CUDA Toolkit
At the time of writing, the latest CUDA version supported by [PyTorch](https://pytorch.org/get-started/locally/#start-locally) is 13.2.

You can find older versions in the [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive). In my case, I will be continuing with [CUDA Toolkit 13.2.0](https://developer.nvidia.com/cuda-13-2-0-download-archive) (March 2026).

You will need to select your operating system (Linux in my case). Afterwards, you will be prompted to select the Architecture. If you are not sure what the Architecture of your PC you can use the command below (in my case, the Architecture is x86_64).
```bash
uname -m
```
Next, we need to select the distribution and version of our operating system, in my case, Ubuntu 22.04. Lastly, I am using the deb (local) installer type.

These are the commands for installing CUDA Toolkit 13.2:
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
```
```bash
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
```
```bash
wget https://developer.download.nvidia.com/compute/cuda/13.2.0/local_installers/cuda-repo-ubuntu2204-13-2-local_13.2.0-595.45.04-1_amd64.deb
```
```bash
sudo dpkg -i cuda-repo-ubuntu2204-13-2-local_13.2.0-595.45.04-1_amd64.deb
```
```bash
sudo cp /var/cuda-repo-ubuntu2204-13-2-local/cuda-*-keyring.gpg /usr/share/keyrings/
```
```bash
sudo apt-get update
```
```bash
sudo apt-get -y install cuda-toolkit-13-2
```

### Check CUDA install
```bash
nvcc --version
```
---
If you are not getting the CUDA version as output, do the following:
- Ensure that CUDA 13.2 is installed in the correct directory, typically `/usr/local/cuda-13.2`.
- Create a symlink to the CUDA directory to make it easier to reference.
  ```bash
  sudo ln -s /usr/local/cuda-13.2 /usr/local/cuda
  ```
- Add the CUDA paths to your `.bashrc` file to ensure they are set up every time you open a terminal.
  ```bash
  echo 'export PATH=/usr/local/cuda-13.2/bin:$PATH' >> ~/.bashrc
  ```
- Apply the changes made to the `.bashrc`
  ```bash
  source ~/.bashrc
  ```

## Install cuDNN

### Download the cuDNN .deb file
Firstly, to match appropriate cuDNN with our CUDA and Driver versions, we can use the [table provided by NVIDIA](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html#id17). In my case, the newest 9.22.0 cuDNN version is appropriate.

You can download the cuDNN file [here](https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local), for which you will need an Nvidia account. Same as for CUDA, you will have to select OS, architecture, distribution, version, and installer type.

In my case, to download the installer for Linux Ubuntu 22.04 x86_64, the instructions are as follows:
```bash
wget https://developer.download.nvidia.com/compute/cudnn/9.22.0/local_installers/cudnn-local-repo-ubuntu2204-9.22.0_1.0-1_amd64.deb
```
```bash
sudo dpkg -i cudnn-local-repo-ubuntu2204-9.22.0_1.0-1_amd64.deb
```
```bash
sudo cp /var/cudnn-local-repo-ubuntu2204-9.22.0/cudnn-*-keyring.gpg /usr/share/keyrings/
```
```bash
sudo apt-get update
```
```bash
sudo apt-get -y install cudnn9-cuda-13
```

## Test CUDA with PyTorch
I assume that you already have Python installed on your machine, so this tutorial will not cover that part.

⚠️ **NOTE:** The latest PyTorch requires Python 3.10 or later.

### Create a Directory
```bash
mkdir test_cuda
```
```bash
cd test_cuda
```
### Create and Activate a Virtual Environment
```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```

### Install PyTorch
```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132
```

### Execute Python test script
```Python
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
print(f"Variable device: {c.device}")
```

## Conclusion
If you carefully followed these instructions, you have successfully installed CUDA and cuDNN on your Ubuntu 22.04 system. Your NVIDIA GPU is now ready for deep learning tasks with PyTorch.

You can also view this guide on [Medium](https://medium.com/@milistu/how-to-install-cuda-cudnn-7e4a00ae4f44). If this guide helped you, give it a 👏, share it, and give it a ⭐️ on GitHub.
