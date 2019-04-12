"""dictionaries for tesing"""

engnums = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 6 : 'six', 0 : 'nul'}
ukrnums = {1 : 'odyn', 2 : 'dva', 5 : 'piat', 7 : 'sim', 8 : 'visim', 0 : 'nul'}

def combine_dicts(d1, d2):
    
    """returns a combined dictionary from two input dictionaries"""
    
    combined = dict()
    
    for d in d2:
    
        if d not in d1:
            combined[d] = d2[d]
            
        elif d1[d] == d2[d]:
            combined[d] = d2[d]
            
        else:
            combined[d] = d1[d], d2[d]
            
    for d in d1:
    
        if d not in d2:
            combined[d] = d1[d]
            
    return combined
