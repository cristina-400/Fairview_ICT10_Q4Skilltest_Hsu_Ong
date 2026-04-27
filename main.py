from pyscript import display, document
import matplotlib.pyplot as plt

# store data globally
days = []
absences = []

def sample_numpy(event):
    # get values from HTML
    day = document.getElementById("day").value
    absence = document.getElementById("absences").value

    # validate input
    if absence == "":
        return

    absence = int(absence)

    # store data
    days.append(day)
    absences.append(absence)

    # clear previous graph
    document.getElementById('output').innerHTML = ""

    # create graph
    plt.figure()
    plt.plot(days, absences, marker='o')

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    # show graph in HTML
    display(plt, target="output")
