import csv
from math import sqrt
import numpy as np
import scipy.optimize as opt


def model_sqrt(x: float, a: float, b: float):
    return a*np.sqrt(b*x)


with open('k_to_freq.csv', 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]
    values: dict[str, list[float]] = {name: [] for name in rows[0]}
    for row in rows[1:]:
        for i, elem in enumerate(row):
            if elem == "":
                continue
            values[rows[0][i]] += [float(elem)]
    # print(values)

    avg_curve = []
    for i in range(len(values["k"])):
        avg_curve += [(values["EOSSPHlowvis"][i] +
                       values["SplitSPHlowvis"][i] +
                       values["EOSSPHhighvis"][i] +
                       values["SplitSPHhighvis"][i])/4]
    # for val in res:
    #     print(val)

    params, _ = opt.curve_fit(model_sqrt, values["k"], avg_curve)
    predicted = [np.sqrt(3) * model_sqrt(x, params[0], params[1])
                 for x in values["k"]]

    print("PRED--------")
    for val in predicted:
        print(val)
    print("--------")
