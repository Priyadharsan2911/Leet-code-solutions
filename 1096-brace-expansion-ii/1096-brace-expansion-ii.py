class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stacks for operators and operands (sets of words)
        ops = []
        stack = []
        
        def evaluate():
            """Pop the top operator and perform union or concatenation."""
            op = ops.pop()
            right = stack.pop()
            left = stack.pop()
            if op == ',':
                stack.append(left | right)
            elif op == '*':
                stack.append({a + b for a in left for b in right})

        i = 0
        n = len(expression)
        
        while i < n:
            char = expression[i]
            
            if char == '{':
                # Insert implicit concatenation operator if preceding token is an operand or closing brace
                if i > 0 and (expression[i - 1].isalpha() or expression[i - 1] == '}'):
                    while ops and ops[-1] == '*':
                        evaluate()
                    ops.append('*')
                ops.append('{')
                i += 1
                
            elif char == '}':
                # Process operators until matching '{'
                while ops and ops[-1] != '{':
                    evaluate()
                ops.pop()  # Pop '{'
                i += 1
                
            elif char == ',':
                # Process pending concatenations before union
                while ops and ops[-1] != '{':
                    evaluate()
                ops.append(',')
                i += 1
                
            elif char.isalpha():
                # Read full string literal (usually single char per grammar)
                start = i
                while i < n and expression[i].isalpha():
                    i += 1
                word = expression[start:i]
                
                # Check for implicit concatenation before pushing literal
                if start > 0 and (expression[start - 1].isalpha() or expression[start - 1] == '}'):
                    while ops and ops[-1] == '*':
                        evaluate()
                    ops.append('*')
                    
                stack.append({word})

        # Process any remaining operations
        while ops:
            evaluate()

        return sorted(list(stack[0]))