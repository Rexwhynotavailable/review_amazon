data = []
count = 1
with open("reviews.txt","r") as text:
    for review in text:
        data.append(review)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print(len(data))
print(data[0])
