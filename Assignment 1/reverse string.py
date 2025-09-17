s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: "olleh"

s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: "olleh"

s = "hello"
reversed_s = ''
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)  # Output: "olleh"
