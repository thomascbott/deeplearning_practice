import torch

def main():
    # creating a tensor with 10 float values
    x = torch.arange(10, dtype=torch.float32)
    print(x)

    # numel() method gives number of elements in a tensor
    num_elements = x.numel()
    print(f"Number of elements in tensor: {num_elements}")

    # the shape attribute returns object of type torch.Size that lists lengths of each dimension of a tensor
    y = x.reshape((5, 2))
    print(y)
    print(y.shape)

    # Can build tensors with elements inited to 0 using zeros() method
    z = torch.zeros(3, 3)
    print(z)


if __name__ == '__main__':
    main()