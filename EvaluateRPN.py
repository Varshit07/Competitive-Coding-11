# TC: O(n) where n is the number of tokens
# SC: O(n) for stack
# LeetCode: Y(https://leetcode.com/problems/evaluate-reverse-polish-notation/)
# Approach: Use a stack to push the operands. 
#           When an operation needs to be formed then pop two operands from the stack and push the result as an operand on the stack
#           The idea behind using a stack to solve this problem is to get the most recent operands for an operation

class Solution:
    # helper function to perform operation on the operands
    def perform_operation(self, op1, op2, operator):
        
        # perform addition
        if operator == "+":
            return (op1 + op2)

        # perform subtraction
        elif operator == "-":
            return (op1 - op2)

        # perform multiplication
        elif operator == "*":
            return (op1 * op2)

        # perform division truncating towards zero
        else:
            return (int(op1 / op2))

    def evalRPN(self, tokens: List[str]) -> int:
        
        # intialize stack
        st = []
        
        for token in tokens:
            
            # if the current token is an operator then perform operation
            if token in ["+", "-", "*", "/"]:
                # Pop operand 2
                op2 = st.pop()
                
                # Pop operand 1
                op1 = st.pop()
                
                # push the result of operation on the stack
                st.append(self.perform_operation(op1, op2, token))
                    
            # if the current token is an operand then push the operand on the stack      
            else:
                st.append(int(token))
                
        # after all the tokens are processed then return the result and empty the stack           
        return st.pop()
        
