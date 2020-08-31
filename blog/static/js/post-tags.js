$(document).ready(function()
    {
        var posts = document.getElementsByClassName("post-tags");
        for (var i = 0; i < posts.length; i++)
        {
            post = posts[i];
            var tags_list = post.innerHTML.split(";");
            post.innerHTML = '';
            for (var j = 0; j < tags_list.length; j++)
                post.innerHTML += '<div class="chip">' + tags_list[j] + '</div>';
        }
    }
)