plan - DBMS
===========

# first step
- use SQLite (3)

- need : save images into DB


## schemes
books
- id : unique id - INTEGER (PRIMARY KEY, INCREMENT)
- image1, image2, image3, image4 : file name of image, uuid - string (64)
  - uuid string length - 60 chars
- name : book name - string(1024)
- author : author name(s) - string (4096)
- tags : free format tags - string (8192)
- created : datetime string - string (32)
- updated : datetime string - string (32)
  - datetime format : ISO8601 (YYYY-MM-DD HH:MM:SS.SSS) - 23 chars

