sayi="73167176531330624919225119674426574742355349194934"
sayi+="96983520312774506326239578318016984801869478851843"
sayi+="85861560789112949495459501737958331952853208805511"
sayi+="12540698747158523863050715693290963295227443043557"
sayi+="66896648950445244523161731856403098711121722383113"
sayi+="62229893423380308135336276614282806444486645238749"
sayi+="30358907296290491560440772390713810515859307960866"
sayi+="70172427121883998797908792274921901699720888093776"
sayi+="65727333001053367881220235421809751254540594752243"
sayi+="52584907711670556013604839586446706324415722155397"
sayi+="53697817977846174064955149290862569321978468622482"
sayi+="83972241375657056057490261407972968652414535100474"
sayi+="82166370484403199890008895243450658541227588666881"
sayi+="16427171479924442928230863465674813919123162824586"
sayi+="17866458359124566529476545682848912883142607690042"
sayi+="24219022671055626321111109370544217506941658960408"
sayi+="07198403850962455444362981230987879927244284909188"
sayi+="84580156166097919133875499200524063689912560717606"
sayi+="05886116467109405077541002256983155200055935729725"
sayi+="71636269561882670428252483600823257530420752963450"

bitisik=""
bitisikCarpim=1
enBuyuk=0

for i in range(0,1001-13,1):
    bitisik=sayi[i:i+13]
    for rakam in bitisik:
        bitisikCarpim*=int(rakam)
    if(bitisikCarpim>enBuyuk):
        enBuyuk=bitisikCarpim
    bitisikCarpim=1
print(enBuyuk)
