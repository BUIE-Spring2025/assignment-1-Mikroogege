def int_to_roman(num):
    value=""
    listone=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    listtwo=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    listone.reverse()
    listtwo.reverse()
    for i in range(13):
        current=num//listone[i]
        value+=listtwo[i]*current
        num=num%listone[i]
    print(value)