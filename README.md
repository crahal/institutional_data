# institutional_data
a repo to hold some miscellaneous code for institutional scrape, parse and ingestion. Build not passing. Further work required! Some code feeds into NHSSpend, and some into a forthcoming CH project (with @aaronreeves). Accounts data parser based on work from @drkane. get_all_ch_data.py requires CH FTP Access. ingest_everything.py requires a local elasticsearch installation which is running (sudo systemctl start elasticsearch.service). Also requires subdir data path set up for caching things like get_all_ch_data.py. Watch this space for more in the future!
