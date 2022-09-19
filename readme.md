
## About The Project

This is a basic start to renaming files using barcodes.

The process will go through every file within your file system and rename them while moving them to an output location of your choice.
 
<!-- GETTING STARTED -->
## Getting Started

Create a terminal session
Add your required switches -
-i = PDF input file location
-o = PDF output file location

```
python panda.py -i 'C:\Users\patpa\Documents\Coding\panda\pdfs' -o 'C:\Users\patpa\Documents\Coding\panda\output'
```
## Prerequisites

Things to install to make sure this works
* Python3
* Have some files to test with - this repo has some examples

  ```sh
  pip install pdf2image pyzbar
  ```
