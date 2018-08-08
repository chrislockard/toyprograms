# Omitting "return" works because Ruby implicitly returns the last calculation
def add(a, b)
  puts "ADDING #{a} + #{b}"
  return a + b
end

def sub(a, b)
  puts "SUBTRACTING #{a} - #{b}"
  return a - b
end

def mult(a, b)
  puts "MULTIPLYING #{a} * #{b}"
  return a * b
end

def div(a, b)
  puts "DIVIDING #{a} / #{b}"
  return a / b
end

puts "Let's do some maths with functions!"

age = add(30, 1)
height = sub(74, 2)
weight = mult(90, 2)
iq = div(100, 2)

puts "Age: #{age}\nHeight: #{height}\nWeight: #{weight}\nIQ: #{iq}"

#A puzzle for extra credit
puts "Here is a puzzle."

what = add(age, sub(height, mult(weight, div(iq, 2))))

puts "That becomes: #{what}. Can you do it by hand?"
