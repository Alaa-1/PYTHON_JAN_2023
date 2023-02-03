/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */
const str1 = "a x a"; 
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!"; "!oho"
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).

 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {

for( var i =0; i < Math.floor(str.length/2); i ++){
leftchar = str[i]
rightchar = str[str.length - 1 - i]

if (leftChar !==rightChar){
  
  return false
}
}
return true

}
console.log(isPalindrome(str4));
/*****************************************************************************/

// const functionIsPalindrome2 = (str = "") =>
  str === str.split("").reverse().join("");


function functionIsPalindrome2 (str = "") {
  return   str === str.split("").reverse().join("");

}












var word ="Hi"

/**

 * @param {string} str
 * @returns {boolean}
 */
function isPalindrome(str = "") {
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    // Looping inwards from both sides.
    const leftChar = str[i];
    const rightChar = str[str.length - 1 - i];

    if (leftChar !== rightChar) {
      return false; // early exit
    }
  }
  return true;
}

/**

 * @param {string} str
 * @returns {boolean}
 */
const functionIsPalindrome = (str = "") =>
  str === str.split("").reverse().join("");

module.exports = { isPalindrome, functionIsPalindrome };
