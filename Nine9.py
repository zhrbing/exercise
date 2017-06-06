# -*- coding:utf-8 -*-
# __author__ = 'zhbing'
# for i in range(9):
#     for j in range(9):
#         if (i + 1 >= j + 1):
#             print(str(i + 1) + "*" + str(j + 1) + "=" + str((i + 1) * (j + 1)), end="\t")
#     print()


l=[str(x+1)+"*"+str(y+1)+"="+str((x+1)*(y+1)) for x in range(9) for y in range(9) if (x + 1 >= y + 1)]
for lk,lv in enumerate(l):
    print(lv,end='\t')
    if(lk in [0,2,5,9,14,20,27,35]):
        print()