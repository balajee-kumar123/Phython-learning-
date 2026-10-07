# p = [987,743,32,545,65,23,56,5,-87374,6,76,34,876,-7644,76]
# large = p[1]
# index = 0

# for i in range(0,len(p)):
#     if p[i] > large:
#         large = p[i]
#         index = i
    
# print(large,index)

#CONFUSION SET
# s1 = {10,20,30,40,50}
# s2 = {30,50,20,40,10}

# s1 ^= s2
# s2 ^= s1
# print(s1)
# print(s2)

#DICTONARY

# D = {10:100,20:200,30:300,40:400,50:500}
# E = {6:60,7:70,8:80}

# for i in D:
#     E[i] = D[i]
#     print(E[i])
    
# print(E)

#question
# d = {"a":30,"b":70,"c":48,"d":90}
# sum = 0

# for i in d:
#     sum += d[i]
# print(sum)    

# l = [233,4,3,34,45,53,4354,54,5,4,44,54,4,4545,454,4,4,5,64,54,645,5,4,4,644,46,5,4,4,444,654,45,5,54,4]
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

d = {"a":30,"b":70,"c":49,"d":95}
e = {"b":30,"a":70,"e":48,"f":90}

for i in e:
    if i in d.keys():
        d[i] += e[i]
    else:
        d[i] = e[i]
print(d)        

