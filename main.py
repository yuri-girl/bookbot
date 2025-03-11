from stats import get_wordcount
from stats import count_characters
from stats import sort_charas
import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents
def main():
	path = sys.argv[1]
	sorted_characters = sort_charas(count_characters(path))
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print("Found " + get_wordcount(path) + " total words")
	print("--------- Character Count -------")
	for i in range(len(sorted_characters)-1):
		print(f"{sorted_characters[i]["char"]}: {sorted_characters[i]["count"]}")
	print("============= END ===============")
main()
