
// Binary Search
// ------------------------------------------------------------
// Given a sorted array and a value, return whether
// that value is present in the array. Do not
// sequentially iterate the entire array. Instead,
// ‘divide and conquer’, taking advantage of the fact
// that the array is sorted.

var arr = [2,40,66,99,300];

function binarySearch(arr, value) {
    var start = 0;
    var end = arr.length-1;
    while (start <= end){ 
        let mid=Math.floor((start + end)/2); 
        if (arr[mid]===value) {
            return true;
        } else if (arr[mid] < value) {
            start = mid + 1; 
        } else{
            end = mid - 1; 
        }
    } 
    return false; 
}

console.log(binarySearch(arr, 55))

// Pairs to Sum
// ------------------------------------------------------------
// How do you find all pairs of an integer array whose sum is equal to a given number?
function pairsToSum(arr, num){
    var pairs = [];
    for (var i = 0; i < arr.length; i++) {
        for (var j = i + 1; j < arr.length; j++) 
            if ((arr[i] + arr[j]) == num) 
            pairs += [arr[i],arr[j]] + "\n"
    }
    return pairs
}
console.log(pairsToSum([3,8,5,1,8,7,3,4,0], 8))
