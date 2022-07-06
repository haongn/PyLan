def clip(text: str, max_len: 'int > 0' = 80) -> str: 
    """Return text clipped at the last space before or after max_len."""
    end = None 
    if len(text) > max_len: 
        space_before = text.rfind(' ', 0, max_len)  # return the index of the space before max_len
        if space_before >= 0:                       # if any space is found 
            end = space_before                      # assign the index of the space
        else: 
            space_after = text.rfind(' ', max_len)  # there is no end index specified 
            if space_after >= 0: 
                end = space_after
    if end is None:                                 # no spaces were found 
        end = len(text)
    
    return text[:end].rstrip()    # return a copy with the trailing character removed. 


if __name__ == '__main__':
    print(clip.__annotations__)   # return dict: extract function annotations
    for name, type in clip.__annotations__.items(): 
        print(name, ':', type)