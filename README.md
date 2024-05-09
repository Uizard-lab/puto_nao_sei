# app-drinking

Please try to follow the example on the [src/Drinks.p](src/Drinks.py) file to save time on json/csv parsing. The
`json.load()` function already implements the logic to parse the files, it can even parse into an object you create,
like
the Drink class on the [src/Drinks.p](src/Drinks.py) file.

```python
json.load(file, object_hook=lambda x: Drinks.Drink(**x))
```

Powered by Phind, the best AI for coding questions 😉 -> """
object_hook
Parameter: object_hook
Purpose: This parameter is a function that will be called for each dictionary in the JSON data. The purpose of this hook
is to transform the dictionaries into other objects. In this case, it's used to convert each dictionary into an instance
of the Drinks.Drink class.
"""
