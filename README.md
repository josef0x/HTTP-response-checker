<<<<<<< HEAD
# URL Checker
Simple Python script to check the HTTP status code of a list of URLs stored inside a text file.
This can be useful when doing recon, once we make an In-scope list of URLs.
A typical use case might be to easily determine alive URLs (in an automated manner instead of checking each one of them manually).


## What does the script do ?
In brief : 
1) Requests each URL in the text file (in GET)
2) For each one of them it prints the corresponding status code and stores the final result in the format ```URL:status-code```

## Usage : 
```python3 checker.py URLs.txt```

> Feature 0:
  If a URL contains at least a script tag, the string "Might be interesting" is printed beneath, as an indication that the URL may
  contain useful information (which probably should be checked out manually).
=======
# URL list Checker
Simple Python script to check HTTP status code of a list of URLs in a .txt file

## What does the script do ?
In brief : 
1) Sends a GET request to each URL in your text file
2) Prints for each URL in the list its corresponding status code

## Usage : 
```python3 checker.py domains.txt```
>>>>>>> d6180d9f21f98eee3fab4e875355228512a0948c
