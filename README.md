# Keyboard Layout Evaluator
This python script evaluates keyboad layouts for words that can be typed on a single row.

## Motivation
This script was initially developed to evaluate the claim that the DVORAK layout permitted the user to type far more words on one row than the QWERTY layout.

## Results
While testing with a list of 370099 it was discovered that 6090 of those words could be typed on one row with the DVORAK layout, compared to a mere 1698 with QWERTY and 2308 with AZERTY. Furthermore, of those DVORAK allowed the user to type 5975 words on the home row, meaning only 115 of the words on one row weren't on the home row. For QWERTY the number dropped drastically to 387 words while AZERTY only placed 100 words on the home row.

## Use
Simply download and run the script, giving up the name of a text file in the same directory to check. Note that the script assumes the text file to be all-lowercase and free of duplicates.

## Credit
Testing was done with the all-alpha word list from the open source list of English words found over at [this](https://github.com/dwyl/english-words) great project.
