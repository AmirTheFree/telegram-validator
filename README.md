# Telegram Validator

### A tool for finding Telegram usernames by phone number.

* Remove `.sample` from end of two files: `dbinfo.py.sample` & `tinfo.py.sample`

* Fill those files with your database info and Telegram app info(you must get from my.telegram.org)

* If you need proxy for connecting to Telegram uncomment all comments in `tinfo.py` & `app.py` (except `In the name of Allah` line at top of files) and fill the variables in `tinfo.py`

* For adding phone numbers to list (database) read `dbconfig.py` line 21

* For checking and saving Telegram info of numbers run `app.py`