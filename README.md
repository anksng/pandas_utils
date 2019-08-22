# pandas_utils
A repo to perform various operations on pandas data frame columns


# Usage : 
```python
from pandas_utils import function
# df -> working dataframe 
corr = function.correlation_matrix_by_frequency(df)  # Initiate the class with working df
table=corr.calculate_correlation()     #Save the dataframe of correlation, can be used for further analysis

corr.plot_heatmap(table)       # Plots a heat map.

```
# Add more functionalities for common day to day column operations over pandas data frame
