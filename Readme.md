# LatestJpg 

A Simple python script to find the latest file in a directory path.

**note**: This is not asynchronious - it needs to be called each time to detect a file file. 

I believe *watchdog* will provide Asynch file scanning.

## Example useage 

```python
from LatestJpeg import LatestJpg
lj = LatestJpg("/Users/DrSpok/Dev/Astro/Images")
print(f"Most recent file is {lj.mostrecentfile()}")
```      
