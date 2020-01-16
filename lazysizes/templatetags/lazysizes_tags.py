from django import template

from lazysizes.util import lazysize_images


register = template.Library()


class LazySizesNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return lazysize_images(output)
        

def do_lazysizes(parser, token):
    nodelist = parser.parse(('endlazysize_images',))
    parser.delete_first_token()
    return LazySizesNode(nodelist)


register.tag('lazysize_images', do_lazysizes)