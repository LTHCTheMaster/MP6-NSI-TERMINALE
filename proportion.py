from math import sqrt

msg = 'BWFWKSAKWFIMWDKWFKDWKHZADGKGHZWKGFLKMHHGKWIMWDSESLAWJWWLSALAFVAXXWJWFLWSMEGMNWEWFLWLSMJWHGKUWIMADQSVWTAWFUWJLSAFUWKLIMWLGMKDWKUGJHKYJSNALWFLDWKMFKKMJDWKSMLJWKUWKLIMWLGMLWKDWKHSJLAUMDWKVWKUGJHKYJSNALWFLDWKMFWKKMJDWKSMLJWKUWKLIMWVSFKUWLMFANWJKLGMLWKLWFLJSFKDSLAGFGMAFFAKMGMWFLJSFKDSLAGFWLAFFAKMSDSXGAKUWLLWKMHHGKALAGFVWKHZADGKGHZWKJWKKWETDWHWMLWLJWSUWDDWVWKYWGEWLJWKIMASVEWLLWFLVWKHGAFLKKSFKSMUMFWVAEWFKAGFVWKDAYFWKKSFKDSJYWMJFAHJGXGFVWMJVWKKMJXSUWKKSFKWHSAKKWMJGMHWMLWLJWHSJDWFLADKVMJWHGKJWDSLAXVMFWESKKWSMFWSMLJWLGMLWKLVSFKMFJWHGKJWDSLAXWFMFNSAKKWSMTSLLMHSJDSLWEHWLWJAWFFQWKLWFMFJWHGKSTKGDMHSKEWEWDWKEGDWUMDWKSYJWYSLANWKFAVMNSAKKWSMFAVWKUGJHKIMADJWFXWJEWKADKFWUGFUGANWFLHSKHDMKVWLWFVSFUWSMJWHGKIMSMEGMNWEWFLVSFKMFUGJHKIMWDUGFIMWUWKLIMSHHSJWEEWFLADKJWYSJVWFLDSESLAWJWUGEEWZGEGYWFWUWKLIMADKXGFLSTKLJSULAGFVWLGMLWKDWKIMSDALWKIMADMAKGFLWKKWFLAWDDWKUWKLIMADKDSUGFKAVWJWFLUGEEWAFSDLWJSTDWVSFKDAFKLSFLHJWKIMWAFVANAKATDWVWDWMJKHWUMDSLAGFUWKLIMADKJSAKGFFWFLVMJWHGKJWDSLAXVMFSYJWYSLSMFSMLJWSYJWYSLUWKLIMADKGMTDAWFLIMWLSFVAKIMADKJSAKGFFWFLVWDAFVAXXWJWFUWVMUGJHKSMEGMNWEWFLGMSMJWHGKDWTDGUVWESJTJWLWFVSKSVAKKGDMLAGFUWKLIMADKSFWSFLAKKWFLHSJDSHWFKWWWLDWEGMNWEWFLYWFWJSDIMASFAEWLGMKDWKUGJHKWLDWMJSULAGFHSJLAUMDAWJWVWKMFKKMJDWKSMLJWKIMADWKVWLJMALLGMKUWKLIMWUWLLWAFVAXXWJWFUWIMGAIMWXSMKKWWFWDDWEWEWESAKEGEWFLSFWWFWJWFVJSHSKDWKDGAKVMEGMNWEWFLWJJGFWWK'

def tri(dic):
    """
    Remet le dictionnaire dic dan l'ordre de la valeur plus grande proportion à la plus petite
    """
    dout = {}
    temp = []
    for i in dic:
        temp.append(dic[i])
    temp.sort(reverse=True)
    for i in temp:
        for j in dic:
            if dic[j] == i:
                dout[j] = i
                break
    return dout

def analyse(msg):
    """
    Donne la fréquence de chaque lettre dans msg
    """
    out = {}
    n = len(msg)
    for i in msg:
        if i not in out:
            out[i] = 1
        else:
            out[i] += 1
    for i in out:
        out[i] = round(out[i] / n * 100, 2)
    temp = tri(out)
    return temp

def nearest(chare, analysed):
    """
    Détermine quelle lettre est associé au E
    """
    char = ''
    dist = 0
    for i in analysed:
        if sqrt(chare**2+analysed[i]**2)>dist:
            dist = sqrt(chare**2+analysed[i]**2)
            char = i
    return char

def scan(msg):
    """
    Fait un scan adapté au message qui en clair sont en français
    """
    analysed = analyse(msg)
    real = {"E": 17.26, "A": 8.40, "S": 8.08, "I": 7.34, "N": 7.13, "T": 7.07, "R": 6.55, "L": 6.01, "U": 5.74, "O": 5.26, "D": 4.18, "C": 3.03, "P": 3.01, "M": 2.96, "V": 1.32, "G": 1.27, "F": 1.12, "B": 1.06, "Q": 0.99, "H": 0.92, "X": 0.45, "J": 0.31, "Y": 0.30, "Z": 0.12, "K": 0.05, "W": 0.04}
    temp = nearest(real["E"],analysed)
    return temp

def decrypt(msg):
    """
    Déchiffre avec un code de césar après avoir récupéré la correspondance du E
    """
    e_cor = scan(msg)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {chr((i+alphabet.find(e_cor))%26+65):chr((i+4)%26+65) for i in range(26)}
    out = ''
    for i in msg:
        if i in d:
            out += d[i]
        else:
            out += i
    return out

print(decrypt(msg))
