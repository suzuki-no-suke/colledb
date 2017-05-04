<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>book [{{id}}] - {{title}}</title>
    </head>
    <body>
        <div>
            <img href="/image/{{image1}}" />
            <p>title : {{title}}</p>
            <p>author : {{author}} </p>
            <p>tags : {{tags}} </p>
        </div>
        <form action="/app/edit/{{id}}" method="GET">
            <input type="SUBMIT" value="Add new book"/>
        </form>
    </body>
</html>
