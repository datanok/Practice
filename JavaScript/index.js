// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

// function flattenObj(obj,parent=""){
//     let result = {}
//     for(key in obj){
//         const newKey = parent ? parent +"_" + key : key //a
//         console.log(newKey,"newKey")
//         const val = obj[key] // 1
//         if(typeof val === "object" && !Array.isArray(val)){
//             // console.log(val,"val")
//             Object.assign(result,flattenObj(val,newKey))
//         }else{
//             result[newKey] = val //{a:1}
//             // console.log(result,"result")
//         }
//     }
//     return result
// }
function objToArr(obj,parent=""){
    let result = []
    for( key in  obj){
        const newKey = parent? `${parent}.${key}`: key
        const val = obj[key]
         if(typeof val === 'object' && !Array.isArray(val)){
            result.push(...objToArr(val,newKey))
        }
        else{
            console.log(newKey,val)
            result.push(`${newKey},${val}`)
        }
    }
    return result
    
   }

function findDeepestKey(obj,parent="",currentHeight = 0,result ={maxKey:'',maxHeight:-1}){
    for( key in  obj){
        const newKey = parent? `${parent}.${key}`: key
        const val = obj[key]
         if(typeof val === 'object' && !Array.isArray(val)){
            Object.assign(result,findDeepestKey(val,newKey,currentHeight+1,result))
        }else{
            if(currentHeight>=result.maxHeight){
                result.maxHeight = currentHeight
                result.maxKey = newKey
            }
        }
    }
    return result.maxKey
}


const input2 = {
  user: {
    name: 'Alice',
    location: {
      city: 'Paris',
      zip: 75000
    }
  },
  active: true
};
const test = { a: 1, b: { c: 2, d: { e: 3 } } };
const data = {
  user: {
    name: 'Alice',
    address: {
      city: {
        name: 'Paris',
        meta: {
          region: 'Europe'
        }
      }
    }
  }
};

console.log(findDeepestKey(data))
// console.log(flattenObj(test))
// console.log(objToArr(input2))