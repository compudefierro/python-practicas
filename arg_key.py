# Function keywords arguments
"""
4.8.3.5. Recap
The use case will determine which parameters to use in the function definition:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

As guidance:

Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names
have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some
positional parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or
you want to prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.
"""


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print("Arg:", arg)
    print("-" * 40)
    for kw in keywords:
        print("keyworkds: ",kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print((lambda x: x + 2)(5))


