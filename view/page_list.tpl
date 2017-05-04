<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>add new book</title>
    </head>
    <body>
        %for book in book_list
        <div>
           <img href="/image/{{book["image1"]}}"/>
           <p>title : {{book["title"]}}</p>
           <p>author : {{book["author"]}}</p>
           <p>tags : {{book["tags"]}}</p>
        </div>
        %end
    </body>
</html>
