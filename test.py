import textgrid
import torch
import torch.nn as nn
import math

if __name__ == '__main__':
    loss_fn = nn.CrossEntropyLoss()
    a = torch.tensor([[0.4, 0.3, 0.3],[0.9, 0.1, 0]])
    tmp = nn.Softmax()(a)
    tmp = torch.log(tmp)
    b = torch.tensor([1, 2])
    loss = loss_fn(a, b)
    print(loss)