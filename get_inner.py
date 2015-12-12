def get_inner(the_list):
    """Uses recursion to print the elements of inner lists"""
    for item in the_list:
         if isinstance(item, list):
             get_inner(item)    # recursion!!!
         else:
             print item
