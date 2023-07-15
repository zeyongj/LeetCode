/* Is the character a digit? */
bool dig(char c)
{
    return (c >= '0' && c <= '9');
}

/*
 * Numbers 0-9
 * Exponent - "e"
 * Positive/negative sign - "+"/"-"
 * Decimal point - "."
 */
bool isNumber(char *s) {    /* the string */
    /* Get rid of these cases */
    if (strlen(s) == 0) return 0;
    if (!s) return 0;
    
    /* start parsing from beginning */
    char *sp = s;
    char deci = 0;
    
    /* What can we start with? */
    while (*sp) if (*sp == ' ') sp++; else break;   /* spaces - eat up */
    if (!*sp) return 0;                             /* all spaces => return false */
    if (*sp == '+' || *sp == '-') *sp++;    /* +/- => allowed */
    if (!*sp) return 0;                     /* nothing afterwards => return false */
    if (*sp == '.') { deci = 1; sp++; }     /* '.' allowed for decimal */
    if (!*sp) return 0;                     /* nothing afterwards => return false */
    if (!dig(*sp++)) return 0;              /* not a digit? => return false */
    
    while (*sp) {
        switch(*sp) {
        case ' ':
            sp++;
            while (*sp) if (*sp == ' ') sp++; else break;
            return (*sp == 0);              /* if we reached the end => trailing spaces */
                
        case '.':                           /* can't have two '.' => return false */
            if (deci) return 0;
            else deci = 1;
            break;
                
        case 'e':                           /* parse the e or E case */
        case 'E':
            if (!*(sp + 1)) return 0; else sp++;
            if (*sp == '+'|| *sp == '-') { if (!*(sp + 1)) return 0; else sp++; }
            if (!dig(*sp)) return 0;
            while (*sp) if (dig(*sp)) sp++; else break;
            while (*sp) if (*sp == ' ') sp++; else break;
            return (*sp == 0);
                
        default: 
            if (!dig(*sp)) return 0;
            break;
        }
        sp++;
    }
    return 1;
}