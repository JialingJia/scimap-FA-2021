import warnings
import numpy as np
from pathlib import Path
import math
from math import cos, sin
import json
from random import sample
from extractTree import *
from drawTree import *

# calcualte the average curvature
def curve(ex):
    x_t = np.gradient(ex[:, 0])
    y_t = np.gradient(ex[:, 1])

    xx_t = np.gradient(x_t)
    yy_t = np.gradient(y_t)

    curvature_val = (xx_t * y_t - x_t * yy_t) / (x_t * x_t + y_t * y_t)**1.5
    return(np.std(curvature_val))

#find visual difference


def visual_diff(tree):

    position = []
    last = [np.array((0, 0))]  # find the last branches positions
    for s, e, c in unfurl(tree):
        position.append(s)
        position.append(e)
        last.append(e)

    # print('last: ', last)

    #calculate the average degree of the tree
    res = [(sum(i) / len(last)) for i in zip(*last)]
    # print('res: ', res)
    ave_degree = math.degrees(math.atan(res[1]/res[0]))
    # print("average degree of the tree: ", ave_degree)

    #calculate the width
    maxi_x = max([i[0] for i in last])
    mini_x = min([i[0] for i in last])
    width = abs(maxi_x - mini_x)
    # print("width of the tree: ", width)

    # calculate the height
    maxi_y = max([i[1] for i in last])
    height = maxi_y
    # print('height of the tree: ', height)

    # find the curvature for all lines in the tree
    all_line = []
    line = [(0, 0)]
    temp = (0, 0)
    for a in [tuple(list(i)) for i in position]:
        if temp != a:
            temp = a
            if a not in line:
                line.append(a)
            else:
                all_line.append(line)
                line = line[0:(line.index(a) + 1)]

    if not all_line:  # avoid if there is only one line
        all_line.append(line)

    # print("all_line: ", all_line)
    curve_list = []
    for i in all_line:
        curve_list.append(curve(np.array(i)))

    # print('curve_list: ', curve_list)
    average_curve = np.average(curve_list)  # find the average curvature
    max_curve = np.max(curve_list)  # find the max curvature
    # print("average curvature: ", average_curve)

    return(({"ave_degree": ave_degree, "width": width, "height": height,
            "average_curve": average_curve, "max_curve": max_curve, "name": tree["name"]}))


def compute_visual_metrics(field):

    # find mentors in the fields
    mentor_list = getAllResearchersWithoutMentors(field)

    # create root tree data in the field
    root_tree = []
    for i in mentor_list:
        gc = getDict(i, 0, 10)
        # postorder(gc)
        if "children" in gc:
            root_tree.append(gc)

    tree_metrics = []
    for i in root_tree:
        tree_metrics.append(visual_diff(i))
        # print(visual_diff(i))

    return tree_metrics
