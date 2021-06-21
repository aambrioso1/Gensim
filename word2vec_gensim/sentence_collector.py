# sentence_collector.py

"""A program for collected the sentences from a text file and storing them in a panda dataframe

https://stackoverflow.com/questions/3549075/regex-to-find-all-sentences-of-text, 

The pater attern for finding a sentence: Upercase, then anything that is not in (;.!?), then one of (;.!?).

"""

import requests as req
import re
import os # Standard library.  Operating system interfaces. 
import pandas as pd

"""
# Index for all books in the GB of the numbers used in these URLs:  https://www.gutenberg.org/dirs/GUTINDEX.ALL
r1 = req.get('https://www.gutenberg.org/cache/epub/105/pg105.txt') # Persuasion

"""

"""
url1 = 'https://www.gutenberg.org/cache/epub/1787/pg1787.txt' # 'Hamlet'
url2 = 'https://www.gutenberg.org/cache/epub/1503/pg1503.txt' # 'King_Richard_III'
url3 = 'https://www.gutenberg.org/cache/epub/1135/pg1135.txt' # 'The_Tempest'
url4 = 'https://www.gutenberg.org/cache/epub/1514/pg1514.txt' # 'A_Midsummer_Night_s_Dream'
url5 = 'https://www.gutenberg.org/cache/epub/1534/pg1534.txt' # 'Antony and Cleopatra'
url6 = 'https://www.gutenberg.org/cache/epub/105/pg105.txt'   # 'Persuasion'
"""

def txt_to_df(url):
	"""retrieves the text at url and stores the sentences in a dataframe
	
	Dependencies:
	pandas, requests

	Arg:
	A url in string form linked to text (code test on urls from Project Gutenberg)

	Returns:
	A panda dataframe containing all the sentences in the text.

	"""
	# Get the information form the URL and turn it into text.
	res = req.get(url) # 
	text = str(res.text[1:]) # Skip first character of text file

	# Create a regular expression to find all the sentences in a string of text.
	pat = re.compile(r'([A-Z][^\.!?;]*[\.!?;])', re.M)
	sentences = pat.findall(text)

	df = pd.concat([pd.DataFrame([item], columns=['sentences']) for item in sentences], ignore_index=True)
	return df

"""
# Two ways to build the dataframe I need are discussed here:  
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
df = pd.DataFrame(columns=['sentences'])
for i, item in enumerate(sentences):	 
	df = df.append({'sentences': item}, ignore_index=True)
	if i < 30: print(item,'\n')
"""

# print(txt_to_df(URL)[:30])

