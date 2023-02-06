/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

var str1 = "object oriented programming";
var expected1 = "OOP";

// The 4 pillars of OOP
var str2 = "abstraction polymorphism inheritance encapsulation";
var expected2 = "APIE";

var str3 = "software development life cycle";
var expected3 = "SDLC";

//? Bonus: ignore extra spaces
var str4 = "  global   information tracker    ";
var expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {

  var acronym = ""
  var wordsArr = str.split(" ")
  // console.log(wordsArr);
  for (var word of wordsArr){
    // check if a word exists

    if(word !== ""){
      acronym += word[0].toUpperCase();
    }
  }

  return acronym


}
// Student solution
function acronymize2(str){
var currentStr = ""
currentStr += str[0]

for(var i= 1; i< str.length; i++){
 if (str[i] == " " && str[i+1] != " "){
  currentStr += str[i+1]
 }
}
return currentStr.toUpperCase()
}

console.log(acronymize2(str4));
/*****************************************************************************/

/**
 * @param {string} wordsStr
 * @returns {string}
 */
function acronymizeWithSplit(wordsStr = "") {
  var acronym = "";
  var wordsArr = wordsStr.split(" ");

  for (var word of wordsArr) {
    // Splitting can result in empty strings.
    if (word !== "") {
      console.log(word);
      // upper case each letter as it's added so toUpperCase doesn't have
      // to loop over each acronym char at the end to upper case.
      acronym += word[0].toUpperCase();
    }
  }
  return acronym;
}

/**
 * @param {string} wordsStr
 * @returns {string}
 */
function acronymize(wordsStr = "") {
  var acronym = "";

  for (var i = 0; i < wordsStr.length; i++) {
    // These booleans add readability because they are named descriptively,
    // they also simplify how many conditional statements or nested conditions
    // are needed.
    var currentChar = wordsStr[i];
    var isCurrentCharSpace = currentChar === " ";
    var isPreviousCharSpace = wordsStr[i - 1] === " ";
    var isFirstletterOfWord =
      (i === 0 && !isCurrentCharSpace) ||
      (!isCurrentCharSpace && isPreviousCharSpace);

    if (isFirstletterOfWord) {
      acronym += currentChar.toUpperCase();
    }
  }
  return acronym;
}

/**

 * @param {string} wordsStr
 * @returns {string}
 */
function acronymize2(wordsStr = "") {
  var acronym = "";

  for (var i = 0; i < wordsStr.length; i++) {
    var currentChar = wordsStr[i];
    var isCurrentCharSpace = currentChar === " ";
    var isPreviousCharSpace = wordsStr[i - 1] === " ";
    var isFirstletterOfWord = !isCurrentCharSpace && isPreviousCharSpace;

    // Special case for idx 0 being start of word.
    if (i === 0 && !isCurrentCharSpace) {
      isFirstletterOfWord = true;
    }

    if (isFirstletterOfWord) {
      acronym += currentChar.toUpperCase();
    }
  }
  return acronym;
}

/**
 * Manually split into words to get the first letter of each.

 * @param {string} wordsStr
 * @returns {string}
 */
function acronymize3(wordsStr = "") {
  var acronym = "";
  var currentWord = "";

  for (var i = 0; i < wordsStr.length; i++) {
    var isSpace = wordsStr[i] === " ";

    if (currentWord.length > 0 && isSpace) {
      acronym += currentWord[0].toUpperCase();
      // reset for next word.
      currentWord = "";
    } else if (isSpace === false) {
      currentWord += wordsStr[i];
    }

    // Reaching the end also indicates the current word is compvare.
    if (i === wordsStr.length - 1 && currentWord.length > 0) {
      acronym += currentWord[0].toUpperCase();
    }
  }
  return acronym;
}

/**

 * @param {string} s
 * @returns {string}
 */
var functionalAcronymize = (s = "") =>
  s
    // Regex can be used if more control over split is needed.
    // This example removes any non alphabetical chars with split.
    .split(/[^A-Za-z]/)
    // Create a new array without empty strings from the split array.
    .filter((word) => word.length > 0)
    // map the filtered words into a new arr of upper-cased first letters.
    .map((word) => word[0].toUpperCase())
    // join the mapped array of first letters together without a separator.
    .join("");


    // acronymizeWithSplit(str1)
module.exports = {
  acronymizeWithSplit,
  acronymize,
  acronymize2,
  acronymize3,
  functionalAcronymize,
};
