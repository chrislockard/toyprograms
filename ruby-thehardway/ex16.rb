filename = ARGV.first

file = open(filename)
puts "#{filename} was last accessed at #{file.atime}"
file.close
puts "Erasing #{filename}"
puts "If you don't want to do this, press CTRL-C (^C)"
puts "If you do want to do this, press ENTER"

$stdin.gets

puts "Opening the file..."
target = open(filename, 'w')

puts "Truncating the file. Goodbye!"
target.truncate(0)

puts "Now I'll ask for three lines."

print "Line 1:"
line1 = $stdin.gets.chomp
print "Line 2:"
line2 = $stdin.gets.chomp
print "Line 3:"
line3 = $stdin.gets.chomp

puts "Writing to #{filename}"

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

puts "Closing #{filename}"
target.close
