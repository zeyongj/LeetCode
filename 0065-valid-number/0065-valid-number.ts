function isNumber(s: string): boolean {
    let state = Array(10).fill(0);
    const finals = 0b101101000;
    const transfer = [
        [ 0, 1, 6, 2, -1],
        [-1,-1, 6, 2, -1],
        [-1,-1, 3, -1, -1],
        [ 8,-1, 3, -1, 4],
        [-1, 7, 5, -1, -1],
        [ 8,-1, 5, -1, -1],
        [ 8,-1, 6, 3, 4],
        [-1,-1, 5, -1, -1],
        [ 8,-1,-1, -1, -1]
    ];
    let idx = 0;
    for (let c of s) {
        idx = make(c);
        if (idx < 0) return false;
        state[0] = transfer[state[0]][idx];
        if (state[0] < 0) return false;
    }
    return (finals & (1 << state[0])) > 0;
}

function make(c: string): number {
    switch (c) {
        case ' ': return 0;
        case '+':
        case '-': return 1;
        case '.': return 3;
        case 'e':
        case 'E': return 4;
        default: return (c >= '0' && c <= '9') ? 2 : -1;
    }
}
