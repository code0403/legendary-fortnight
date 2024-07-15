function subsets(arr) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
      const currentSubset = [];
      for (let j = i; j < arr.length; j++) {
        currentSubset.push(arr[j]);
        result.push(currentSubset);
      }
    }
    return result;
  }
  
  const inputArray = [1, 2, 3];
  const resultSubsets = subsets(inputArray);
  
  console.log(resultSubsets);