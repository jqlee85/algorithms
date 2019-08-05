import {sortArray,merge,multiply, reverseString} from './example'

describe('sortArray()', () => {

  it('Correctly sorts input array', () => {

    const input = [5,1,1,2,0,0]
    const expectedOutput = [0,0,1,1,2,5]

    expect(
      sortArray(input)
    ).toEqual(
      expectedOutput
    )

  })

})

describe('merge()', () => {

  it('Correctly merges 2 sorted arrays into an array of ascending order', () => {

    let input1 = [1,2,3,0,0,0]
    const m = 3
    const input2 = [2,5,6]
    const n = 3
    const expectedOutput = [1,2,2,3,5,6]

    expect(
      function(){
        merge(input1,m,input2,n)
        return input1
      }()
    ).toEqual(
      [1,2,2,3,5,6]
    )

  })

})

// describe('multiply()', () => {

//   it('Correctly multiplies numbers', () => {

    
//     expect(
//       multiply('1234','5678')
//     ).toEqual(
//       '7006652'
//     )
    
//     // expect(
//     //   multiply('848925','248742')
//     // ).toEqual(
//     //   '211163302350'
//     // )


//     let num1 = '3141592653589793238462643383279502884197169399375105820974944592'
//     let num2 = '2718281828459045235360287471352662497757247093699959574966967627'
//     let expected = '8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184'

//     // console.log('Answer:',multiply(num1,num2))
//     expect(
//       multiply(num1,num2)
//     ).toEqual(
//       expected
//     )

//   })

// })

// describe('stringMultiplication()', () => {

//   it('Correctly multiplies numbers', () => {

    
//     expect(
//       stringMultiplication('1234','5678')
//     ).toEqual(
//       '7006652'
//     )



//     let num1 = '3141592653589793238462643383279502884197169399375105820974944592'
//     let num2 = '2718281828459045235360287471352662497757247093699959574966967627'
//     let expected = '8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184'

//     // console.log('Answer:',multiply(num1,num2))
//     expect(
//       stringMultiplication(num1,num2)
//     ).toEqual(
//       expected
//     )

//   })

// })


describe('reverseString()', () => {

  let startArray = ['o','y','e','c','o','m','o','v','a','s']
  let finalArray = ['s','a','v','o','m','o','c','e','y','o']

  it('Correctly reverses string in place', () => {

    expect(
      (()=>{
        reverseString(startArray)
        return startArray
      })()
    ).toEqual(
      finalArray
    )

  })

})