# 
def is_palindrome(s):
    """Assumes s is a str. Returns True if letters in s form a palindrome;
       False otherwise. Non-letters and capitaization are ignored."""
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    
    return is_pal(to_chars(s))


def is_palindrome_viz(s):
    """Assumes s is a str. Returns True if is a palindrome; False otherwise.
       Punctuation makrs, blanks, and capitlization are ignored."""
       
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        print(' is_pal called with', s)
        if len(s) <= 1:
            print('   About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print('   About to return', answer, 'for', s)
            return answer
    
    return is_pal(to_chars(s))

def test_is_palindrome_viz():
    print('Try dogGod')
    #print(is_palindrome_viz('dogGod'))
    print(is_palindrome_viz('radar'))
    print('Try doGood')
    print(is_palindrome_viz('doGood'))