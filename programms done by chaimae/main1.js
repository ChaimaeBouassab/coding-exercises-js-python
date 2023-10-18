var bubblesort= (array)=>{
    for(i=0;i<array.length -1;i++){
        for(j=0;j<array.length -1-i;j++){
            if(array[j]>array[j+1]){
                let temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
            }
        }
    }
    return array

}

console.log(bubblesort([15,18,20,19]))