import numpy as np
import scipy as sp
import torch
import torch.nn as nn
torch.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"
