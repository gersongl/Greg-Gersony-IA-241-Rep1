#lab6

#3.1

for i in range(6):
    if i != 3:
        print(i)

#3.2

result = 1

for i in range (1,6):
    result = result * i
    
print(result)

#3.3

sum_of = 0

for i in range(1,6):
    sum_of = sum_of + i

print(sum_of)

#3.4

product = 3

for i in range(4,9):
    product = product * i
    
print("The product is " + str(product) + " this time.")

#3.5

outcome = 1

for i in range(4,9):
    outcome = outcome * i

print("The outcome is " + str(outcome) + " in this case.")

#3.6

value = 0
for word in 'this is my 6th string'.split():
    value += 1

print("The answer is " + str(value) + " words.")

#3.7_optional

my_tweet = {
            "favorite_count":1138,
            "lang": "en",
            "coordinates": (-75, 40),
            "entities": {'hashtags': ["Preds", "Pens", "SingIntoSpring"]}
            }

ending = 0

for hashtag in my_tweet['entities']['hashtags']:
    ending += 1

print("There are " + str(ending) + " hashtags in this tweet.")
