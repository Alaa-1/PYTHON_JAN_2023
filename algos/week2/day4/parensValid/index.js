/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid
*/
//            i
const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = ")N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {

  var parens = []

  for (var i  = 0; i < str.length -1 ; i++){
    if(str[i] === '('){
      parens.push(str[i])

    } else if (str[i] === ')'){
      if(parens.length === 0 ){
        return false
      } else {
        parens.pop()
      }
    }
  }
  return parens.length === 0
}

/*****************************************************************************/
console.log(parensValid(str1)); 
console.log(parensValid(str2)); 
console.log(parensValid(str3)); 
console.log(parensValid(str4)); 