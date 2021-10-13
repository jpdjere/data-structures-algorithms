for (let i = 0; i < n.length; i++) {
  console.log(i)
}

const hasPairWithSum = (data, sum) => {
  let low = 0;
  let high = data.length - 1;
  while(low < high) {
    const probableSum = data[low] + data[high];
    if(probableSum === sum) {
      return true
    } else if(probableSum < sum) {
      low = low + 1
    } else {
      high = high - 1;
    }
  }
  return false;
}

const hasPairWithSum = (data, sum) => {
  const complements = new Set();
  for(let num of data) {
    if(complements.has(num)) {
      return true;
    }
    complements.add(sum-num)
  }
  return false;
}