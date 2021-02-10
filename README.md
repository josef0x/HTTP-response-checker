# URL list Checker
Simple Python script to check the HTTP status code of URLs in a .txt file

## What does the script do ?
In brief : 
1) Sends a GET request to each URL in your text file
2) Prints for each URL in the list the corresponding status code

## Usage : 
```python3 checker.py domains.txt```

> Feature 0:
  If a URL contains at least a HTML <script> tag, the script adds "Might be interesting" under the corresponding URL, as an indication that it might
  contain useful information that should be checked out manually.
