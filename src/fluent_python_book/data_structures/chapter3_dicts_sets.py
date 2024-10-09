# Compile the word pattern regex
# WORD_RE = re.compile(r'\w+')

# # Initialize an empty dictionary to store the word index
# index = {}

# # Open the file specified in the command line argument
# with open(sys.argv[1], encoding='utf-8') as fp:
#     # Iterate over each line in the file with line numbers starting from 1
#     for line_no, line in enumerate(fp, 1):
#         # Find all matches of the word pattern in the current line
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)

#             # Cool feature:
#             index.setdefault(word, []).append(location)

#             # alternative


# # Display the words and their locations in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])


# setdefault() explained
my_dict = {}
key = "my_key"
new_value = 1

my_dict.setdefault(key, []).append(new_value)

if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(new_value)
