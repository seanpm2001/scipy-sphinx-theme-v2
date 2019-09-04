import sys
import os

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('./demo/'))

# sys.path.insert(0, os.path.abspath('./sphinxext'))

needs_sphinx = '1.1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.imgmath', 'numpydoc',
              'sphinx.ext.intersphinx', 'sphinx.ext.coverage',
              'sphinx.ext.autosummary', 'matplotlib.sphinxext.plot_directive']


templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'scipy-sphinx-theme-v2'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'



# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

intersphinx_mapping = {'rtd': ('https://docs.readthedocs.io/en/latest/', None)}


# -- Options for HTML output ---------------------------------------------------

# themedir = os.path.join(os.pardir, '../')
import custom_sphinx_theme
themedir = custom_sphinx_theme.get_path()
print(themedir)
if not os.path.isdir(themedir):
    raise RuntimeError("Get the scipy-sphinx-theme-v2 first, "
                       "via git submodule init && git submodule update")

html_theme = 'custom_sphinx_theme'
html_theme_path = [themedir]

#html_logo = '_static/scipyshiny_small.png'
# html_static_path = ['_static']
html_theme_options = {
    "edit_link": "true",
    "sidebar": "right",
    "scipy_org_logo": "true",
    "rootlinks": [("http://scipy.org/", "Scipy.org"),
                  ("http://docs.scipy.org/", "Docs")]
}

#------------------------------------------------------------------------------
# Plot style
#------------------------------------------------------------------------------

plot_pre_code = """
import numpy as np
import scipy as sp
np.random.seed(123)
"""
plot_include_source = True
plot_formats = [('png', 96), 'pdf']
plot_html_show_formats = False

import math
phi = (math.sqrt(5) + 1)/2

font_size = 13*72/96.0  # 13 px

plot_rcparams = {
    'font.size': font_size,
    'axes.titlesize': font_size,
    'axes.labelsize': font_size,
    'xtick.labelsize': font_size,
    'ytick.labelsize': font_size,
    'legend.fontsize': font_size,
    'figure.figsize': (3*phi, 3),
    'figure.subplot.bottom': 0.2,
    'figure.subplot.left': 0.2,
    'figure.subplot.right': 0.9,
    'figure.subplot.top': 0.85,
    'figure.subplot.wspace': 0.4,
    'text.usetex': False,
}
