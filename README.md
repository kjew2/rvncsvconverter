# rvncsvconverter

Converts rvn exports to cointracker format

## Getting Started

In rvncore wallet use extract button to generate csv

### Executing program

* download script
* pass filepath of csv and pass mining payout and a threshold in flags
* payout: amount you receive in each mining payout
* threshold: how close transaction needs to be to be considered a mining transaction
```
python rvncsvconverter.py yourpathtocsv --payout 10 --threshold 5
```
