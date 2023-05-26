"""
Separate out valid and invalid dictionary?
1. {"first message": "hello world"}  # valid
2. dict("message"="hello")  # invalid
3. {"": 123}  # Valid
4. dict(value=4) # Valid
5. {1: "Hello", 2: "World"}  # Valid
6. {1.2: "Hello", 2.1: "World"}  # Valid
7. {[1, 2, 3]: "Hello"}  # Invalid
8. {([1, 2,], 1): "World"}  # Invalid

"""