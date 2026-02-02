import torch
import torch.nn as nn
from torchtyping import TensorType
from collections import Counter


# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: list[str], negative: list[str]) -> TensorType[float]:
        tokens = [word for sentence in positive + negative for word in sentence.lower().split()]
        tokens.sort()
        counter = Counter(tokens)
        vocab = {word: i+1 for i, word in enumerate(counter)}
        encoded_positive = [torch.Tensor([vocab[word] for word in sentence.lower().split()]) for sentence in positive]
        encoded_negative = [torch.Tensor([vocab[word] for word in sentence.lower().split()]) for sentence in negative]
        out = torch.nn.utils.rnn.pad_sequence(encoded_positive + encoded_negative, batch_first=True)
        return out

        
positive=["Good case, Excellent value.","Great for the jawbone.","The mic is great.","If you are Razr owner...you must have this!","Highly recommend for any one who has a blue tooth phone"]
negative=["So there is no way for me to plug it in here in the US unless I go buy a converter.","Tied to charger for conversations lasting more than 45 minutes.MAJOR PROBLEMS!!","I have to jiggle the plug to get it to line up right to get decent volume.","Needless to say, I wasted my money.","What a waste of money and time!"]



Solution().get_dataset(positive=positive, negative=negative)