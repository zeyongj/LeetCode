function isNumber(s: string): boolean {
    if(s.toLocaleLowerCase().includes('infinity')) return false;
    const num: number = Number(s);
    return !isNaN(num);
};