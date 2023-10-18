var linearsearch= (list,element)=>{
    for(i=0;i<list.length;i++){
        if(list[i]==element){
            return i;
        }

    }
    return -1;
}

console.log(linearsearch([15,18,20,19],20))