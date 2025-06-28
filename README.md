# codex-test

This repository contains a simple lottery predictor script.

## Usage

Prepare a CSV file with past results, each line containing three numbers in the range 1-6, e.g.

```
1,3,5
2,6,4
...
```

Run the predictor specifying how many past draws to analyze and which position to predict:

```
python lottery_predictor.py path/to/data.csv -N 100 -p 1
```

The script prints the number with the highest observed frequency and its probability distribution based on the last `N` draws.

Note: Lottery games are typically random; this script cannot guarantee accurate predictions.
