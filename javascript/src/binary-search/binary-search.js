function findMiddle(min, max) {
  return Math.floor((min + max) / 2);
}

export function binarySearch(arr, target, min, max) {
  if (min > max) {
    return -1;
  }

  const middle = findMiddle(min, max);
  const arrMiddle = arr[middle];

  if (arrMiddle > target) {
    return binarySearch(arr, target, min, middle - 1)
  } else if (arrMiddle < target) {
    return binarySearch(arr, target, middle + 1, max)
  } else {
    return middle;
  }
}