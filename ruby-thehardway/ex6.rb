types_of_people = 10
x = "There are #{types_of_people} types of people."
binary = "binary"
do_not = "don't"
# String inside a string
y = "Those who know #{binary} and those who #{do_not}."

puts x
puts y

# String inside a string
puts "I said: #{x}."
# String inside a string - this works also; string interpolation
puts "I also said: '#{y}'."

hilarious = false
joke_evaluation = "Isn't that joke funny?! #{hilarious}"

puts joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

# String concatenation
puts w + e
