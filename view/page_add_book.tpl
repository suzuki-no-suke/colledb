<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>add new book</title>
    </head>
    <body>
        <a href="/app/list">back to list</a>
        <form action="/app/add" method="POST" enctype="multipart/form-data">
            <p>book image1 <input type="file" name="image1"/></p>
            <p>book image2 <input type="file" name="image2"/></p>
            <p>book image3 <input type="file" name="image3"/></p>
            <p>book image4 <input type="file" name="image4"/></p>
            <p>title <input type="text" name="title"/> </p>
            <p>author <input type="text"  name="author"/></p>
            <p>tags <input type="text" name="tags"/></p>
            <input type="SUBMIT" value="Add new book"/>
        </form>
    </body>
</html>
