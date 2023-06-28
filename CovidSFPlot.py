import matplotlib.pyplot as plt

# Function to plot the San Francisco Covid data
def fPlotSFCovid(pFileName):
    x = []  # dates
    y = []  # moving averages
    
    # Read the file and extract date and moving average data
    with open(pFileName, "r") as file:
        for line in file:
            date, cases, mov_avg = line.strip().split(",")
            x.append(date)
            y.append(float(mov_avg))
    
    # Customize the plot axes
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
    
    # Create the scatter plot
    plt.scatter(x, y, c='blue')
    
    # Show the plot
    plt.show()