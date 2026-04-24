import numpy as np
import torch
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # torch.sigmoid(x)
    x = torch.tensor(x) * -1
    return 1/(1+ torch.exp(x));