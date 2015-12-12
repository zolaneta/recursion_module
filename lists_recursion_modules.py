# Getting elements out of inner lists

movies = ["Holly Wolly",1975, "Gone Wind", 1287,["Hello Wello", "Miau",["Lolly Molly", "Hello Gwacamolly"]]]

for item in movies:
    if isinstance(item, list):
        for nested_item in item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    if isinstance(deeper_item, list):
                        print deeper_item
                    else:
                        print deeper_item    
            else:
                print nested_item        
    else:
        print item

print "Recursion is a better way to do it!!!"
print

# use function, recursion and module 

import get_inner as gi

gi.get_inner(movies)
