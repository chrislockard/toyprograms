the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first loop goes through a list in a traditional manner
# found in other programming languages
# for number in the_count
#   puts "This is count #{number}"
# end
# Apparently, this is bad Ruby style and rubyists will shun
# me as a bad coder for using it, I better change it to the
# "preferred" method
the_count.each do |count|
  puts "This is count #{count}"
end
# This loop achieves the same, but in the preferred Ruby way
fruits.each do |fruit|
  puts "A fruit of type: #{fruit}"
end

# Here's how to go through mixed lists in another new style
change.each {|i| puts "I got #{i}"}

# Here's how to build a list, starting with an empty array
elements = []

# Now add to it
(0..5).each do |i|
  puts "Adding #{i} to the list"
  # Push the "i" variable to the end of the list
  elements.push(i)
end

# Now this array can be printed as well
elements.each {|i| puts "Element was: #{i}"}

# This is my array implemented poorly
heart_rate = []
[120, 100, 90, 77].each do |i|
  puts "Adding heart rate #{i} from previous flights."
  heart_rate << i
end
heart_rate.each {|i| puts "Heart rate: #{i}"}
# Now clear the array
puts "What was that last one, again?"
puts heart_rate.last
puts "And what about some one of the middle ones?"
puts heart_rate[1..2]
