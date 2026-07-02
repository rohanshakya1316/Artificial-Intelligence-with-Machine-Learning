# Write a python program to implement AND, OR, NOT and XOR.

# 1. Implementation using Logical Operators (True/False)
def logical_gates():
    print("--- 1. Logical Gates (Boolean) ---")
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    
    # AND Gate
    print("\nAND Gate:")
    for a, b in inputs:
        print(f"{a} AND {b} = {a and b}")
        
    # OR Gate
    print("\nOR Gate:")
    for a, b in inputs:
        print(f"{a} OR {b} = {a or b}")
        
    # NOT Gate (Takes single input)
    print("\nNOT Gate:")
    print(f"NOT False = {not False}")
    print(f"NOT True  = {not True}")
    
    # XOR Gate (True if inputs are different)
    print("\nXOR Gate:")
    for a, b in inputs:
        print(f"{a} XOR {b} = {a != b}")


# 2. Implementation using Bitwise Operators (1/0)
def bitwise_gates():
    print("\n--- 2. Bitwise Gates (Binary Integers) ---")
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    # Bitwise AND (&)
    print("\nAND Gate (&):")
    for a, b in inputs:
        print(f"{a} & {b} = {a & b}")
        
    # Bitwise OR (|)
    print("\nOR Gate (|):")
    for a, b in inputs:
        print(f"{a} | {b} = {a | b}")
        
    # Bitwise NOT (~) 
    # Note: ~x equals -x-1 in Python due to two's complement. 
    # We use 'int(not x)' to represent a clean 1/0 logic gate flip.
    print("\nNOT Gate:")
    print(f"NOT 0 = {int(not 0)}")
    print(f"NOT 1 = {int(not 1)}")
    
    # Bitwise XOR (^)
    print("\nXOR Gate (^):")
    for a, b in inputs:
        print(f"{a} ^ {b} = {a ^ b}")


# Execute both implementations
if __name__ == "__main__":
    logical_gates()
    bitwise_gates()
