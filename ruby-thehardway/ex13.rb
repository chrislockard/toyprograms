first, second, third = ARGV
puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

puts "Change that last one... Enter a new item:"
# I learned a very important, and odd, lesson debugging this
# issue. From stack overflow:
# https://stackoverflow.com/questions/6965885/ruby-readline-fails-if-process-started-with-arguments
fourth = $stdin.gets.chomp
puts "Okay, that's better. Now the third variable is: #{fourth}"
