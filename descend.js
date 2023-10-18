function descendingOrder(n) {
  const digitsArray = [];
  let num = n;

  while (num > 0) {
    const digit = num % 10;
    digitsArray.push(digit);
    num = Math.floor(num / 10);
  }

  for (let i = 0; i < digitsArray.length - 1; i++) {
    for (let j = 0; j < digitsArray.length - i - 1; j++) {
      if (digitsArray[j] < digitsArray[j + 1]) {
        const temp = digitsArray[j];
        digitsArray[j] = digitsArray[j + 1];
        digitsArray[j + 1] = temp;
      }
    }
  }

  let result = 0;
  for (let digit of digitsArray) {
    result = result * 10 + digit;
  }

  return result;
}

// Example usage
const num = 14532;
const result = descendingOrder(num);
console.log(result);  // Output: 54321
 