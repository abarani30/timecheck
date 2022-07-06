## Time Validity:
This package will check the time validity through checking both of hours and minutes.

## How to install the package?

To install the package:<br>

`pip install time-check-validity`

## How to use the package?

To use the package inside your python file: <br>

```python
#import the class TimeCheck from the package name
from timecheck import TimeCheck <br>
#create a new object (instance) from TimeCheck class
myObj = TimeCheck()<br>
#Now, call the method validTime to check if the time is valid or not
print(myObj.validTime("10:45")) #output: True
print(myObj.validTime("10:65")) #output: False
```

