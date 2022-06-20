# What I Learned 

## argmin without numpy 

```python
def argmin(x):
    return min(range(len(x)), key =lambda i:x[i])
```
