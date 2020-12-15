// Find maximum product of two integers in an array
// ---------------------------------------------------------------------------------
// Given an array of integers, find maximum product of two integers in an array
// input = [4,7,2,9,5]
// output = 63 (7*9)
// input =[5,-4,2,6,-8]
// output = 32 (-8*-4)
var arr = [4,7,2,9,5];

function pairsToMaxProduct(arr){
    var max = 0;
    var pair = [];
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < i; j++) 
            if ((arr[i] * arr[j]) > max) 
                max = arr[i] * arr[j];
                pair = arr[i]+"*"+arr[j]
    }
    return max +", "+pair
}

console.log(pairsToMaxProduct(arr))

// Move all zeros present in an array to the end
// ---------------------------------------------------------------------------------
// Given an array of intefers, move all zeros present in the array to the end.  The solution should maintain the relative order of items in the array.
// NO NEW ARRAY

// input = [6,0,8,2,3,4,0,4,0,1]
// output = [6,8,2,3,4,4,1,0,0,0]

function moveZeroToEnd(arr){
    var count = 0;  
    for (var i = 0; i < arr.length; i++) 
        if (arr[i] != 0) 
            arr[count++] = arr[i];
    while (count < arr.length) 
        arr[count++] = 0; 
    return arr
}

console.log(moveZeroToEnd([6,0,8,2,3,4,0,4,0,1]))