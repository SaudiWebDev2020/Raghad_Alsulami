// Arrs2Map
// ----------------------------------------------------------------------------------------------------------------
// Given two arrays, create an associative array (map) containing keys of the first, and values of the
// second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc":
// 42, 3: "wassup", "yo": true}.

var arr1 = ["abc", 3, "yo"], arr2 = [42, "wassup", true];

function arrs2Map(arr1, arr2){
    var obj = {};
    for (var i = 0 ; i < arr1.length ; i++){
        obj[arr1[i]] = arr2[i];
    }
    return obj;
}

console.log(arrs2Map(arr1, arr2));


// InvertHash
// ----------------------------------------------------------------------------------------------------------------
// Create invertHash(assocArr) that converts a hash’s keys to values and values to corresponding keys.
// Example: given {"name": "Zaphod"; "numHeads": 2}, return {"Zaphod": "name"; 2:
// "numHeads"}. You will need to learn and use a JavaScript for ... in h ere!

var object = {"name": "Zaphod", "numHeads": 2};
function invertHash(obj) {

}
console.log(object);

// ReverseString
// ----------------------------------------------------------------------------------------------------------------
// Implement a function reverseString(str) that, given a string, will return the string of the same length but
// with characters reversed. Example: given "creature", return "erutaerc". Do not use the built-in
// reverse() function!

var str = "creature";

function reverseString(str){
    var newString = "";
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}

console.log(reverseString(str));