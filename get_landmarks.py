import numpy as np

def GetLandmarks(filename):
    file_2d = open(filename, "r")
    for line in file_2d:
        break
    
    x_2d = []
    y_2d = []
    for line in file_2d:
        tokens = line.split(", ")
        tokens[-1] = tokens[-1][:-1]
        x_2d.append(tokens[5: 5 + 68])
        y_2d.append(tokens[5 + 68: 5 + 68 + 68])

    file_2d.close()

    x_2d = np.array(x_2d).astype(np.float32)
    y_2d = np.array(y_2d).astype(np.float32)

    print(x_2d.shape, x_2d.dtype)

    return x_2d, y_2d


if __name__ == "__main__":
    X, Y = GetLandmarks('test/demo9.csv')