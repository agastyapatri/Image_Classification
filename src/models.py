import numpy as np
import scipy as sp
import torch
import torch.nn as nn
torch.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"


class ResNet34(nn.Module):
    """
        ResNet, as defined in Kaiming He et al. 
    """
    def __init__(self, ) -> None:
        super().__init__()
    
    def forward(self, x):
        pass 


class VGG19(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()

    def forward(self, x):
        pass 



if __name__ == "__main__":
    pass