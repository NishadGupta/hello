# Python Hello World

This repository contains a minimal Flask application.

## Setup

Install dependencies and run the development server:

```
pip install -r requirements.txt
python app.py
```

Set the `IMDB_API_KEY` environment variable with your IMDb API key (for
example `k_1234567890`) and then visit `http://localhost:5000` to see a
list of the latest anime shows from IMDb. You can also edit `app.py` and
replace the placeholder API key with your own.

Navigate to `http://localhost:5000/stopwatch` to use a simple browser-based
stopwatch implemented in JavaScript.
