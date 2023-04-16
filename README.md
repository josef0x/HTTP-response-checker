# URL Checker
Simple Python script to check the HTTP status code of a list of URLs stored inside a text file.
This can be useful when doing recon, once we make an In-scope list of URLs.
A typical use case might be to easily determine alive URLs (in an automated manner instead of checking each one of them manually).


## What does the script do ?
In brief : 
1) Requests each URL in the text file (in GET)
2) For each one of them it prints the corresponding status code and stores the final result in the format ```URL:status-code```

## TODO:
> Make the script multi-threaded !

## Usage : 
```python3 checker.py URLs.txt```

> Feature 0:
  If a URL contains at least a script tag, the string "Might be interesting" is printed beneath, as an indication that the URL may
  contain useful information (which probably should be checked out manually).
