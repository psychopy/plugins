from pathlib import Path
import json
from sphinx_design.grids import GridDirective
from docutils.parsers.rst import directives


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
                # make rst for a card
                card = (
                    ".. grid-item-card:: %(name)s [``%(pipname)s``]\n"
                    "    :link: %(homepage)s\n"
                    "    :img-top: %(icon)s\n"
                    "    \n"
                    "    %(description)s\n"
                ) % profile
                # add it to content
                lines += card.split("\n")
        # overwrite original content
        self.content.data = lines


def setup(app):
    # add directives
    directives.register_directive('plugin-grid', PluginGridDirective)

    return {
        'version': '0.1',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }