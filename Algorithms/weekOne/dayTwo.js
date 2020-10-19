// Today's Algo challenges (Do not use any built in JS methods):

arr = [1,2,3,4];
val = 5;
index = 2;

//  Array: Push Front
function pushFront(arr, val) {
    for ( var i = arr.length ; i > 0 ; i-- ){
        arr[i] = arr[i-1];
    }
    arr[0] = val;
    return arr;
}

console.log(pushFront(arr, val));

//  Array: Pop Front, remove and return first val
function popFront(arr) {
    for ( var i = 0 ; i < arr.length ; i++ ){
        arr[i] = arr[i+1];
    }
    arr.length--;
    return arr;
}

console.log(popFront(arr));

//  Array: Insert At, insert at the index
function insertAt(arr, index, val){ // ([], 0, 1)
    for ( var i = arr.length ; i > index ; i-- ){
        arr[i] = arr[i-1];
    }
    arr[index] = val;
    return arr;
} 

console.log(insertAt(arr, index, val));

//  Array: Remove At
function removeAt(arr, index){
    for ( var i = index ; i < arr.length ; i++ ){
        arr[i] = arr[i+1];
    }
    arr.length--;
    return arr;
}

console.log(removeAt(arr, index));