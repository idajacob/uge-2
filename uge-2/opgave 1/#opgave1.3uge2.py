#opgave1.3uge2.py

from collections import defaultdict

class NameSorter:
    def __init__(self, names):
        self.names = names
        self.sorted_names = sorted(names, key=str.lower)
        self.letter_counts = defaultdict(int)

    def sort_names(self):
        return self.sorted_names

    def count_letters(self):
        for name in self.sorted_names:
            for letter in name:  
                if letter.isalpha():
                    self.letter_counts[letter.lower()] += 1
        return self.letter_counts

    def print_results(self):
        print(self.sorted_names)
        for letter, count in sorted(self.letter_counts.items()):
            print(f"{letter}: {count}")


names = [
    "Zander", "Travon", "Juanita", "Trista", "Quinlan", "Franklin", "Tasia", "Bridget", "Kourtney", "Jewel", 
    "Keagan", "Cristopher", "Dillion", "Nathaniel", "Christa", "Dakotah", "Darlene", "Warren", "Marvin", 
    "Talia", "Treasure", "Kaylee", "Xochitl", "Dwayne", "Abbigail", "Gianna", "Jaxson", "Dylan", "Tracy", 
    "Tristen", "Rolando", "Chancellor", "Tyreese", "Noah", "Matteo", "Marcanthony", "Kiya", "Danielle", 
    "Meaghan", "Santiago", "Montana", "Gerardo", "Beyonce", "Kobi",
]

name_sorter = NameSorter(names)
name_sorter.sort_names()
name_sorter.count_letters()
name_sorter.print_results()