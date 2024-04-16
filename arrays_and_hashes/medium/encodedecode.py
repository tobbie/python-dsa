class EncodeDecode:
    """
    @param: strs list of strings
    @return: encode a list of strings to a single string
    """

    def encode(self, strs: list):
        encoded =""
        for word in strs:
           encoded += str(len(word)) + "#" + word
        
        return encoded
    
    def decode(self, input_string: str):
        result, index = [], 0
        
        while index < len(input_string):
            step = index
           
            while input_string[step] != "#":
                step += 1
            
            length = int(input_string[index : step])
            start, end = step +1, step + 1 + length
            result.append(input_string[start : end])
            index = end
        
        return result
        
            







sol = EncodeDecode()
print(sol.encode(["neet","coder", "is", "coding?again"]))