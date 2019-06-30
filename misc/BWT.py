def alphabet(s):
    """count which characters appear in a string, and in how many copies. Store counters in a dictionary"""
    alph = dict()
    for char in s:
        if char not in alph:
            alph[char] = 1
        else: alph[char] += 1
    return alph


def fm_index(s, alph_char):
    """build the FM-index of a string with respect to a single character. Return a list with the length
    of the string passed as argument, where each position represents the fm index of that position of the string
    (i.e. how many times the character passed as argument occurred up to that position)"""

    fm = [0 for i in range(len(s))]
    fm[0] = 1 if s[0] == alph_char else 0  # construct that looks like an iif (?)

    for i in range(1, len(s)):
        if s[i] == alph_char:
            fm[i] = fm[i-1] + 1
        else:
            fm[i] = fm[i-1]
    return fm


def map_interval(fm_indices):
    """given a dictionary containing the fm indices of all characters, for each letter in the alphabet,
    calculate the position of the suffix array in which suffixes beginning with that character start occurring"""
    map = dict()
    counter = 0

    for ch in sorted(fm_indices.keys()):  # letters of the alphabet are sorted lexicographically
        fm = fm_indices[ch]
        map[ch] = counter
        counter += fm[len(fm)-1]  # the next letter will start occurring in the SA after all the suffixes
        # starting with the previous letter. Thus, increment by the last position of the FM index of the
        # current character

    return map


def bwt_decode(s):

    # build fm index for each character
    FM = dict()
    for ch in alphabet(s).keys():
        FM[ch] = fm_index(s, ch)

    # for each character, determine the intervals where suffixes start with those characters
    interval = map_interval(FM)
    sol = str()

    i = 0
    sol = s[0] + sol  # prepend i-th character of BWT to solution

    while len(sol) < len(s):

        # update i. The first term of the sum is the n-th occurrence of the character; the second is the interval
        # of suffixes starting with that character
        # the -1 is just because indices start from 0 in Python and from 1 when we treat the problem of BWT on paper
        i = FM[s[i]][i] + interval[s[i]] - 1

        # prepend i-th character of BWT to solution
        sol = s[i] + sol

    return sol


if __name__ == "__main__":
    dummy = "attp$aa"
    print(bwt_decode(dummy))
