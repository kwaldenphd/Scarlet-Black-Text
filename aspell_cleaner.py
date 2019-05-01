import aspell
import glob
spellchecker = aspell.Speller('lang', 'en')

def correct_word(checker, line, add_to_dict=[]):
    "Takes in an aspell object and a word and corrects the word if needed"
    # Add custom words to the dictionary
    for w in add_to_dict:
        checker.addtoPersonal(w)

    corrected = ""
    # Check to see if it's a string
    words = line.split()
    numwords = len(words)
    worth = 0
    for word in words:
        if isinstance(word, str):
            # Check the spelling
            ok = checker.check(word)
            if not ok:
                # Grab suggestions for misspelled word
                suggestions = checker.suggest(word)
                if suggestions:
                    # Grab the best suggestion
                    best = suggestions[0]
                    # print(word + ", " + best)
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
    file_list = glob.glob("./ocr_results aspell/*.txt")
    for txtfile in file_list: 
        print txtfile
        with open(txtfile) as f:
            content = f.readlines()
            for line in content:
                # line = line.decode('utf-8')
                correct_word(spellchecker, line, ["Grinnell", "SCARLET", "Scarlet"])
# you may also want to remove whitespace characters like `\n` at the end of each line

main()
