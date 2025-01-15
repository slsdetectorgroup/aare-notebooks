#Rendering version
from IPython.display import Markdown, display
from datetime import datetime as dt
def nb_aare_version():
    try:
        from importlib import metadata
        v = metadata.version('aare')
    except:
        v = 'dev'

    s = f'Example run on: **{dt.now():%Y-%m-%d %H:%M}** with aare: **{v}**'
    display(Markdown(s))
