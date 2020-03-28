# Emotion annotated datasets 

Here, we provide line-level emotion annotated datasets for English and German in simple tab separated format. The relevant data files are
- `english.tsv`
- `emotion.german.tsv`

The structure of the data is as follows:

1. Title of the poem
2. Newline separates stanzas
3. Two newlines separate poems
4. Per line: tab separates text and annotations. There are two annotations per line, corresponding to the two annotators.
5. Each annotator annotates 1 or 2 emotions per line. Emotion separator is "---"

**NB** This directory does not include the 48 gold standard annotated poems.
