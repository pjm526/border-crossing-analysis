# Border Crossing Analysis - Data Insight Challenge

## Approach

* **Created a nested dictionary for loading the data in the format: 
           { (Border, Measure) : { Date : Value}}**
* **Calculated the total number of crossings across border each month.**
  1. The dictionary was grouped first by a tuple of Border and Measure.
  2. Performed sum by group on date in the second layer.
  
* **Calculated running monthly average of total number of crossings for that type of crossing and border.**
  1. Initialized another dictionary with sum of value as key and value as the calculated running average.
  2. Maintained the value of sum and total no of months by sorting on date
  3. Further looped on the number of values for each date key.
  
* **Created Lists and merged the corresponding values.**

* **Sorted the final list created on date to get the required output.**

* **Stored output list in a csv file.**
  
### Takeaways
* The given code is developed using python3.7.
* Libraries like csv, math and sys have been used for file related operations.
* Script has been run and tested on subsets of dataset as well as on the entire dataset.

