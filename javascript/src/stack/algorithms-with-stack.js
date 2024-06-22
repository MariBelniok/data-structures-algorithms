import { Stack } from "./object-stack.js";

/**
 * Converts a decimal number to binary
 * 
 * @param {*} decNumber decimal number to be converted
 * @returns converted binary number as string
 * 
 * Complexity = O(n)
 */
export function decimalToBinary(decNumber) {
  const stack = new Stack();
  let number = decNumber;
  let rem;
  let binaryString = '';

  while (number > 0) {
    rem = Math.floor(number % 2);
    stack.push(rem);
    number = Math.floor(number / 2);
  }

  while(!stack.isEmpty()) {
    binaryString += stack.pop().toString()
  }

  return binaryString;
}
      