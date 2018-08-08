# define function cheese_and_crackers that takes two arguments and prints them in a string
def cheese_and_crackers(cheese_count, boxes_of_crackers)
  puts "You have #{cheese_count} cheeses!"
  puts "You have #{boxes_of_crackers} boxes of crackers!"
  puts "Man, that's enough for a party!"
  puts "Get a blanket.\n"
end

# exercise 19.3 - my own function (but not calling it 10 different ways)
def my_func(foo)
  puts "I love #{foo}!"
  puts "(oh, and bar, and baz!)"
end

# Print a line and call c_n_c with two integer values
puts "We can just give the function numbers directly: "
cheese_and_crackers(20, 30)

# Assign integer values to two variables to pass in to c_n_c function
puts "OR, we can use variables from our script:"
cheese_amount = 10
cracker_amount = 50

cheese_and_crackers(cheese_amount, cracker_amount)

# Call c_n_c with arithmetic on two integers
puts "We can even do math inside function arguments!:"
cheese_and_crackers(10 + 20, 5 + 6)

# Call c_n_c with arithmetic on two variables
puts "And we can combine variables and math!:"
cheese_and_crackers(cheese_amount + 100, cracker_amount + 1000)

# Call my function and pass a string to it
my_func("FOO")
my_func(1024)
my_func(true)
my_func(false)
