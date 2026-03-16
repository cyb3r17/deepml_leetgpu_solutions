import torch.nn.functional as F

def solve(input, kernel, output, input_size, kernel_size):
   
    x = input.unsqueeze(0).unsqueeze(0)   # (1, 1, input_size)
    k = kernel.unsqueeze(0).unsqueeze(0)  # (1, 1, kernel_size)
    
    result = F.conv1d(x, k)
    output.copy_(result.squeeze())
    return output
