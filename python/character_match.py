# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	if sorted(string1.lower()) == sorted(string2.lower()):
		return True
	return False

def is_character_match_complex(string1, string2):
	for character in string1:
		if character.lower() not in string2.lower():
			return False
		return True

# Part 2
def anagrams_for(word, list_of_words):
	# your code here
	pass
