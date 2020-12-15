// Second-Largest
// -------------------------------------------------------
// Return the second-largest element of an array
var arr = [5, 2, 6, 7];

function secondLargest(arr){
    var max = arr[0];
    var index = 0;
    for(var i = 1; i < arr.length; i++){
        if (arr[i] > max ){
            max = arr[i];
            index = i;
        }
    }
    if ( index == arr.length-1 ){
        return arr[0];
    }
    return arr[index+1]
}

console.log(secondLargest(arr));

// Nth-Largest
// -------------------------------------------------------
// Given an array, return the Nth-largest element:
// there should be (N - 1) elements that are larger.

function nthLargest(arr, n) {
    arr.sort();
    return arr[arr.length - 2];
}

console.log(nthLargest(arr, 3));

// Shuffle
// -------------------------------------------------------
// Recreate the shuffle()built into JavaScript, to
// efficiently shuffle a given array’s values. Do you
// need to return anything from your function?

function shuffle(arr) {
    var j, x;
    for (var i = arr.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = arr[i];
        arr[i] = arr[j];
        arr[j] = x;
    }
    return arr;
}

console.log(shuffle(arr));