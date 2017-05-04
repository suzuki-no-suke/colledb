<!DOCTYPE HTML>
% # parameter - book - dictionary
% #          book - key -> id, title, author, tags, image(1-4)
% #          if image(1-4) is empty, it is not show image
<html>
    <head>
        <meta charset="utf-8"/>
        <title>add new book</title>
    </head>
    <body>
        <a href="/app/list">cancel : back to list</a>
        <form action="/app/book/{{book['id']}}" method="POST" enctype="multipart/form-data">
            % for no in range(1, 5):
                % img_key = "image{}".format(no)
                <p>book {{img_key}}
                  % if book[img_key]:
                      <img src="/image/{{book['id']}}/{{no}}" height=200 />
                  % end
                  <input type="file" name="{{img_key}}" />
                </p>
            % end
            <p>title <input type="text" name="title" value="{{book['title']}}"/> </p>
            <p>author <input type="text"  name="author" value="{{book['author']}}" /></p>
            <p>tags <input type="text" name="tags" value="{{book['tags']}}"/></p>
            <input type="SUBMIT" value="update book"/>
        </form>
    </body>
</html>
