/* 
  String: Reverse

  Given a string,
  return a new string that is the given string reversed
*/

var str1 = "creature";
var expected1 = "erutaerc"; "erutaerc"

var str2 = "car";
var expected2 = "rac";

var str3 = "hello";
var expected3 = "olleh";

var str4 = "";
var expected4 = "";

/**
 * Reverses the given str.
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str = "") {
  var reversed = "";

  for (var i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  return reversed;
}

console.log(reverseString(str1));
console.log(reverseString(str1) === expected1);