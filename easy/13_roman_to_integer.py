def solution(s: str) -> int:
    roman_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    i = 0
    summ = 0
    while i < len(s):
        try:
            s[i+1]
        except IndexError:
            summ += roman_dict[f'{s[i]}'] 
            break
        else:
            if roman_dict[f'{s[i]}'] < roman_dict[f'{s[i+1]}']: 
                summ += (roman_dict[f'{s[i+1]}'] - roman_dict[f'{s[i]}'])
                i += 2
            else:
                summ += roman_dict[f'{s[i]}'] 
                i += 1
    return summ