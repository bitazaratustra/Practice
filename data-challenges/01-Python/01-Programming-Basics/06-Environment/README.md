Another way of modifying the behaviour of a Python script (other than command line arguments) is to use **environment variables**.

## Exercise

Open the `flask_option.py` file and implement the `start` function. It should return a `String` depending on the presence and value of the `FLASK_ENV` environment variable.

Here is the expected behavior:

```bash
FLASK_ENV=development python flask_option.py
# => "Starting in development mode..."

FLASK_ENV=production python flask_option.py
# => "Starting in production mode..."

python flask_option.py
# => "Starting in empty mode..."
```

💡 **Tip**: have a look at the `os.getenv` in the [`os`](https://docs.python.org/3/library/os.html) module.
