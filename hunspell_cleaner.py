import glob
from hunspell import HunSpell
spellchecker = HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')

def correct_word(checker, line, add_to_dict=[]):
    "Takes in a hunspell object and a word and corrects the word if needed"
    # Add custom words to the dictionary
    for w in add_to_dict:
        checker.add(w)

    corrected = ""
    # Check to see if it's a string
    words = line.split()
    numwords = len(words)
    worth = 0
    for word in words:
        if isinstance(word, unicode):
            # Check the spelling
            ok = checker.spell(word)
            if not ok:
                # Grab suggestions for misspelled word
                suggestions = checker.suggest(word)
                if suggestions:
                    # Grab the best suggestion
                    best = suggestions[0]
                    print word + ", " + best
                    corrected = best
                else:
                    # There are no suggestions for misspelled word, return the original
                    # count += 1
                    corrected = word
            else:
                # Word is spelled correctly
                corrected = word
        else:
            ## Not a string. Return original
            corrected = word
        return corrected


def main():
    file_list = glob.glob("./ocr_results/*.txt")
    print(file_list)
    for txtfile in file_list: 
        with open(txtfile) as f:
            content = f.readlines()
            for line in content:
                line = line.decode('utf-8')
                correct_word(spellchecker, line, ["Grinnell", "SCARLET", "Scarlet"])

main()