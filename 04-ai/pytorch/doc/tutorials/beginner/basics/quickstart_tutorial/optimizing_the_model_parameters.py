import torch
from torch import nn

# loss function
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model)