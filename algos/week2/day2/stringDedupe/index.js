/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

var str1 = "abcABC";
var expected1 = "abcABC";

var str2 = "helloo";
var expected2 = "helo";

var str3 = "";
var expected3 = "";

var str4 = "aa";
var expected4 = "a";

/**
 * De-dupes the given string.
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {

  var resultStr =""
  var freqDict = {}

  //* loop through the given str

  for (var i = 0; i<= str.length-1; i++){
    if(!freqDict[str[i]]){
      resultStr += str[i]
      freqDict[str[i]] = true;
      console.log(freqDict);
    }
  }
  return resultStr
}

/**
 * Keeps first occurrence, no hash table approach.
 * @param {string} str
 * @returns {string}
 */
function stringDedupe2(str = "") {
  var distinctStr = "";

  for (var char of str) {
    if (distinctStr.includes(char) === false) {
      distinctStr += char;
    }
  }
  return distinctStr;
}

var stringDedupeWithSet = (str = "") => [...new Set(str)].join("");