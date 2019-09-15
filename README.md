# Keyboard Layout Evaluator
This python script evaluates keyboad layouts for words that can be typed on a single row.

## Motivation
This script was initially developed to evaluate the claim that the DVORAK layout permitted the user to type far more words on one row than the QWERTY layout.

## Results
While testing with a list of 370099 it was discovered that 6090 of those words could be typed on one row with the DVORAK layout, compared to a mere 1698 with QWERTY and 2308 with AZERTY. Furthermore, of those DVORAK allowed the user to type 5975 words on the home row, meaning only 115 of the words on one row weren't on the home row. For QWERTY the number dropped drastically to 387 words while AZERTY only placed 100 words on the home row.

I also looked at the 3000 most common words in the English language. 175 of these could be typed on one row with DVORAK, 91 with QWERTY and 94 with AZERTY. For the home row, this dropped to 172 with DVORAK (just 3 fewer), 18 words with QWERTY and only 1 word with AZERTY.

## Use
Simply download and run the script, giving up the name of a text file in the same directory to check. The script will display the number of words that can be typed on a single row, as well as the number of words that can be typed on the home row alone in the console. The keyboard layouts defined at the top of the file, which is where the user can add other layouts. QWERTY, DVORAK and AZERTY are already included in the file, but can be removed to improve performance. Note that the script assumes the text file to be all-alpha, all-lowercase and free of duplicates.

## Credit
Testing was done with the all-alpha word list from the open source list of English words found over at [english-words](https://github.com/dwyl/english-words), as well as with the list [3000 most common words in English](https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/), provided by Education First.
