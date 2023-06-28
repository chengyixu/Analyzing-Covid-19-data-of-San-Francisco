Name:
ID:

While working on the code above, I faced a few challenges and utilized some resources to overcome them:

Reading and processing the input files: Initially, I had difficulty extracting the specific data needed for San Francisco County from the input files. To resolve this issue, I used the split() function to separate the values in each line, and then checked whether the line contained "San Francisco." This allowed me to extract the relevant data for further processing.
Handling data irregularities: I noticed that some daily case numbers were extremely large compared to the previous and following numbers. To address this problem, I set an upper limit of 2000 for daily cases, which helped to avoid any unrealistic data points.
Calculating the moving average: When calculating the 7-day moving average, I initially struggled with properly handling the first 6 days where there wasn't enough data to calculate the average. To overcome this, I set the first 6 values in the moving average list to 0 and then calculated the moving average for the 7th and higher values.
Creating the scatter plot: I had difficulty setting up the scatter plot to properly display the data with a reasonable number of ticks on the x and y axes. To solve this, I utilized the matplotlib.pyplot module and its MaxNLocator function to set the number of major tick locations on both axes. This made the plot more readable and informative.
During the development process, I referred to the official Python documentation and various online resources, such as Stack Overflow, to clarify doubts and gather information on different functions and techniques. Additionally, I relied on my previous programming experience and knowledge to help me effectively structure and write the code.