"""Small module for routine tasks"""
decipher_dict = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}

def base2number(base):
    """Takes base nucleotid as string and returns a number"""
    return decipher_dict[base]

def number2base(number):
    return [k for k, v in decipher_dict.items() if v == number][0]