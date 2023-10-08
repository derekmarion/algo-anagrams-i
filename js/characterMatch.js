isCharacterMatch = function(string1, string2) {
	const sortedString1 = string1.toLowerCase().replace(/\s/g, "").split("").sort().join(""); //make into array, sort, crunch whitespace, then reform string
	const sortedString2 = string2.toLowerCase().replace(/\s/g, "").split("").sort().join("");
	return sortedString1 === sortedString2 //deep equality to cover true and false returns without conditional statement
};

anagramsFor = function(word, listOfWords) {
	let output = [];
	const sortedWord = word.toLowerCase().replace(/\s/g, "").split("").sort().join("");
	for (element of listOfWords) {
		sortedElement = element.toLowerCase().replace(/\s/g, "").split("").sort().join("");
		if (sortedWord === sortedElement) {
			output.push(element);
		}
	}
	return output;
};

module.exports = {isCharacterMatch, anagramsFor};
