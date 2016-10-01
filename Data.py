import requests as req
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#Data = lambda text:text
def Data(w):
	import word
	try:
		return word.word[w]
	except:
		return None