import torch


def solve(input: torch.Tensor, output: torch.Tensor, rows: int, cols: int):
    output.copy_(torch.transpose(input, 0, 1))
    return output
