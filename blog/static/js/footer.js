$(document).ready(function()
    {
        if( $(document).height() < $(window).height() )
        {
            $('main').height
            (
                $(window).height - $('nav').height() - $('footer').height()
            );
        }
    }
)
