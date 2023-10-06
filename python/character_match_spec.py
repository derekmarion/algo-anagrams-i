from character_match import is_character_match, is_character_match_complex, anagrams_for

# Part 1 testing is_character_match
def test_0():
    assert is_character_match('charm', 'march') == True
def test_1():
    assert is_character_match('zach', 'attack') == False
def test_2():
    assert is_character_match('CharM', 'mARcH') == True
def test_3():
    assert is_character_match('abcde2', 'c2abed') == True
def test_4():
    assert is_character_match('Anna Madrigal', 'A man and a girl') == True
def test_5():
    assert is_character_match('cat', 'Tacocat') == False

# Part 1 testing is_character_match_complex
def test_00():
    assert is_character_match_complex('charm', 'march') == True
def test_01():
    assert is_character_match_complex('zach', 'attack') == False
def test_02():
    assert is_character_match_complex('CharM', 'mARcH') == True
def test_03():
    assert is_character_match_complex('abcde2', 'c2abed') == True
def test_04():
    assert is_character_match_complex('Anna Madrigal', 'A man and a girl') == True
def test_05():
    assert is_character_match_complex('cat', 'Tacocat') == False
def test_06():
    assert is_character_match_complex('abba', 'abaa') == False

# Part 2

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

def test_anagrams_for():
    assert anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"]
    assert anagrams_for("apple", list_of_words) == []
