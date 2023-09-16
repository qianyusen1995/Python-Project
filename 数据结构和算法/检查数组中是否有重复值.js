function hasDuplicateValue(array) {
  var steps = 0;
  var existingNumbers = [];
  for (var i = 0; i < array.length; i++) {
    steps++
    if(existingNumbers[array[i]] === undefined) { //array[i]在array = [3, 5, 8]
      existingNumbers[array[i]] = 1;
    } else {
      return true;
    }
  }
  console.log(existingNumbers);
  console.log(steps);
  return false;
}

hasDuplicateValue([3, 5, 8]);
