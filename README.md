# Scarlet and Black Plain Text Files
Plain text files from Grinnell College's student newspaper, the [*Scarlet and Black*](http://www.thesandb.com/) (1894-2010).

## History:

As described in [*Grinnell Magazine*](http://magazine.grinnell.edu/news/releases/explore-grinnell-college%E2%80%99s-history-through-digital-archive-scarlet-black): "Since its first publication on Sept. 12, 1894, the *Scarlet & Black* has served as a vital source of up-to-date news on campus, an important record of Grinnell College and a rich historical resource."

In 2014, former Samuel R. and Marie-Louise Rosenthal Librarian of the College Richard Fyffe and Special Collections Librarian and Archivist Chris Jones contracted ArcaSearch to digitize past issues of the S&B and place them in [a publicly-accessible database](http://usiagrc.arcasearch.com/Research.aspx). This effort was described in title in articles published in [*Grinnell Magazine*](http://magazine.grinnell.edu/news/releases/explore-grinnell-college%E2%80%99s-history-through-digital-archive-scarlet-black) and the [S&B](https://www.grinnell.edu/news/over-century-newspaper-archives-digitized).

[That database](http://usiagrc.arcasearch.com/Research.aspx) launched in October 2014 and remains the primary access point for individuals interested in searching and browsing the S&B.

## Methods:

In Spring 2018, [Sarah J. Purcell, L.F. Parker Professor of History & Grinnell Class of 1992](https://www.grinnell.edu/user/purcelsj), worked with student research assistant [Papa Kojo Ampim-Darko, Class of 2019](https://www.linkedin.com/in/papakojo/), to explore possibilities for converting the digitized S&B issues into plain-text files that could be used for computational text analysis and other digital research methods. This work was supported by [Julia Bauder, Social Studies and Data Serfices Librarian](https://www.grinnell.edu/user/bauderj), and [Katherine Walden, Digital Liberal Arts Specialist](https://www.grinnell.edu/user/waldenka).

OCR conversion of the tiff image scans was accomplished using [Tesseract 4](https://github.com/tesseract-ocr/tesseract), on a virtual high-performance computing cluster. HPC support was provided by [Mike Conner, Linux Administrator](https://www.grinnell.edu/user/connerms).

Two Python libraries, [aspell](https://github.com/WojciechMula/aspell-python) and [hunspell](https://github.com/blatinier/pyhunspell), were used to clean the OCR output. The results of both cleaning processes are included in this repo. The Python scripts used to clean the OCR output are also included in this repo.

## Acknowledgements:

This project would not have been possible without the indefatibable efforts of former Grinnell student Papa Kojo Ampim-Darko, supported by Sarah Purcell. Julia Bauder provided invaluable technical expertise getting the project off the ground and providing access to the digitized S&B files. Katie Walden served as de-facto project manager, coordinating the various units and individuals involved. The support of Mike Conner and [Sam Rebelsky, Professor of Computer Science](https://www.grinnell.edu/user/rebelsky), provided necessary access to HPC resources. Additional thanks to [Jarren Santos](https://www.grinnell.edu/user/santosja) of the [Data Analysis and Social Inquiry Lab](http://dasil.sites.grinnell.edu/) for his support of this project.
