def palindrome(s):
    '''функция сравнивает оригинальную и перевёрнутую строки.
    если они одинаковы, то возвращает True, иначе - False'''
    if s == s[::-1]:
        return True
    return False