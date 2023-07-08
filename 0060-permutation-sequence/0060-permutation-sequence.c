char* getPermutation(int n, int k)
{
    //               1  2  3  4   5    6    7     8      9
    int fact[] = {0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };
    char *ch = malloc(sizeof(char) * (n + 1));
    int i, j, num; // account for the first permutation
    int v;

    /* Trust but verify */
    if (!ch)
        return NULL;

    /* Create the array */
    for (i = 0; i < n; ++i)
        ch[i] = '1' + i;
    ch[i] = 0; // NULL terminate

    /* Loop the required number of iterations are done */
    for (num = k - 1; num; num -= (fact[j] * v))
    {
        char ct;

        /* Find the largest number whose factorial is less than num */
        for(j = 9; fact[j] > num; --j);

        /* The below two step transformation is equal to (j! * v)
           iterations of calculating next permutation:
           1. All the elements from offset "(n - 1) - j" to "(n - 1) - j + v - 1"
              will shift by one to the right.
           2. And the value at offset "(n - 1) - j" would be replaced with the
              character from "(n - 1) - j + v"
        */
        v = num / fact[j];
        ct = ch[(n - 1) - j + v];
        for (i = (n - 1) - j + v; i > (n - 1) - j; --i)
            ch[i] = ch[i - 1];
        ch[i] = ct;
    }

    /* Return the permutation */
    return ch;
}