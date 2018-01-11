data = open('./unicode_2350.txt')
u_list = data.read().split('\n')
data2 = open('hangeul_2350.txt')
h_list = data2.read().split('\n')

dict = {}

for i, uni in enumerate(h_list):
	dict[uni] = u_list[i]

my_200 = open('my_200.txt')
lst = my_200.read().split('\n')

f = open('my_unicode_200.txt', 'w')
for h in lst:
    f.write(dict[h] + "\n")
f.close()