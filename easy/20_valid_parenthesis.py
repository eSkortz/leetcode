def check(symbols: dict) -> int:
    if len(symbols['(']) != len(symbols[')']) \
        or len(symbols['[']) != len(symbols[']']) \
        or len(symbols['{']) != len(symbols['}']):
        return 0
    return 1


def forming_symbols_dict(string: str) -> dict:
    symbols = {
        '(' : [],
        ')' : [],
        '[' : [],
        ']' : [],
        '{' : [],
        '}' : []
    }
    for i in range(len(string)):
        symbols[string[i]].append(i)
    return symbols


def symbol_processing(s: str, symbols: dict, open_symbol: str, close_symbol: str) -> int:
    while symbols[open_symbol] != []:
        counter_valid = 0
        for j in range(len(symbols[close_symbol])):
            open_id = symbols[open_symbol][0]
            close_id = symbols[close_symbol][j]
            if open_id < close_id:
                symbols1 = forming_symbols_dict(s[0:open_id] + s[close_id+1:len(s)])
                symbols2 = forming_symbols_dict(s[open_id+1:close_id])
                if check(symbols1) == 1 and check(symbols2) == 1:
                    symbols[open_symbol].remove(open_id)
                    symbols[close_symbol].remove(close_id)
                    counter_valid = 1
                    break
        if counter_valid == 0:
            return 0
    return 1


class Solution:
    def isValid(self, s: str) -> bool:
        all_symbols = forming_symbols_dict(s)

        if check(all_symbols) == 0:
            return False
        
        is_valid_1 = symbol_processing(s, all_symbols, '(', ')')
        is_valid_2 = symbol_processing(s, all_symbols, '[', ']')
        is_valid_3 = symbol_processing(s, all_symbols, '{', '}')

        if is_valid_1 == 1 and is_valid_2 == 1 and is_valid_3 == 1:
            return True
        return False
    
    
# time limit on 90/95 tests, but solution is correct