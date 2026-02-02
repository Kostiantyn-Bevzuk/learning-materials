import torch
import torch.nn
from torchtyping import TensorType

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        out_shape = to_reshape.shape
        return torch.reshape(to_reshape, (out_shape[0] * out_shape[1] // 2, 2))

    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        return torch.mean(to_avg, dim=0) # dim = 0 - by columns dim = 1 - by rows

    def concatenate(self, cat_one: TensorType[float], cat_two: TensorType[float]) -> TensorType[float]:
        return torch.cat(cat_one, cat_two, dim=0)

    def get_loss(self, prediction: TensorType[float], target: TensorType[float]) -> TensorType[float]:
        return torch.nn.functional.mse_loss(prediction, target)