var factoriel=(num)=>{
    if(num ==0) return 1
    return num*factoriel(num-1)
}
console.log(factoriel(7))