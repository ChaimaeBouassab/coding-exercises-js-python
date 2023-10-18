var binarysearch= (array,element)=>{
    let left = 0;
    let right = array.length -1 ;
    while(left<=right){
        let mid=Math.floor((left+right)/2);
        if(array[mid]==element){
            return mid;
        }
        else if(array[mid]<element){
            left=mid+1;
        }
        else if(array[mid]>element){
            right=mid-1;
        }
    }
    return -1
}

console.log(binarysearch([15,18,19,20],18))