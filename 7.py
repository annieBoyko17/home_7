def winter(snowflake):
    i=0
    while True:
        print("Let`s count some snowflakes")
        yield snowflake+i
        i+=1
res = winter(10)
print(res)
for _ in res:
    print(_)