import numpy as np

def GetBBoxes(filename):
    file_bbox = open(filename, "r")
    
    confidences = []
    bboxes = []
    for line in file_bbox:
        tokens = line.split(" ")
        tokens[-1] = tokens[-1][:-1]
        confidences.append(float(tokens[0]))
        bboxes.append([float(tokens[1]), float(tokens[2]), float(tokens[3]), float(tokens[4])])

    file_bbox.close()

    confidences = np.array(confidences)
    bboxes = np.array(bboxes)

    print(confidences.shape, bboxes.shape)

    return confidences, bboxes


if __name__ == "__main__":
    confidences, b_boxes = GetBBoxes('test/bboxes.txt')