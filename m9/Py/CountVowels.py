def count_vowels(myStr):
    lowerstr=myStr.lower()
    x=0
    for v in "aeiou":
        x=x+lowerstr.count(v)
    print(x)

count_vowels('Mama mila vElikU ramu')
count_vowels('annnmemmmtlo')
count_vowels('kjjs')

