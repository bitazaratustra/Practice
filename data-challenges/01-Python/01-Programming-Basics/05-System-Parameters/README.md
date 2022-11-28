Python scripts can read arguments passed in the command line. This may come in handy when you want to add options to your script.

## A note about `sys.argv`

Consider the following code:

```python
# args.py
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
```

You can save it in the file called `args.py` and run it:

```bash
python args.py arg1 arg2 arg3
# Number of arguments: 4 arguments.
# Argument List: ['args.py', 'arg1', 'arg2', 'arg3']
```

[`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) is a python **list** containing the command line arguments passed to a Python script. `argv[0]` is always the script name.

## Exercise

Let's write a simple calculator for **integers**. Here's how it should work:

```bash
python calc.py 4 + 5
# => 9
python calc.py 2 \* 6
# => 12
python calc.py 3 - 9
# => -6
```

⚠️ Note the backslash before the `*` above. This is because the `*` is a special character and we have to 'escape' it.

Open the `calc.py` file and implement this behavior! You will find that a `main` function is automatically executed thanks to [this feature](https://docs.python.org/3/library/__main__.html).

💡 **Hint**: Don't hesitate to `print()` a lot, to better understand how the program behaves.

## Going Further

If you have to build a serious CLI tool with Python, please consider the built-in [`argparse`](https://docs.python.org/3/library/argparse.html).
