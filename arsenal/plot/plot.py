
# Extracted from pandas, which intern extracted it from
# https://gist.github.com/huyng/816622 this is the rcParams set when setting
# display.with_mpl_style to True.
mpl_stylesheet = {
    'axes.axisbelow': True,
     'axes.color_cycle': ['#348ABD',
                          '#7A68A6',
                          '#A60628',
                          '#467821',
                          '#CF4457',
                          '#188487',
                          '#E24A33'],
     'axes.edgecolor': '#bcbcbc',
     'axes.facecolor': '#eeeeee',
     'axes.grid': True,
     'axes.labelcolor': '#555555',
     'axes.labelsize': 'large',
     'axes.linewidth': 1.0,
     'axes.titlesize': 'x-large',
     'figure.edgecolor': 'white',
     'figure.facecolor': 'white',
     'figure.figsize': (6.0, 4.0),
     'figure.subplot.hspace': 0.5,
     'font.family': 'monospace',
     'font.monospace': ['Andale Mono',
                        'Nimbus Mono L',
                        'Courier New',
                        'Courier',
                        'Fixed',
                        'Terminal',
                        'monospace'],
     'font.size': 8,
     'interactive': True,
     'keymap.all_axes': ['a'],
     'keymap.back': ['left', 'c', 'backspace'],
     'keymap.forward': ['right', 'v'],
     'keymap.fullscreen': ['f'],
     'keymap.grid': ['g'],
     'keymap.home': ['h', 'r', 'home'],
     'keymap.pan': ['p'],
     'keymap.save': ['s'],
     'keymap.xscale': ['L', 'k'],
     'keymap.yscale': ['l'],
     'keymap.zoom': ['o'],
     'legend.fancybox': True,
     'lines.antialiased': True,
     'lines.linewidth': 1.0,
     'patch.antialiased': True,
     'patch.edgecolor': '#EEEEEE',
     'patch.facecolor': '#348ABD',
     'patch.linewidth': 0.5,
     'toolbar': 'toolbar2',
     'xtick.color': '#555555',
     'xtick.direction': 'in',
     'xtick.major.pad': 6.0,
     'xtick.major.size': 0.0,
     'xtick.minor.pad': 6.0,
     'xtick.minor.size': 0.0,
     'ytick.color': '#555555',
     'ytick.direction': 'in',
     'ytick.major.pad': 6.0,
     'ytick.major.size': 0.0,
     'ytick.minor.pad': 6.0,
     'ytick.minor.size': 0.0
}

import numpy as np
import matplotlib as mpl
import matplotlib.pylab as pl

mpl.rc_params().update(mpl_stylesheet)


xs, ys = np.random.uniform(0,1,size=(2,30))
pl.scatter(xs, ys)

pl.show()
