# Scarlet and Black Plain Text Files
Plain text files from Grinnell College's student newspaper, the [*Scarlet and Black*](http://www.thesandb.com/) (1894-2010).

## History:

As described in [*Grinnell Magazine*](http://magazine.grinnell.edu/news/releases/explore-grinnell-college%E2%80%99s-history-through-digital-archive-scarlet-black): "Since its first publication on Sept. 12, 1894, the *Scarlet & Black* has served as a vital source of up-to-date news on campus, an important record of Grinnell College and a rich historical resource."

In 2014, former Samuel R. and Marie-Louise Rosenthal Librarian of the College Richard Fyffe and Special Collections Librarian and Archivist Chris Jones contracted ArcaSearch to digitize past issues of the S&B and place them in [a publicly-accessible database](http://usiagrc.arcasearch.com/Research.aspx). This effort was described in articles published in [*Grinnell Magazine*](http://magazine.grinnell.edu/news/releases/explore-grinnell-college%E2%80%99s-history-through-digital-archive-scarlet-black) and the [S&B](https://www.grinnell.edu/news/over-century-newspaper-archives-digitized).

[That database](http://usiagrc.arcasearch.com/Research.aspx) launched in October 2014 and remains the primary access point for individuals interested in searching and browsing the S&B.

## Methods:

In Spring 2018, [Sarah J. Purcell](https://www.grinnell.edu/user/purcelsj) (L.F. Parker Professor of History & Grinnell Class of 1992) worked with student research assistant [Papa Kojo Ampim-Darko](https://www.linkedin.com/in/papakojo/) (Grinnell College Class of 2019) to explore possibilities for converting the digitized S&B issues into plain-text files that could be used for computational text analysis and other digital research methods. This work was supported by [Julia Bauder](https://www.grinnell.edu/user/bauderj) (Social Studies and Data Services Librarian), and [Katherine Walden](https://www.grinnell.edu/user/waldenka) (Digital Liberal Arts Specialist).

OCR conversion of the tiff image scans was accomplished using [Tesseract 4](https://github.com/tesseract-ocr/tesseract), on a virtual high-performance computing cluster. HPC support was provided by [Mike Conner](https://www.grinnell.edu/user/connerms) (Linux Administrator).

Two Python libraries, [aspell](https://github.com/WojciechMula/aspell-python) and [hunspell](https://github.com/blatinier/pyhunspell), were used to clean the OCR output. The results of both cleaning processes are included in this repo. The Python scripts used to clean the OCR output are also included in this repo.

## Repo Structure

*aspell_cleaner.py* and *hunspell_cleaner.py* include the Python scripts used to clean the Tesseract output. 

The *original_ocr_results* folders include the direct output of the Tesseract OCR process. 

The *ocr_results_aspell* folders include the output from the aspell cleaning process. The *ocr_results_hunspell* folders include the output from the hunspell cleaning process.

The *unstructured* folders include the entire batch of txt files, with no sub-folder structure. The *structured* folders organize the txt files by decade, year, and month.

The file naming convention (maintained from ArcaSearch digitized files) adheres to the following structure:

<blockquote>
 Sample file name: usiagrc_scb_1894_09_12_50_000_00001-00000_000.txt
 Issue year: 1894
 Issue month: 09 (September)
 Issue date: 12 (Twelth)
 Issue page: 00001
</blockquote>


## Acknowledgements:

This project would not have been possible without the indefatibable efforts of former Grinnell student Papa Kojo Ampim-Darko, supported by Sarah Purcell. Julia Bauder provided invaluable technical expertise getting the project off the ground and providing access to the digitized S&B files. Katie Walden served as de-facto project manager, coordinating the various units and individuals involved. The support of Mike Conner and [Sam Rebelsky](https://www.grinnell.edu/user/rebelsky) (Professor of Computer Science), provided necessary access to HPC resources. Additional thanks to [Jarren Santos](https://www.grinnell.edu/user/santosja) (Data Scientist and Grinnell College Class of 2017) of the [Data Analysis and Social Inquiry Lab](http://dasil.sites.grinnell.edu/) for his support of this project.
