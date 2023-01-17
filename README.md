# adobe-pdf-extract-api
OCR and Layout Adobe PDF Extract API for English Machine Readable Documents.
The src folder contains four different code files.

run_api_get_json is the standard process to inout a PDF file and get compressed json file of corresponding layout.

run_api_get_hocr involves invoking the Adobe PDF Extract API and process the json results to get corresponding hocr file.

run_json_get_hocr is used to parse json result to generate hocr file from already created json file and avoid redundant API requests.
