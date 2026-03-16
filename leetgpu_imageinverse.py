import torch

def solve(image: torch.Tensor, width: int, height: int):
    image[0::4] = 255 - image[0::4]
    image[1::4] = 255 - image[1::4]
    image[2::4] = 255 - image[2::4]
    return image
