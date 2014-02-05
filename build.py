import markdown
import sys
import codecs

top="""<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>RAM Works</title>
        <link rel="stylesheet" href="../css/normalize.css" type="text/css" media="all">
        <link rel="stylesheet" href="../css/style.css" type="text/css" media="all">
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
             (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
             m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
             })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

            ga('create', 'UA-47687575-1', 'rw.cm');
            ga('send', 'pageview');
        </script>
    </head>
    <body>
"""

bottom="""
    </body>
</html>
"""

input_file = codecs.open(sys.argv[1], mode="r", encoding="utf-8")
text = input_file.read()
html = top
html += markdown.markdown(text,['extra'])
html += bottom

output_file = codecs.open(
                        sys.argv[2], "w", 
                        encoding="utf-8", 
                        errors="xmlcharrefreplace"
                        )
output_file.write(html)
