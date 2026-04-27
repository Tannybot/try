import ast


def display_ast(title, code):
    print("=" * 60)
    print(f"Example: {title}")
    print("=" * 60)

    tree = ast.parse(code)

    print("Source Code:")
    print(code.strip())

    print("\nAST Structure:")
    print(ast.dump(tree, indent=4))

    print("\n")


examples = {
    "1. For Loop": """
for i in range(5):
    print(i)
""",

    "2. Generator Function": """
def generate_numbers():
    for i in range(5):
        yield i
""",

    "3. Complex Conditional Statement": """
x = 15

if x > 10 and x < 20:
    print("Between 10 and 20")
elif x == 10:
    print("Equal to 10")
else:
    print("Other number")
""",

    "4. Complex Arithmetic Operation": """
a = 10
b = 5
c = 2
d = 8
e = 4

result = (a + b) * c - d / e ** 2
"""
}


for title, code in examples.items():
    display_ast(title, code)