isCharacterMatch = function(string1, string2) {
	const sortedString1 = string1.toLowerCase().replace(/\s/g, "").split("").sort().join(""); //make into array, sort, crunch whitespace, then reform string
	const sortedString2 = string2.toLowerCase().replace(/\s/g, "").split("").sort().join("");
	console.log(sortedString1);
	console.log(sortedString2);
	return sortedString1 === sortedString2 //deep equality to cover true and false returns without conditional statement
};

anagramsFor = function(word, listOfWords) {

};

module.exports = {isCharacterMatch, anagramsFor};
