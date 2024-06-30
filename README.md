# How to install CUDA & cuDNN.
Setting up CUDA & cuDNN for Machine Learning can be an overwhelming process. In this guide, I will walk you through the steps to install CUDA and cuDNN on your system, ensuring your machine is correctly set up for deep learning tasks. 

**System Configuration:**
- Operating System: Ubuntu 22.4
- GPU: GeForce RTX 3090
- ML Framework: Pytorch

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
We will install the NVIDIA driver tagged recommended - Which indicates which drivers are recommended for each piece of hardware based on compatibility and performance.

### Install Ubuntu drivers
```bash
sudo ubuntu-drivers autoinstall
```

### Install NVIDIA drivers
My recommended version is 555, change "XYZ" in the following command to your recommended driver.
```bash
sudo apt install nvidia-driver-XZY
```
Reboot the system for these changes to take effect.
```bash
reboot
```

### Check Installation
After reboot verify that the following command works:
```bash
nvidia-smi
```
