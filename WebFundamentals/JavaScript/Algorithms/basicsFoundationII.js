arr = [1,2,3,4];
strArr = ['domain', 'dojo', 'world']
arrSwap = [true,42,"Ada",2,"pizza"];

// 1
function makeItBig(arr) {
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] > 0) {
            arr[index] = "big";
        }
    }
    return arr;
}

//console.log(makeItBig(arr));

// 2
function printLowReturnHigh(arr) {
    var low = arr[0];
    var high = 0;
    for (var i = 0 ; i < arr.length ; i++){
        if (arr[i]< low){
            low = arr[i];
        }else if (arr[i] > high){
            high = arr[i];
        }
    }
    console.log("Lowest value is "+low);
    return high;
}

//console.log("Highest value is "+ printLowReturnHigh(arr));

// 3
function printOneReturnOthers(arr) {
    for (var i = 1 ; i < arr.length ; i++){
        console.log("Element number "+ (i+1) +" is "+arr[i]);
    }
    return arr[0];
}

//console.log("The first element is "+printOneReturnOthers(arr));

// 4
function doubleVision(arr) {
    var newArr = [];
    for (var index = 0; index < arr.length; index++) {
        newArr.push(arr[index] + arr[index]);
    }
    return newArr;
}

//console.log(doubleVision(arr));

// 5
function countPositives(arr) {
    var count = 0;
    for (var index = 0; index < arr.length; index++) {
        if (arr[index] > 0) {
            count++;
        }
    }
    arr.pop();
    arr.push(count);
    return arr;
}

//console.log(doubleVision(arr));

// 6 
function evenAndOdd(arr) {
    var sum = 0;
    for (var i = 0 ; i < arr.length-1 ; i++){
        if (arr[i] > 0 ){
            sum+= arr[i];
        }
    }
    arr[arr.length-1] = sum;
    return arr;
}

//console.log(evenAndOdd(arr));

// 7
function incrementTheSeconds(arr){
    for (var i = 0 ; i < arr.length ; i++){
        if (i % 2 == 1 ){
            arr[i] += 1;
        }
    }
    return arr;
}

//console.log(incrementTheSeconds(arr));

// 8
function previousLengths(strArr){
    var preStr ='';
    for (var i = arr.length-1 ; i > 0 ; i--){
        preStr = strArr[i-1];
        strArr[i] = preStr.length;
    }
    return strArr;
}

//console.log(previousLengths(strArr));

// 9 
function addSeven(arr) {
    for (var i = 0 ; i < arr.length ; i++){
        arr[i] += 7;
    }
    return arr;
}

//console.log(addSeven(arr));

// 10
function reverseArray(arr){
    for (var i = 0, j = arr.length-1 ; i < arr.length/2 ; i++, j--){
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}

//console.log(reverseArray(arr));

// 11
function createNegativeArr(arr) {
    var newArr =[];
    for (var i = 0 ; i < arr.length ; i++){
        newArr.push(-arr[i]);
    }
    return newArr;
}

//console.log(createNegativeArr(arr));

// 12
function alwaysHungry(strArr) { 
    var count = 0;
    for (var i = 0 ; i < arr.length ; i++){
        if (arr[i] == "food"){
            console.log("yummy");
            count ++;
        }
    }
    if (count < 1){
        console.log("I'm hungry!");
    }
}

//alwaysHungry(strArr);

// 13 
function swapTowardToCenter(arr){
    var center = 0;
    if ( arr.length % 2 == 0 ){
        center = arr.length/2;
    }else {
        center = Math.floor((arr.length/2)-1);
    }
    for (var i = 0, j = arr.length-1 ; i < center ; i++, j--){
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}


console.log(swapTowardToCenter(arrSwap));

// 14
function scaleTheArray(arr, num) {
    for (var i = 0 ; i < arr.length ; i++){
        arr[i] += num;
    }
    return arr;
}

//console.log(scaleTheArray(arr, 3));
