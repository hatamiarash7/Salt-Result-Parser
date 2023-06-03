"""This script will parse the Salt output and visualize the job durations"""

import re
import sys
import matplotlib.pyplot as plt
import mplcursors

# Initialize lists to store job titles and durations
job_titles = []
durations = []


def parse():
    """Parse the output file and extract job titles and durations"""

    # Path to the file containing the output
    file_path = sys.argv[1]

    # Read the output file
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        output = file.read()

    # Extract job titles and durations using regex
    matches = re.findall(r'----------\n\s+ID: (.+)', output)
    for match in matches:
        job_titles.append(match.strip())

    matches = re.findall(r'Duration: (.+) ms', output)
    for match in matches:
        durations.append(float(match.strip()))


def draw():
    """Draw a horizontal bar chart using matplotlib"""

    # Create a chart using matplotlib
    _, axis = plt.subplots()

    # Plot the horizontal bar chart
    bars = axis.barh(job_titles, durations)

    # Connect the tooltips to the chart
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", update_tooltip)

    # Draw the plot
    axis.set_xlabel('Duration (ms)')
    axis.set_ylabel('Job Title')
    axis.set_title('Job Durations')
    plt.tight_layout()
    plt.show()


def update_tooltip(self):
    """Generate tooltip text for each bar"""

    # Create the tooltip format string
    tooltip_format = '%s: %.3f ms'

    index = self.target.index
    title = job_titles[index]
    duration = durations[index]
    self.annotation.set_text(tooltip_format % (title, duration))


if __name__ == '__main__':
    parse()
    draw()
