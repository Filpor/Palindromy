napis="radar"
def czyPalindrom(napis):
    n=len(napis)
    for i in range (len(napis)//2):
        if napis[i]!=napis[n-i-1]:
            return False
        return True
if czyPalindrom(napis)==True:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")