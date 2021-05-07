# spelling-bee
Beat the NYTimes Spelling Bee puzzle https://www.nytimes.com/puzzles/spelling-bee

Finds all solutions and (optionally) submits them to NYTimes on your behalf.

## Setup
Install Python and the `requests` library. If usinig `pipenv`:
```
pipenv install requests
pipenv shell
```
You will also need a dictionary of possible words to search. If submitting automatically, use the largest word list
* 480k word list: https://github.com/dwyl/english-words/blob/master/words.txt
* 58k word list: http://www.mieliestronk.com/corncob_lowercase.txt

## Usage
To show matching words without submitting. This example would solve a puzzle with the center letter `I` and `COILRTV` as the complete set of allowed letters.
```
python spelling-bee.py --word_file ~/Downloads/words.txt --center_letter i --letters coilrtv 
```
To automatically submit your answers, include the `--puzzle_id` and `--nyt_s` options. You can find the values for these by submitting a word on the NYTimes site and inspecting the request: `--puzzle_id` is `puzzleID` in the request body, and `--nyt_s` is the value from the `--nyt_s` header.
```
python spelling-bee.py --word_file ~/Downloads/words.txt --center_letter i --letters coilrtv --puzzle_id 12065 --nyt_s <value>
```
