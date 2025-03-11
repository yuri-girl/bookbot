def get_wordcount(path):
	wordcount = 0
	with open(path) as f:
		words = (f.read()).split()
		for word in words:
			wordcount += 1
	return str(wordcount)
def count_characters(path):
	with open (path) as f:
		chars = list(f.read())
		count = {}
		for char in chars:
			char = char.lower()
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
		return count
def sort_charas(dict):
	char_list = []
	for char, count in dict.items():
		if char.isalpha():
			char_list.append({"char": char, "count": count})
	def sort_on(dict):
		return dict["count"]
	char_list.sort(reverse=True, key=sort_on)
	return char_list
