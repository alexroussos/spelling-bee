import argparse
import re
import json
import requests

# Ruin the spelling bee https://www.nytimes.com/puzzles/spelling-bee
#
# Setup:
#
# $ pipenv install requests
# $ pipenv shell
#
# Usage:
#
#	show matches without submitting( eg for a puzzle with the letters NAMTOID where the cetner letter is O):
#
#		python spelling-bee.py  -w ~/Downloads/words.txt -c o -l namtoid 
#
# 	auto-submit matches to NYT:
#	
#		python spelling-bee.py  -w ~/Downloads/words.txt -c o -l namtoid -p 9477 -s <token>
#
#
# Word lists:
# - 480k word list: https://github.com/dwyl/english-words/blob/master/words.txt
# - 58k word list: http://www.mieliestronk.com/corncob_lowercase.txt
# 

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--word_file", required=True, help="path to word list")
ap.add_argument("-c", "--center_letter", required=True, help="center letter")
ap.add_argument("-l", "--letters", required=True, help="other allowed letters")
ap.add_argument("-p", "--puzzle_id", required=False, type=int, help="puzzle ID from PUT request; will attempted to submit words if provided")
ap.add_argument("-s", "--nyt_s", required=False, help="value of 'nyt-s' header from PUT request")
args = vars(ap.parse_args())

SUBMIT_WORD_URL = "https://nyt-games-prd.appspot.com/svc/spelling-bee/v1/game.json"

def submit_words(words, puzzle_id, nyt_s):
    response = requests.put(
        url = SUBMIT_WORD_URL,
        json = { 
            "puzzleID": puzzle_id,
            "answers": words
        },
        headers = {
        	"content-type": "application/json",
        	'Accept':'application/json',
        	"nyt-s": nyt_s
        }
    )

    return response

def find_matching_words(word_file, center_letter, letters):
	# TODO take in list of words, not file path
	pattern = "^[%s%s]*$" % (center_letter, letters)
	expression = re.compile(pattern)
	matching_words = []
	with open(word_file) as words:
		for w in words:
			word = w.strip().lower()
			if len(word) > 3 and center_letter in word and re.search(expression, word):
				matching_words.append(word)
	return matching_words

# Find all the matching words
word_file = args["word_file"]
center_letter = args["center_letter"].lower()
letters = args["letters"].lower()
matching_words = find_matching_words(word_file, center_letter, letters)
print("Found: " + ", ".join(matching_words))

# Submit words to NYT
puzzle_id = args["puzzle_id"]
nyt_s = args["nyt_s"]
if puzzle_id:
	response = submit_words(matching_words, puzzle_id, nyt_s)
	print("Submitted: " + str(response))
	



