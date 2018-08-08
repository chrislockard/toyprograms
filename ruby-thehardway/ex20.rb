# assign the first ARGV argument to input_file
input_file = ARGV.first

# define a function to print all contents of a file, f
def print_all(f)
  puts f.read
end

# define a function to move to the 0th-byte position of a file, f
def rewind(f)
  f.seek(0)
end

# define a function to print an indicated line from a file passed as args
def print_a_line(line_count, f)
  puts "#{line_count}, #{f.gets.chomp}"
end

# open the file specified by the first argument to the script
current_file = open(input_file)

# Print the contents of the file by calling "print_all"
puts "First let's print the whole file:\n"
print_all(current_file)

# Rewind to the beginning of the file by seeking to the 0th position
puts "Now let's rewind, kind of like a tape."
rewind(current_file)

# Create a counter and print the line from the file corresponding to the 
# counter's current position, then increment the counter by one and print
# that line, three times.
puts "Let's print three lines:"

current_line= 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
