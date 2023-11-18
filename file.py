# Create a text file with a size of 1MB filled with the word "walt.id"

file_size_mb = 1
text_to_repeat = "walt.id"


num_repeats = (file_size_mb * 1024 * 1024) // len(text_to_repeat)


content = text_to_repeat * num_repeats

# Write the content to the file
with open("1MB.txt", "w") as file:
    file.write(content)

print("File created successfully.")
