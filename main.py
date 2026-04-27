# Numerical Python and Matplotlib
from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

# store data globally
days = []
absences = []


def sample_numpy(event):

    # get values from HTML (FIXED ID)
    day = document.getElementById("dayofweek").value
    absence = document.getElementById("absences").value

    # validate input
    if absence == "":
        return

    absence = int(absence)

    # store data
    days.append(day)
    absences.append(absence)

    # NUMPY ARRAYS
    x = np.array(days)          # categorical data
    y = np.array(absences)     # numeric data

    # convert x into index positions for graphing
    x_index = np.arange(len(days))

    # create graph
    fig = plt.figure(5.5)
    plt.plot(x_index, y, marker='o', color='blue')

    # replace numbers with day labels
    plt.xticks(x_index, x)

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    plt.grid(True)

    # clear previous output
    document.getElementById("output").innerHTML = ""

    # DISPLAY FIGURE
    display(fig, target="output")
