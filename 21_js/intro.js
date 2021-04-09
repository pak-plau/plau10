var factI = (n) => {
    var temp = 1;
    for (var i = 1; i <= n; i++) {
        temp *= i;
    }
    return temp;
}

var factR = (n) => {
    if(n == 1 || n == 0) {
        return 1;
    }else {
        return n * factR(n - 1);
    }
}

var fibI = (n) => {
    var a = 0;
    var b = 1;
    var c = 1;
    for(var i = 0; i < n; i++) {
        a = b;
        b = c;
        c = a + b;
    }
    return a;
}

var fibR = (n) => {
    if(n == 0) {
        return 0;
    }else if(n == 1 || n == 2) {
        return 1;
    }else {
        return fibR(n - 1) + fibR(n - 2);
    }
}
