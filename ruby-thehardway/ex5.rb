name = 'Chris Lockard'
age = 31.0 # In 2015 (early, 2015)
height = 72.0 # Inches
weight = 180.0 # lbs
eyes = 'multi-colored'
teeth = 'White'
hair = 'Brown'
centis = height * 2.54
kgs = weight * 0.453592

puts "Let's talk about #{name}."
puts "He's #{height} inches tall."
puts "He's #{weight} pounds heavy."
puts "Actually, that's not too heavy."
puts "He's got #{eyes} eyes and #{hair} hair."
puts "His teeth are usually #{teeth} depending on coffee intake."
puts "In a metric world, #{name} is #{centis} centimeters tall, and #{kgs} kilograms heavy."
#Tricky line
puts "If I add #{age}, #{height}, and #{weight} I get #{age + height + weight}."
