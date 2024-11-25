function multiplyNumbers(a, b) {
    return a * b
}

// a = parseFloat(prompt("Unesi prvi broj:"))
// b = parseFloat(prompt("Unesi dr1ugi broj:"))
// document.write("<p>Umnožak ovi brojeva je: " + multiplyNumbers(a, b) + "</p>")

// number = parseInt(prompt("Unesi broj:"))
// document.write("<p>Factoriel broja " + number + " je: " + generatefactoriel(number) + "</p>")
function generatefactoriel(number) {
    let result = 1;
    for (i = 1; i <= number; i++) {
        result *= i
    }
    return result
}

// zadatak3();
function zadatak3() {
    let ime = prompt("Unesi ime");
    let godine = prompt("Unesi godine");
    document.write("<p>" + ime + " Ima " + godine + " godina</p>");
}

// zadatak4();
function zadatak4() {
    let brojevi = [];
    for (i = 1; i <= 100; i++) {
        if (i % 7 == 0) {
            brojevi.push(i);
        }
    }
    document.write("<p>" + brojevi.join(", ") + "</p>");
}

zadatak5();
function zadatak5() {
    let broj;
    do {
        broj = parseInt(prompt("Unesi broj"));
        if (broj != 0) {
            document.write("<p>" , broj , "</p>");
        }
    }
    while (broj != 0);

}





























































