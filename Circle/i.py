from collections import namedtuple

rectangle = namedtuple('rectangle', 'length width')
r = rectangle(length = 1, width = 2)

print(r)
print(r.length)
print(r.width)
print(r._fields)

d = dict(
    {
        'name' : 'Sasha',
        'surname' : 'T`sepaev'
    }
)
print(d['name'])
print(d.values())
print(d.items())
d.update({
    'age' : 18
})
print(d)

#Счетчик
from collections import Counter
shirts_colors = ["red", "white", "blue", "white", "white", "black", "black"]
c = Counter(shirts_colors)
print(c)

c["blue"] += 1
print((f"After shopping: {c}"))

#Срез
a = "Уложи в мою коробку 5 картин"

start, stop = 8, 21

b = a[start:stop]
c = a[start:]
d = a[:stop]
e = a[]

print(b, "\n",
      c, "\n",
      d, "\n",
      e, "\n"
      )





