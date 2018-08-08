# This one is like ARGV
# *args puts all values into args as a list
def print_two(*args)
  arg1, arg2 = args
  puts "arg1: #{arg1}, arg2: #{arg2}"
end

# ok, *args wasn't needed. this will work
def print_two_again(arg1, arg2)
  puts "arg1: #{arg1}, arg2: #{arg2}"
end

# This one takes one argument
def print_one(arg1)
  puts "arg1: #{arg1}"
end

# This function takes no arguments
def print_none()
  puts "I got nothin'"
end

print_two("Chris", "first")
print_two_again("Chris", "again")
print_one("Chris!")
print_none()
