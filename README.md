# PO-EMO

This is [PO-EMO](https://arxiv.org/abs/2003.07723), a corpus of German and English poetry, annotated on line level with aesthetic emotions.

Repository is continuously being updated.

## Structure of the repository

- 48 gold annotated German poems in XML format are given in [XMLGold](XMLGold/)
- 110 German poems and 64 English poems annotated by two annotators are given in [tsv](tsv/) in tab separated format
- All 158 German poems with emotion and prosody annotation in tsv 
- Sample code is provided in [code](code/)
- Our annotation guidelines can be found in [annotationGuidelines](annotationGuidelines/)

## Further releases

- We had one (female) native Chinese speaker annotate 30 classical and 30 modern Chinese poems according to the label scheme of PO-EMO
- The links to the data are here: [30 modern](https://docs.google.com/spreadsheets/d/1ilxAN0ap3FGOeSG4i1XUG6TWRpOUa8yLZRMaqvrLabY/edit?usp=sharing), [30 classical](https://docs.google.com/spreadsheets/d/12SuEeGRszDhPtSTD7uO6G__2fDfNaIrz4qsLnS-YORE/edit?usp=sharing)
- Before doing so, we had the annotator "train" on batches of 5-8 English poems until acceptable agreement was finally reached (see details: [here](https://docs.google.com/spreadsheets/d/1WOI-w72EAstejrS3WRJyQwGbmdj7YtBG9LQO6YkcS2Y/edit?usp=sharing) and [here](https://docs.google.com/spreadsheets/d/1jXIsQWU53jC7sgf_gLTwEPm3yIgBb3E6ZkUlbDE3Eas/edit?usp=sharing)) 
- Subsequently, the annotator annotated further [15 modern](https://docs.google.com/spreadsheets/d/17I_PjQ_6L_uPGfCAEq4pxkS4QDNkX86tkQXvZCVT0W8/edit?usp=sharing) and [15 classical](https://docs.google.com/spreadsheets/d/19XOSdPu0cqm4vD4RW6TmvuXd9HevONzmUYqYofMjD2Y/edit?usp=sharing) poems.


## Reference

If you find this resource helpful, consider citing our paper

```
@inproceedings{Haider2020,
  author = {Thomas Haider and Steffen Eger and Evgeny Kim and Roman Klinger and Winfried Menninghaus},
  title = {{PO-EMO}: Conceptualization, Annotation, and Modeling of Aesthetic Emotions in {German} and {English} Poetry},
  booktitle = {Proceedings of the 12th International Conference on Language Resources
	and Evaluation (LREC'20)},
  year = {2020},
  editor = {Nicoletta Calzolari and Khalid Choukri and Thierry Declerck and Hrafn
	Loftsson and Bente Maegaard and Joseph Mariani and Asuncion Moreno
	and Jan Odijk and Stelios Piperidis},
  address = {Marseille, France},
  month = {May},
  publisher = {European Language Resources Association (ELRA)},
  date = {11-16},
  language = {english},
  note = {accepted},
  url = {http://www.romanklinger.de/publications/HaiderEgerKimKlingerMenninghaus2020LREC_PO-EMO.pdf}
}
```


