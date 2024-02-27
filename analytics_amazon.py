data = []
count = 0
with open("reviews.txt","r") as text:
    for review in text:
        data.append(review)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("讀取完了，總共有", len(data), "筆資料")

sum_len = 0
for b in data:
    sum_len = sum_len + len(b)
print("總平均長度為:", sum_len / len(data) )

new = []
for c in data:
    if len(c) < 100 :
        new.append (c)
print("每筆留言字數小餘100:",len(new))
print(new[0])
print(new[1])
print(new[2])