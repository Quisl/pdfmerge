# About pdfmerge
This is a CLI tool that merges a list of PDF files into one PDF file by attaching the last page of the first PDF with the frist page of the second PDF and so on.

# How to install
1) Make sure Python 3 & pip is installed and environment variables are set. ( --> https://www.python.org/ )
2) Clone this repository with git ( --> https://git-scm.com/ )
```
$ git clone https://github.com/Quisl/pdfmerge.git
```
3) Install requirements like this:
```
$ cd pdfmerge
$ pip install -r requirements.txt
```
# How to use
Run the script pdfmerge.py and give your PDF file names as arguments (parameters). Order matters!

```
python pdfmerge.py [FILE...]
```

Example:
```
$ python pdfmerge.py filename1.pdf filename2.pdf filename3.pdf
```

The resulting filename will be "result.pdf"
