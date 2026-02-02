from torch.nn.utils.rnn import pad_sequence
import torch 
a = torch.ones(25, 300)
b = torch.ones(22, 300)
c = torch.ones(15, 300)
print(pad_sequence([a, b, c], batch_first=True).size())

from torch.nn.utils.rnn import pad_sequence
import torch

a = torch.tensor([1, 2, 3])       # length 3
b = torch.tensor([4, 5])          # length 2
c = torch.tensor([6])             # length 1

padded = pad_sequence([a, b, c], batch_first=False)
print(padded)
print(padded.size())