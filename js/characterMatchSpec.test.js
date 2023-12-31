var ana = require("./characterMatch");

// Part 1 Tests
describe("isCharacterMatch Tests", () => {
    test("Test 1", () => { 
      expect(ana.isCharacterMatch('charm', 'march')).toEqual(true);
    });

    test("Test 2", () => { 
        expect(ana.isCharacterMatch('zach', 'attack')).toEqual(false);
      });

    test("Test 3", () => { 
    expect(ana.isCharacterMatch('CharM', 'mARcH')).toEqual(true);
    });

    test("Test 4", () => { 
    expect(ana.isCharacterMatch('abcde2', 'c2abed')).toEqual(true);
    });
  });

// Part 2 Tests
list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"];

describe("anagramsFor Tests", () => {
    test("Test list of words with several anagrams", () => { 
      expect(ana.anagramsFor("threads", list_of_words)).toEqual(["threads", "trashed", "hardest", "hatreds"]);
    });

    test("Test that will produce no output", () => { 
        expect(ana.anagramsFor("apple", list_of_words)).toEqual([]);
      });
  });