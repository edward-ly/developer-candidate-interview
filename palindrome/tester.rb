class Tester
  class T1
    def palindrome?(string)
      # first implementation
      # treat string as an array of characters

      # 1. check edge cases first
        # return false for non-strings and nil strings by checking length method
      # 2. remove non-alphabet characters from string
        # create a new string that will contain only letters from string
        # use POSIX bracket expression to add each letter to the new string
        # if string is empty (no letters to check), return false
      # 3. convert all letters to lowercase for comparison
      # 4. check eack pair of characters one at a time for matches
        # start at the two ends of the string
        # while string[i] and string[j] refer to different characters, make comparison
        # move i and j towards middle of string if letters match, else return false
        # middle character (when i == j) is not important in a palindrome
        # return true if all characters match

      return false if not string.respond_to?(:length)

      test_string = ""
      string.length.times { |char| ( test_string << string[char] ) if ( string[char] =~ /[A-Za-z]/ ) }
      return false if test_string.length == 0

      test_string = test_string.downcase

      i = 0
      j = test_string.length - 1

      while i < j
        return false if not test_string[i] == test_string[j]
        i += 1
        j -= 1
      end

      return true
    end
  end

  class T2
    def palindrome?(string)
      # second implementation
      # use "reverse" method to compare strings (palindrome iff string == reverse_string)

      # 1-3. process string in the same manner as before
      # 4. compare string with reverse string and return result

      return false if not string.respond_to?(:length)
      test_string = ""
      string.length.times { |char| test_string << string[char] if string[char] =~ /[A-Za-z]/ }
      return false if test_string.length == 0
      test_string = test_string.downcase

      return test_string == test_string.reverse
    end
  end
end
