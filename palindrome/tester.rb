class Tester
  class T1
    def palindrome?(string)
      # first implementation
      # treat string as an array of characters

      # 1. check edge cases first

      # return false for non-strings and nil strings by checking length method
      return false if not string.respond_to?(:length)

      # 2. remove non-alphabet characters from string

      # create a new string that will contain only letters from string
      test_string = ""
      # use POSIX bracket expression to add each letter to the new string
      string.length.times { |char| test_string << string[char] if string[char] =~ /[A-Za-z]/ }

      # if there are no letters to check, return false
      return false if test_string.length == 0

      # 3. convert all letters to lowercase for comparison
      test_string = test_string.downcase

      # 4. check eack pair of characters one at a time for matches


    end
  end

  class T2
    def palindrome?(string)
      # second implementation
      # use "reverse" method to compare strings

      # 1-3. process string in the same manner as before

      return false if not string.respond_to?(:length)
      test_string = ""
      string.length.times { |char| test_string << string[char] if string[char] =~ /[A-Za-z]/ }
      return false if test_string.length == 0
      test_string = test_string.downcase

      # 4. compare string with reverse string and return result


    end
  end
end
