## :file_cabinet: :open_file_folder: Institutional Data Curation and Reconciliation :open_file_folder: :file_cabinet:
![coverage](https://img.shields.io/badge/Purpose-Research-yellow)
[![Generic badge](https://img.shields.io/badge/Python-3.8-red.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/License-MIT-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/BuildPassing-No-orange.svg)](https://shields.io/)
![coverage](https://img.shields.io/badge/Data-Institutional-purple)
---


A Repository to hold some miscellaneous code for institutional scrape, parse and ingestion. Build not passing. Further work required! Some code feeds into NHSSpend, and some into a forthcoming CH project (with [aaronreeves](https://github.com/asreeves)). Accounts data parser based on work from [drkane](https://github.com/drkane). `get_all_ch_data.py` requires CH FTP Access, and this is parsed with the functions in `parse_ftp.py` which was created by [Gabriele Simeone](github.com/gsime) whilst at Transparency International. `ingest_everything.py` requires a local elasticsearch installation which is running (sudo systemctl start elasticsearch.service). Work on the `Elasticsearch` functionality comes from [ianknowles](https://github.com/ianknowles). Also requires subdir data path set up for caching things like `get_all_ch_data.py`. Watch this space for more in the future!
