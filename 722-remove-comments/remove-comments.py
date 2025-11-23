class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        is_block_comment = False  
        cleaned_code = []  
        current_line = []     
        for code_line in source:
            char_index = 0
            if not is_block_comment:
                current_line = []       
            while char_index < len(code_line):
                if not is_block_comment and char_index + 1 < len(code_line) and code_line[char_index:char_index+2] == "//":
                    break         
                elif not is_block_comment and char_index + 1 < len(code_line) and code_line[char_index:char_index+2] == "/*":
                    is_block_comment = True  
                    char_index += 1    
                elif is_block_comment and char_index + 1 < len(code_line) and code_line[char_index:char_index+2] == "*/":
                    is_block_comment = False 
                    char_index += 1               
                elif not is_block_comment:
                    current_line.append(code_line[char_index])            
                char_index += 1          
            if current_line and not is_block_comment:
                cleaned_code.append("".join(current_line))      
        return cleaned_code


                    





        