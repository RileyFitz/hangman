# Hangman
This is a simple implementation of a hangman game designed in vanilla python.

### Custom wordbanks/CSV's

This program supports custom wordbanks from external csv's, as long as they are in the same directory as hangman.py.

This can be initialized as such:

```
python3 hangman.py custom.csv
```


This does come with some caveats based off limitations of the vanilla csv loader in python.

Files must be of the format:
```
apple,banana,cucumber,...
```
And **NOT** the more common format of:
```
apple
banana
cucumber
...
```

A simple solution to generating a csv of the proper format, is to load your wordbank into a spreadsheet editor (Libre Calc, Google Sheets, or Microsoft Excel), and to transpose the column, then simply save or export to a csv file.
