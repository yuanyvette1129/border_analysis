This was a data challenge project.

I used Python built-in modules instead of numpy and pandas packages to do data analysis. 


Here are the steps:

1. Read the data using csv module

2. I fixed data types, and did some exploratory data analysis have a better understanding of the data

3. To calculate total values per group of border, measure, date, I sorted the data by the group, used itertools.groupby to get the total, and stored the result.

4. To calculate running monthly average per group of border and measure, I used itertools.groupby again, and calcualted the cumulative sum in order to get the average.

5. I sorted the final result as requested, and save it into report.csv.
