# unclaim-s3-finder

This is a lightweight tool that check wheather bucket is avaliable for takeover or not.

## Requirment:

### packages 

- requests
- xmltodict
- bcolors
- sys
- argparse

### python > 3.x 

## usage: 

bucket-takeover.py  -u < Valid Bucket URL with http:// or https:// >

OPTIONS: 

```
-u            valid bucket URL with http:// or https:// or a text file with bucket names 
  		< bucket is avaibale for takeover or not >
