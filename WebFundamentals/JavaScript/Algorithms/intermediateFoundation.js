// Intermediate Foundation

arr = [9,2,3,6,4,1,7];
arrStr = [42, true, 4, "Liam", 7];

// 1 : Sigma

function sigma(num){
    var count;
    for ( var i = 1 ; i <= num ; i++){
        count += i;
    }
    return count;
}

//console.log(sigma(3));

// 2 : Factorial

function factorial(num){
    var count;
    for ( var i = 1 ; i <= num ; i++){
        count *= i;
    }
    return count;
}

//console.log(factorial(5));

// 3 : Fibonacci

function fibonacci(num) {
    var a = 1, b = 0, temp;
    while (num >= 0){
        temp = a;
        a = a + b;
        b = temp;
        num--;
    }
    return b;
}

//console.log(fibonacci(6));

// 4 : Array: Second-to-Last

function secondToLast(arr) {
    if (arr.length < 1 ){
        return null;
    }else{
        return arr[arr.length-2];
    }
}

//console.log(secondToLast(arrStr));

// 5 : Array: Nth-to-Last

function nthToLast(arr, num){
    var value;
    for (var i = 0, j = arr.length-1 ; i < num; i++, j--){
        value = arr[j];
    }
    return value;
}

//console.log(nthToLast(arr, 3));

// 6 : Array: Second-Largest

function secondLargest(arr) {
    var max = arr[0], index;
    for (var i = 0 ; i < arr.length ; i++){
        if ( arr[i] > max ){
            max = arr[i];
            index = i;
        }
    }
    if (index > 0){
        return arr[index-1];
    }else { 
        return arr[arr.length-1]
    }
}

//console.log(secondLargest(arr));

// 7 : Double Trouble

function doubleTrouble(arr) {
    var newArr = [];
    for (var i = 0 ; i < arr.length ; i++){
        newArr.push(arr[i], arr[i]);
    }
    return newArr;
}

console.log(doubleTrouble(arrStr));


