# Open a filename passed as the first argument to the script
filename = ARGV.first

# txt is a handle to the open file
txt = open(filename)

# Print the contents of the file
puts "Here's your file {#filename}"
print txt.read
txt.close

# Change input to stdin and ask for another file
print "Type the filename again: "
file_again = $stdin.gets.chomp

# Open the file passed to stdin
txt_again = open(file_again)
print txt_again.read
txt_again.close
