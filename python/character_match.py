# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	if sorted(string1.lower().replace(" ", "")) == sorted(string2.lower().replace(" ", "")):
		return True
	return False

def char_counter(char, list):
	count = 0
	for element in list:
		if element == char:
			count += 1
	return count

def is_character_match_complex(string1, string2):
	string1_arr = list(string1.replace(" ", "").lower())
	string2_arr = list(string2.replace(" ", "").lower())
	for character in string1_arr:
		if char_counter(character, string1_arr) != char_counter(character, string2_arr):
			return False
	return True

# Part 2
def anagrams_for(word, list_of_words):
	# your code here
	pass
