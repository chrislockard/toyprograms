from_file, to_file = ARGV
File.open(from_file, 'r') do |infile|
  File.open(to_file, 'w') do |outfile|
    while buffer = infile.read(4096)
      outfile << buffer
    end
  end
end
# Commenting out most of the script per Study drill 2
# puts "[*] Copying from #{from_file} to #{to_file}."

# How could these two be done on one line?
# in_file = open(from_file)
# indata = in_file.read

# puts "[*] The input file is #{indata.length} bytes long."

# puts "[*] Does the file exist? #{File.exist?(to_file)}"
# puts "[*] Ready, hit RETURN to continue, CTRL-C to abort."
# $stdin.gets

# out_file = open(to_file, 'w')
# out_file.write(indata)

# puts "[*] Done"

# out_file.close
# in_file.close
