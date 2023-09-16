//O(N)
function makeUpperCase(array) {
  var newArray = [];
  for (var i = 0; i < array.length; i++) {
    newArray[i] = array[i].toUpperCase();
  }
  return newArray;
}
//O(1)
function makeUpperCase(array) {
  var newArray = [];
  for (var i = 0; i < array.length; i++) {
    array[i] = array[i].toUpperCase();
  }
  return newArray;
}

//O(N^2)
function hasDuplicateValue(array) {
  var exisitingNumbers = [1,1];
  for(var i = 0; i < array.length; i++) {
    if (exisitingNumbers[array[i]] === undefined) {
      exisitingNumbers[array[i]] = 1;
    } else {
      return true;
    }
  }
  return false;
}
hasDuplicateValue([1,2,2])