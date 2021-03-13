"""You are given a dictionary where the keys are strings and the values are strings or dictionaries.
The goal is flatten the dictionary, but save the structures in the keys. The result should be the a dictionary without
the nested dictionaries. The keys should contain paths that contain the parent keys from the original dictionary.
The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty
string (""). Let's look at an example:"""


d = {
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

res = []
def f(x):

    print('x.items():', x.items())
    for item in x.items():
        if isinstance(item[1], dict):
            f(item[1])
        else:
            res.append(item[1]) if item[1] else res.append('')
    return res

print(f(d))