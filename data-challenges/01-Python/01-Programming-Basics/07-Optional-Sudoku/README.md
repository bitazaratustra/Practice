Congratulations for reaching this exercise! We are going to implement a Sudoku Validator. The goal is simple: given a **9x9 Sudoku grid**, determine if it's valid!

![](https://res.cloudinary.com/wagon/image/upload/v1560713910/sudoku_szhhdf.png)

## Rules

A sudoku is valid if and only if:

- A row contains all numbers from `1` to `9`
- A column contains all numbers from `1` to `9`
- Each of the nine 3x3 little squares contains numbers from `1` to `9`

## Data Model

A Sudoku grid will be represented by a Python list of lists:

```python
grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]
```

With that structure in mind, you can access a cell at row `i` and column `j` with the following statement:

```python
grid[i][j]
```

💡 Remember that python list indices start at **`0`**, so `i` and `j` values are between `0` and `8`.

## Exercise

Open the `sudoku.py` file and implement the `sudoku_validator()` method. To check if your code is working, run the tests with:

```bash
make
```
