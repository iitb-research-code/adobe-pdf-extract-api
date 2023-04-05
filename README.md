# adobe-pdf-extract-api
OCR and Layout Adobe PDF Extract API for English Machine Readable Documents.
The src folder contains four different code files.

run_api_get_json
------------------------
This is the standard process to inout a PDF file and get compressed json file of corresponding layout.

run_api_get_hocr 
------------------------
This involves invoking the Adobe PDF Extract API and process the json results to get corresponding hocr file.

```
python3 run_api_get_hocr.py <pdf-input> <output-folder> <page-offset> <page-count>
```

Page offset is 0 for any PDF with less than 100 pages.
Page offset will take value '1' for a split PDF having pages 101 to 200 and so on.
Page count includes count


run_json_get_hocr
------------------------
This is used to parse json result to generate hocr file from already created json file and avoid redundant API requests.
