
// 1 : Print odds 1-20

function printOddNumTo20() { 
    for ( var i = 1; i < 20 ; i++){
        if ( i % 2 != 0 ){
            console.log(i);
        }
    }
}

printOddNumTo20();

// 2 Sum and Print 1-5

function sumAndPrint1To5() {
    var sum = 0;
    for ( var i = 1; i <= 5 ; i++){
        sum+= i;
        console.log("Num "+i+", Sum "+sum);
    }
}

sumAndPrint1To5();