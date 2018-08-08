def while_num(num, inc)
i = 0
numbers = []
  while i < num
    puts "At the top i is #{i}"
    numbers.push(i)

    i += inc
    puts "Numbers now: ", numbers
    puts "At the bottom i is #{i}"
  end
  puts "The numbers: "
  numbers.each {|num| puts num}
end

def for_num(num)
  i = 0
  numbers = []
  (0..num).each {|i| numbers << i}
  numbers.each {|num| puts num}
end

while_num(20, 3)
for_num(20)
