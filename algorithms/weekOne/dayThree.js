// Reverse Array
// -----------------------------------------------------
// Given a numerical array, reverse the order of the
// values. The reversed array should have the same
// length, with existing elements moved to other
// indices so that the order of elements is reversed.
// [1,2,3,4,5] -> [5,4,3,2,1]

var arr = [1,2,3,4,5];

function reverseArray(arr){
    for (var i = 0, j = arr.length-1 ; i < arr.length/2 ; i++, j--){
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}

console.log(reverseArray(arr));

// Remove Negatives
// -----------------------------------------------------
// Implement a function removeNegatives() that
// accepts an array and removes any values that
// are less than zero.
// Second-level challenge: don’t use nested loops.
//[5,-2,4,-2,-2] -> [5,4]

arr = [5,-2,4,-2,-2];

function removeNegatives(arr) { 
    var newArr = [];
    for (var i = 0 ; i < arr.length ; i++){
        if ( arr[i] > 0 ){
            newArr.push(arr[i]);
        }
    }
    return newArr;
}

console.log(removeNegatives(arr));

// Skyline Heights
// -----------------------------------------------------
// You are given an array with heights of consecutive buildings in the city. For example, [-1,7,3] would
// represent three buildings: first is actually below street level, second is seven stories high, and third is
// three stories high (but hidden behind the seven-story onbe). You are situated at street level. Return an
// array containing heights of the buildings you can see, in order. Given [1,-1,7,3] return [1,7].
//[4,2,6,3,8,7,1,9]

arr = [4,2,6,3,8,7,1,9];

function skylineHeights(arr){
    var newArr = [];
    var max = 0;
    for (var i = 0 ; i < arr.length ; i++){
        if (max < arr[i]){
            newArr.push(arr[i]);
            max = arr[i];
        }
    }
    return newArr;
}

console.log(skylineHeights(arr));