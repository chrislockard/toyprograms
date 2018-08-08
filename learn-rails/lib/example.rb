class Example < Object

  # This is a comment.

  # Attributes are values for classes that we can "set" and "get". Attributes allow for 
  # pushing data into an object and pulling it out later. Attributes are just specialized
  # methods that expose data outside of the object.
  attr_accessor :honorific
  attr_accessor :name
  attr_accessor :date

  def initialize(name, date)
    @name = name # @ prior to variable name makes it an instance variable, 
                 # available to any method in the instance of this class
    @date = date.nil? ? Date.today : date #ternary operator
  end

  def backwards_name
    @name.reverse
  end

  def to_s
    @name
  end

  def titled_name
    @honorific ||= 'Esteemed' # Double-bar equals - conditional assignment. Equivalent to
                              # if not @honorific
                              #   @honorific = 'Esteemed'
                              # end
    titled_name = "#{@honorific} #{@name}" # String interpolation using double quotes and #{}
  end

  def december_birthdays
    # An array, which can contain any mix of objects (if an array contains an array, it's 'nested')
    born_in_december = [ ]
    # A block, or unnamed method. name and date are only available through this method
    # Any variable in the method is available within the block (here, the instance variable name 
    # comes from @name defined earlier)
    famous_birthdays.each do |name, date|
      if date.month == 12
        born_in_december << name
      end
    end
    born_in_december
  end

  # Access Control
  # Any methods in a private section are only available by other methods of the same class.
  private

  def famous_birthdays
    # Birthdays is a hash or a key->value mapping (aka dictionary, map, or associative array)
    # The '=>' or "hashrocket" operator associates a key and value pair in a hash.
    # Modern ruby (newer than 1.9) allows the use of symbols to associate key->value pairs thusly,
    # birthdays = {
    #   beethoven: Date.new(1770, 12, 16),
    #   brubeck: Date.new(1920, 12, 6),
    #   holly: Date.new(1936, 9, 7),
    #   richards: Date.new(1943, 12, 18)
    # }
    # Alternately, a string containig spaces can be transformed into a hash, thusly
    # birthdays = {
    #   :'Ludwig van Beethoven' => Date.new(1770, 12, 16),
    #   :'Dave Brubeck' => Date.new(1920, 12, 6),
    #   :'Buddy Holly' => Date.new(1936, 9, 7),
    #   :'Keith Richards' => Date.new(1943, 12, 18)
    # }
    birthdays = {
      'Ludwig van Beethoven' => Date.new(1770, 12, 16),
      'Dave Brubeck' => Date.new(1920, 12, 6),
      'Buddy Holly' => Date.new(1936, 9, 7),
      'Keith Richards' => Date.new(1943, 12, 18)
    }
  end

end
