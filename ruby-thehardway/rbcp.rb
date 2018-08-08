from_file, to_file = ARGV
File.open(from_file, 'r') do |infile|
  File.open(to_file, 'w') do |outfile|
    while buffer = infile.read(4096)
      outfile << buffer
    end
  end
end
