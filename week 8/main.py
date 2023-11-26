number_of_words = 0
with open(r'morning_has_broken.txt','r') as file:
  data=file.read()
  lines=data.split()
  number_of_words += len(lines)
with open(r"morning_has_broken.txt", "r") as fp:
  number_of_lines = len(fp.readlines())
  
number_of_words_str = str(number_of_words)
number_of_lines_str = str(number_of_lines)
word_count = open("morning_has_broken_word_count_and_line_count.txt", "a")
word_count.write("The song contains " + number_of_words_str + " words" + " and " + number_of_lines_str + " lines.")
word_count.close()