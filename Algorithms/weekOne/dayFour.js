// Rotate Array
// -----------------------------------------------------
// Implement rotateArr(arr, shiftBy) that
// accepts array and offset. Shift arr’s values to the
// right by that amount. ‘Wrap-around’ any values
// that shift off array’s end to the other side, so that
// no data is lost. Operate in-place: given
// ([1,2,3],1), change the array to [3,1,2].

// Optionally, add these advanced features:
//     a) allow a negative shiftBy (shift left, not right),
//     b) minimize memory usage. With only a few local
//         variables (not an array), handle arrays and
//         shiftBys in the millions,
//     c) minimize how many touches of each element.

var arr = [1,2,3,4,5,6];

function rotateArr(arr, shiftBy){
    for ( var i = 0 ; i < shiftBy ; i++ ){
        for ( var j = arr.length ; j > 0 ; j-- ){
            arr[j] = arr[j-1];
        }
        arr[0] = arr[arr.length-1];
        arr.length--;
    }
    return arr;
}

console.log(rotateArr(arr, 2));

// Min Of Sorted-Rotated
// -----------------------------------------------------
// You will be given a numerical array that has first
// been sorted, then rotated by an unknown
// amount. Find and return the minimum value in
// that array.

function minOfSortedRotated(arr){
    var min = arr[0];
    for ( var i = 0 ; i < arr.length ; i++ ){
        if ( arr[i] < min ) {
            min = arr[i]; 
        }
    }
    return min;
}

console.log(minOfSortedRotated(arr));