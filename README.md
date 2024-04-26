# URL Checker
Simple Python script to check the HTTP status code of a list of URLs stored in a text file.
This can be useful when doing recon, once a list of URLs is available.
A typical use case is to easily determine alive URLs (in an automated manner instead of checking each one manually).


## What does the script do ?
In brief : 
1) Requests each URL in the text file (in GET)
2) For each one of them it prints the corresponding status code and stores the final result in the directory `output_files`

## Usage : 
```python3 checker.py -i URLs.txt```