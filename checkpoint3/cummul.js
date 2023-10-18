function accum(s) {
    const characters = s.toLowerCase().split('');
    let result = '';

    for (let i = 0; i < characters.length; i++) {
        const repeatedCharacter = characters[i].toUpperCase() + characters[i].repeat(i);
        result += (i !== 0 ? '-' : '') + repeatedCharacter;
    }

    return result;
}

console.log(accum("abcd"));    // Output: "A-Bb-Ccc-Dddd"
console.log(accum("RqaEzty")); // Output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
console.log(accum("cwAt"));    // Output: "C-Ww-Aaa-Tttt"
