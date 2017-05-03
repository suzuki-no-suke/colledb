API server specification
=========================

overview
========
Dojin books database manipulation

- REST APIs
- return JSON value



APIs
====

## GET /list
get "all" of books

- response
```
{
    'books' : [
        {
            "ID": <book id>
            "title": "book title",
            "summary": "book author and tags summary"
        },
        ... <and all books> ...
    ]
}
```

- error
  - no books
    - array books is 0 length


## GET /book/<id>
get single book data

- response
```
{
    "ID": <book id>
    "title": "book title",
    "author": "book author",
    "tags": "book tags",
    "created": "YYYY-MM-DD HH:MM:SS" (ISO8601 formatted time)
    "updated": "YYYY-MM-DD HH:MM:SS" (ISO8601 formatted time)
}
```

- error
  - when not found -> 404


## POST /book
add new book to database

NOTE : "appendix", "papers", "good" register as other item.
 not : register as image of book
 recommend : same book name and add postfix
   - book
   - book - appendix
   - book - C90 only paper

- POST parameter
  - not json

- "title": "book title",
- "author": "book author",
- "tags": "book tags",

# multipart file
- "image1": <image binary>
- "image2": <image binary>
- "image3": <image binary>
- "image4": <image binary>


- POST result response
```
{
    "ID": <book id>
}
```


## PUT /book/<id>
update book on database

- POST parameter
```
{
    "title": "book title",
    "author": "book author",
    "tags": "book tags",

    # multipart file
    "image1": <image binary>
    "image2": <image binary>
    "image3": <image binary>
    "image4": <image binary>
}
```

- NOTE
if image does not specified in key, it is not updated
if image value is empty, it is not updated

Value specification
===================
- text encoding : UTF-8

- title : upto 1024 charactors (UTF-8)
- author : upto 4096 charactors (UTF-8)
- tags : upto 8192 charactors (UTF-8)

- image(1-4) : size limit 4MB


Additional APIs
---------------
## GET /thumbnail/<book id>
get book thumbnail image

- use first book image to thumbnail

NOTE : in future : fixed size


## GET /image/<book id>[/<number>]
get book image

- number -> all books can add upto 4 images
  - default : 1


Plan
====
## GET /search/<keyword>/<order>

## GET /list/<order>


