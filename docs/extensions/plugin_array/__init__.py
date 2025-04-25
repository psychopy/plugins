from pathlib import Path
import json
from sphinx_design.grids import GridDirective
from docutils.parsers.rst import directives, nodes


class plugin_search(nodes.Element):
    tagname = "div"

    def __init__(self, rawsource='', *children, **attributes):
        # pre-populate with class
        attributes['class'] = "plugin-search-container"
        # initialize as normal
        nodes.Element.__init__(self, rawsource, *children, **attributes)

    def on_visit(self, node):
        # open element
        self.body.append(
            node.starttag()
        )
        # define function
        js_file = Path(__file__).parent / "search.js"
        js_text = Path(js_file).read_text(encoding="utf-8")
        self.body.append(
            f"<script type='text/javascript' language='javascript'>\n"
            f"{js_text}\n"
            f"</script>\n"
        )
        # define styles
        css_file = Path(__file__).parent / "search.css"
        css_text = Path(css_file).read_text(encoding="utf-8")
        self.body.append(
            f"<style>\n"
            f"{css_text}\n"
            f"</style>\n"
        )
        # make ctrl
        self.body.append(
            "<input type=search placeholder='Search plugins...' onsearch='filterPlugins(this)' class=plugin-search-ctrl />"
        )

    def on_depart(self, node):
        # close element
        self.body.append(
            node.endtag()
        )


class PluginGridDirective(GridDirective):
    def __init__(self, *args, **kwargs):
        GridDirective.__init__(
            self,
            *args,
            **kwargs
        )
        # array for new content
        lines = [""]
        # run for each line
        for content in self.content:
            # get json file path
            file = self.env.relfn2path(content)[1]
            # load json file
            with Path(file).open("r", encoding="UTF-8") as f:
                plugins = json.load(f)
            # add each plugin
            for profile in plugins:
                # format tags
                tags = [
                    f":bdg:`{tag}`" 
                    for tag in profile['keywords']
                ]
                profile['tags'] = "  ".join(tags)
                # make rst for a card
                card = (
                    ".. grid-item-card:: %(name)s [``%(pipname)s``]\n"
                    "    :link: %(homepage)s\n"
                    "    :img-top: %(icon)s\n"
                    "    :class-card: plugin-card\n"
                    "    :class-title: plugin-card-title\n"
                    "    :class-body: plugin-card-body\n"
                    "    :class-footer: plugin-card-tags\n"
                    "    \n"
                    "    %(description)s\n"
                    "    +++\n"
                    "    %(tags)s\n"
                ) % profile
                # add it to content
                lines += card.split("\n")
        # overwrite original content
        self.content.data = lines
    
    def run(self):
        return [plugin_search()] + GridDirective.run(self)


def setup(app):
    # add nodes
    app.add_node(
        plugin_search,
        html=(plugin_search.on_visit, plugin_search.on_depart),
    )
    # add directives
    directives.register_directive('plugin-grid', PluginGridDirective)

    return {
        'version': '0.1',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }