// 1

function printTo255() {
    for (var i = 1 ; i <= 255 ; i++){ 
        console.log(i);
    }
}

// 2 

function printIntsAndSum0To255() { 
    sum = 0;
    for (var i = 1 ; i <= 255 ; i++){ 
        console.log(i);
        sum += i;
        console.log(sum);
    }
}

// 3

function printMaxOfArray(arr) { 
    max = Math.max(arr);
    console.log(max);
}

// 4 

function returnOddsArray1To255() { 
    oddArr = [];
    for (var i = 1 ; i <= 255 ; i++){ 
        if ( i % 2 == 1) { 
            oddArr.push(i);
        }
    }
    return oddArr;
}

// 5 

function returnArrayCountGreaterThanY(arr, Y){ 
    arrGreaterThanY = [];
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( arr[i] > Y){ 
            arrGreaterThanY.push(arr[i]);
        }
    }
}

// 6 

function printMaxMinAverageArrayVals(arr) { 
    max = Math.max(arr);
    console.log(max);

    min = Math.min(arr);
    console.log(min);

    avg = Math.avg(arr);
    console.log(avg);
}

// 7 

function swapStringForArrayNegativeVals(arr) { 
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( arr[i] < 0 ){ 
            arr[i] = 'Dojo';
        }
    }
}


// 8 

function printOdds1To255() { 
    for (var i = 1 ; i <= 255 ; i++){ 
        if ( i % 2 == 1) { 
            console.log(i);
        }
    }
}

// 9 

function printArrayVals(arr){ 
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        console.log(i);
    }
}

// 10 

function printAverageOfArray(arr){ 
    avg = arr.avg(arr); 
    console.log(avg);
}

// 11

function squareArrayVals(arr){ 
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        squar = Math.sqrt(arr[i]);
        arr[i] = squar;
    }
}

// 12 

function zeroOutArrayNegativeVals(arr){
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( i < 0 ) {
            arr[i] = 0; 
        }
    }
}

// 13 

function shiftArrayValsLeft(arr){
    lastIndex = arr.length-1;
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if (i < arr.length-1) {
        arr[i] = arr[i + 1];
        } else { 
            arr[lastIndex] = 0;
        }
    }
}

