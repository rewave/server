Adding a new filter to the system
---------------------------------
The root directory of the app has a file called `basefilter.py`. 

To add a new filter, for example decimalfilter, create a new file called `decimalfilter.py`, extend the BaseFilter class and override the `_apply` method :

    from basefilter import BaseFilter
    
    class DecimalFilter(BaseFilter):
        def __init__(self, x, y, prescision):
            super(DecimalFilter, self).__init__(x,y)
            self.precision = precision
            
        def _apply(self, p):
            #do the filtering
            #don't access self.x or self.y
            #filter only p and return float
            p = round(p, self.precision)
		    return p if p**2> 0