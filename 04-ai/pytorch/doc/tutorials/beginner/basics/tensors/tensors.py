import torch
import numpy as np

# inintializing a tensor
# directly form data
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)


# from a numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# from another tensor
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n{x_ones}\n")
x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n{x_rand}\n")

# with random or constant values
shape = (2, 3,)
rand_tensor = torch.rand(shape)
one_tensor = torch.ones(shape)
zero_tensor = torch.zeros(shape)

print(f"Random Tensor: \n{rand_tensor}\n")
print(f"Ones Tensor: \n{one_tensor}\n")
print(f"Zeros Tensor: \n{zero_tensor}\n")

# Attributes of a Tensor 张量的属性
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")


# Operations on Tensors 张量的操作
# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to('cuda')

# Standard numpy-like indexing and slicing 标准的类似numpy的索引和切片
tensor = torch.ones(4, 4)
print(f"Frist row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:, 1] = 0
print(tensor)

# Joining tensors 连接张量
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)


# Arithmetic operations 算术运算



