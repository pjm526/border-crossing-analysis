# Border Crossing Analysis - Data Insight Challenge

## Approach

1. **Created a nested dictionary for loading the data in the format: 
           { (Border, Measure) : { Date : Value}}**
2. **Calculated the total number of crossings across border each month.**
  1. The dictionary was grouped first by a tuple of Border and Measure.
  2. Performed sum by group on date in the second layer.
  
3. **Calculated running monthly average of total number of crossings for that type of crossing and border.**
  1. Initialized another dictionary with sum of value as key and value as the calculated running average.
  2. Maintained the value of sum and total no of months by sorting on date
  3. Further looped on the number of values for each date key.
  
4. **Created Lists and merged the corresponding values**

5. **Sorted the final list created on date to get the required output**

6. **Stored output list in a csv file**
  

