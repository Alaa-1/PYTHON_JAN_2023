/* 
  Given in an alumni interview in 2021.

  String Encode

  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */
//            a4|b2|c1|d3
//            v   v v   v
//          aaaa bb c ddd

var str1 = "aaaabbcddd";
var expected1 = "a4b2c1d3";

var str2 = "";
var expected2 = "";

var str3 = "a";
var expected3 = "a";

var str4 = "bbcc";
var expected4 = "bbcc"; 

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
/*****************************************************************************/
/**
 * @param {string} str
 * @returns {string}
 */

function strEncode(str = "") {
  var encoded = "";

  for (var i = 0; i < str.length; i++) {
    var currChar = str[i];
    var dupeCount = 1;

    while (str[i + 1] === currChar) {
      dupeCount++;
      i++;
    }
    encoded += currChar + dupeCount;
  }
  return encoded.length < str.length ? encoded : str;
}

/**
 * @param {string} str
 * @returns {string}
 */
function strEncodeHashTable(str = "") {
  var charFreq = {};
  var encoded = "";

  for (var char of str) {
    if (charFreq[char]) {
      charFreq[char]++;
    } else {
      charFreq[char] = 1;
    }
  }

  // iterate back over str to get the proper order
  // order of keys on obj is not guaranteed to be in order
  for (var char of str) {
    if (charFreq[char] > 0) {
      encoded += char + charFreq[char];
      // Next time the same letter is looked up, it won't be added again.
      charFreq[char] = 0;
    }
  }
  return encoded.length < str.length ? encoded : str;
}

console.log(strEncodeHashTable(str1));

module.exports = { strEncode, strEncodeHashTable };
