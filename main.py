from pyscript import display, document
import matplotlib.pyplot as plt

# store absences per day
attendance_data = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0
}

def sample_numpy(event):
    # get values from HTML
    day = document.getElementById("day").value
    absences = document.getElementById("absences").value

    # convert to number
    if absences == "":
        return
    absences = int(absences)

    # store/update data
    attendance_data[day] = absences

    # clear previous graph
    document.getElementById('output').innerHTML = ""

    # prepare data for plotting
    days = list(attendance_data.keys())
    values = list(attendance_data.values())

    # create graph
    plt.figure()
    plt.plot(days, values, marker='o')

    plt.title("Student Absences Per Day")
    plt.xlabel("Days")
    plt.ylabel("Number of Absences")

    # display graph in HTML
    display(plt, target="output")
