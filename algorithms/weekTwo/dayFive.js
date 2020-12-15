// MostFrequentNumber
// ------------------------------------------------------------------------
// Given an array of interfers containing duplicates,return the majority element in the array if Present.
// Input = [2,8,7,2,2,5,2,3,1,2,2]
// Output = 2

var arr = [2,8,7,2,2,5,2,3,1,2,2];
var count = 0;
var mostFreq = 1;
var value;
function mostFrequentNumber(arr) {
    for (var i=0; i<arr.length; i++) {
        for (var j=i; j<arr.length; j++) {
            if (arr[i] == arr[j]){
                count++;
            }
            if (mostFreq < count) {
                mostFreq = count;
                value = arr[i];
            }
        }
        count = 0;
    }
    return value+" repeated, "+mostFreq+" times."
}

console.log(mostFrequentNumber(arr));

// Number of Steps to Reduce a Number to Zero
// // ------------------------------------------------------------------------
// Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
// Example
// Input: num = 8
// Output: 4
// Explanation: 
// Step 1) 8 is even; divide by 2 and obtain 4. 
// Step 2) 4 is even; divide by 2 and obtain 2. 
// Step 3) 2 is even; divide by 2 and obtain 1. 
// Step 4) 1 is odd; subtract 1 and obtain 0.

var val=5;
function sub(val){
    var count=0;
    while(val != 0){
        if(val % 2 != 0){
            val=val-1;
        }else {
            val=val/2;
        }
        count++;
    }
    return val;
}
console.log(sub(val));


