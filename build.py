import markdown
import sys
import codecs
from string import Template

top_1="""<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>$title</title>
        <link rel="stylesheet" href="$css_path/normalize.css" type="text/css" media="all">
        <link rel="stylesheet" href="$css_path/style.css" type="text/css" media="all">
"""

top_2="""
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
    $body_before
"""

bottom="""
    </body>
</html>
"""

def build_html(in_file, out_file, css_path='css'):
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    md = markdown.Markdown(extensions = ['abbr','meta'])
    md_out = md.convert(text)
    metas = md.Meta

    top_1_t = Template(top_1)
    html = top_1_t.substitute(title=metas['title'][0], css_path=css_path)

    meta_tags = ""
    s = Template('<meta name="$name" content="$content" />')
    
    for (k,v) in metas.items():
        meta_tags += s.substitute(name=k,content=v[0])

    print meta_tags
    html += meta_tags

    top_2_t = Template(top_2)
    html += top_2_t.substitute(body_before=
            '<h5>Posted: ' + metas['date'][0] + ' Updated: ' + metas['updated'][0] + '</h5>'
            )
    html += md_out
    html += bottom

    output_file = codecs.open(
                            out_file, "w", 
                            encoding="utf-8", 
                            errors="xmlcharrefreplace"
                            )
    output_file.write(html)

build_html(sys.argv[1], sys.argv[2],'../css')
