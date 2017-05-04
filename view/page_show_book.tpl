<!DOCTYPE HTML>
% parameter : book - dictionary - id, title, author, tags
%           : image_nos - list of image id (1-4)
<html>
    <head>
        <meta charset="utf-8"/>
        <title>book [{{book['id']}}] - {{book['title']}}</title>
    </head>
    <body>
        <div>
            %for img_no in image_nos:
                <img href="/image/book['id']/{{img_no}}" />
            %end
            <p>title : {{book['title']}}</p>
            <p>author : {{book['author']}} </p>
            <p>tags : {{book['tags']}} </p>
        </div>
        <form action="/app/edit/{{book['id']}}" method="GET">
            <input type="SUBMIT" value="Add new book"/>
        </form>
    </body>
</html>
