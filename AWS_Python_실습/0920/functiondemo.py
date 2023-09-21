def calc_sum(start, end): #parameter 매개변수
    sum = 0

    for i in range(start, end+1):
        sum += i
        
    return sum
    #함수의 끝
    
    # print(' %d부터 %d까지의 합은 %d 입니다.'%(start,end, sum))
    
    
start = 50
end = 70

# calc_sum(start, end) #인자, 인수, Argument    
# calc_sum(2, 7989)   #함수의 호출, Call by Name
# calc_sum(45, 8989)
result = calc_sum(start, end)
print("%d부터 %d까지의 합은 %d 입니다."%(start,end,result))

#Call by Name
#Call by Value -> immutable type
#Call by Reference -> mutable type