const productSum = (array) => {
// Write your code here.
    return sumArray(array,1)
}

const sumArray = (arr,level) => {
    let sum = 0
    arr.forEach((item,i)=>{
        if ( Array.isArray(item) ) sum += level * sumArray( item, level+1 )
        else sum += level * item
    })
    return sum
}

// Do not edit the line below.
exports.productSum = productSum
