
// Example merge sort
export const sortArray = (nums) => {
  let i = 1
  let sorted = [nums[0]]
  while (i < nums.length) {
    let current = nums[i]

    let j = 0
    while (j < sorted.length)  {
      
      if (current <= sorted[j]) {
        sorted.splice(j, 0, current)
        break
      } 
      else if (j === sorted.length -1) {
        sorted.push(current)
        break
      }
      j++
    }
    i++
  }
  return sorted
}

/**
 * https://leetcode.com/problems/merge-sorted-array
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
export const merge = function(nums1, m, nums2, n) {
  
  // Return version (ignores edge cases)
  // let k = 0
  // let i = 0
  // let j = 0
  // let c = []
  // nums1 = nums1.slice(0,m)
  // while (k < m + n) {
  //   if (nums1[i] <= nums2[j]) {
  //     c[k] = nums1[i]
  //     i++
  //   } else{
  //     c[k] = nums2[j]
  //     j++
  //   }
     
  //   k++
  // }
  // return c

  for (let i=0;i<nums2.length;i++){
      for(let j=0;j<nums1.length;j++){
          if (nums2[i]<=nums1[j] || (j === m)){
              nums1.pop()
              nums1.splice(j,0,nums2[i])
              m++
              break
          }
      }
  }
}

/**
 * An implementation of Karatsuba Multiplication (using recursion)
 * https://www.coursera.org/learn/algorithms-divide-conquer/exam/srsxO/programming-assignment-1/attempt
 * @param {number} num1
 * @param {number} num2
 * @param {number} base=10
 *
 * @return {number} 
 */
export const multiply = function(num1s,num2s) {
  console.log('============multiply()')
    console.log('num1',num1s)
    console.log('num2',num2s)
  
  
  // TODO: Figure out why this doesn't work properly
  
  try {
    
    if (!num1s || !num2s) {
      throw 'Error in multiply'
      return null
    }
    if (typeof(num1s) !== 'string') num1s = num1s.toString()
    if (typeof(num2s) !== 'string') num2s = num2s.toString()

    // Base case
    if ( num1s.length < 2 || num2s.length < 2) {
      return (parseInt(num1s) * parseInt(num2s)).toString()
    }

    // Process Strings
    
    let n = (num1s.length > num2s.length) ? num2s.length : num1s.length
    let x = Math.round(n/2)

    // First num
    console.log('num1:',num1s)
    console.log(typeof(num1s))
    let a = num1s.substr(0, num1s.length-x)
    let b = num1s.substr(num1s.length-x,num1s.length)
    
    // Second num
    let c = num2s.substr(0, num2s.length-x)
    let d = num2s.substr(num2s.length-x,num2s.length)

    if (!a || !b || !c || !d) throw 'ERROR!'
    console.log('----')
    console.log('a:',a)
    console.log('b:',b)
    console.log('c:',c)
    console.log('d:',d)

    // Recursion  
    let r1 = multiply(b,d)
    let r2 = multiply(stringAddition(a,b),stringAddition(c,d))
    let r3 = multiply(a,c)

    // if (r3.length > 10) {
    //   console.error('r3',r3)
    //   throw 'Too long'
    //   return false
    // }

    // let part1 = (r3 * Math.pow(10,2*x))
    
    let part1 = r3 * Math.pow(10,2*x)

    // let part2 = ( (r2-r3-r1) * Math.pow(10,x))
    let part2a = stringSubtraction(stringSubtraction(r2,r3),r1)
    let part2 = part2a * Math.pow(10,x)
    let part3 = r1
    
    // Return
    let response = stringAddition(stringAddition(part1,part2),part3)
    console.log('RESPONSE:',response)
    return response
  
  } catch (error) {
    console.error('ERROR ',error)
    return
  }

}

const stringAddition = (a,b) => {
  
  console.log('stringAddition() '+a+' AND '+b)
  if (!a || !b) throw 'Error in string addition'
  if (typeof(a) !== 'string') a = a.toString()
  if (typeof(b) !== 'string') b = b.toString()
  return (parseInt(a) + parseInt(b)).toString()
}

const stringSubtraction = (a,b) => {
  

  console.log('stringSubtraction() '+a+' AND '+b)
  if (!a || !b) throw 'Error in string substrction'
  if (typeof(a) !== 'string') a = a.toString()
  if (typeof(b) !== 'string') b = b.toString()
  return (parseInt(a) - parseInt(b)).toString()
}

// export const stringMultiplication = (a, b) => {
  
//   try {

//   if (typeof(a) !== 'string') a = a.toString()
//   if (typeof(b) !== 'string') b = b.toString()

//   console.log('stringMultiplication() '+a+' AND '+b)
  
//   if (a.length < 5 && b.length < 5) {
//     console.log( (parseInt(a) * parseInt(b)).toString())  
//     return (parseInt(a) * parseInt(b)).toString();
//   }

//   a = a.split('').reverse();
//   b = b.split('').reverse();
//   var result = [];

//   for (var i = 0; a[i] >= 0; i++) {
//       for (var j = 0; b[j] >= 0; j++) {
//           if (!result[i + j]) {
//               result[i + j] = 0;
//           }

//           result[i + j] += a[i] * b[j];
//       }
//   }

//   for (i = 0; result[i] >= 0; i++) {
//       if (result[i] >= 10) {
//           if (!result[i + 1]) {
//               result[i + 1] = 0;
//           }

//           result[i + 1] += parseInt(result[i] / 10);
//           result[i] %= 10;
//       }
//   }

//   result.reverse();
//   for (i = 0; i < result.length; i++){
//     if (result[i] === 0){
//        result.splice(i--, 1);
//     }else{
//       i = result.length * 2;
//     }
//   }
//   console.log('result.join',result.join(''))
//   return result.join('');
//   } catch(error) {
//     throw error
//   }

// }

// https://leetcode.com/problems/reverse-string/
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
export const reverseString = (s) => {

  let leftIndex = 0
  while (leftIndex < Math.floor( (s.length) / 2) ) {
    let rightIndex = s.length - 1 - leftIndex
    let right = s[rightIndex]
    let left = s[leftIndex]

    s[leftIndex] = right
    s[rightIndex] = left
    leftIndex++
  }

  return s

};