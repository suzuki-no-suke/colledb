<!DOCTYPE HTML>
% # parameter - book_list - list of "book"
% #     book - dictionary
% #        id, img_src, summary
<html>
    <head>
        <meta charset="utf-8"/>
        <title>add new book</title>
    </head>
    <body>
        <table>
        <tr>
            <th>image<th>
            <th>book summary</th>
            <th>edit</th>
        </tr>
        %for book in book_list
        <tr>
           <td>
           %if book['img_src']:
               <img src="{{book['img_src']}}" height=100 />
           %else
               <p>No Image</p>
           %end
           </td>
           <td><p>summary</p></td>
           <td><a href="/app/edit/{{book['id']}}"> edit book info </a></td>
        </tr>
        %end
        </table>
    </body>
</html>
