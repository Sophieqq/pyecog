[![PyPI version](https://badge.fury.io/py/pyecog.svg)](https://badge.fury.io/py/pyecog)
## PyECoG
This module is for detecting epileptiform activity from *single* channel intracranial EEG (or ECoG) recordings.
Currently under heavy construction!

http://jcornford.github.io/pyecog/

### Recommended installation procedure:

1. Install [Anaconda](https://www.continuum.io/downloads). Choose the Python 3, 64-bit version for your operating system (Linux, Windows, or OS X). You can also download python 2, but just make sure your python version for the environment is 3 (next step).

2. Make a new conda environment and install dependencies for pyecog. To do this open a terminal windows (on Windows, a cmd prompt) and type or copy:
    ```{bash}
    conda create --name pyecog python=3.7 jupyter=1 scipy=1.4.1 numpy=1.18.1 scikit-learn=0.21.3 pandas=1.0.1 matplotlib=3.1.3 seaborn=0.10.0 h5py=2.10.0 xlrd=1.2.0 pyqt=5.9.2 numba=0.48.0
    source activate pyecog  # or just "activate pyecog_env" if you are on windows
    pip install pyqtgraph
   ```
 * Note you do not have to make a virtual environment if you will not be using python for anything else. See below.
 
3. Click on the green "clone or download" button on the top right of this page. Download the zip file and extract it somewhere on your computer. Navigate to the extracted folder in terminal/cmd line or open a terminal/cmd window at the extracted folder. To do this quickly on windows shift+right click on the folder and select "open a command window here". 

4. Finally, you are ready to run. First activate your python environment with the required dependencies for the Pyecog gui:
```{bash}
activate pyecog  # or  "source activate pyecog_env" if on a mac
```
And then run the gui with:
```{bash}
python start.py
```
---

### Installing with pip:
This is for when the software is more developed.

1 . After step 2 above, run:
```{bash}
pip install pyecog
```
2. Ignore step 3. Open command window and activate the pyecog_env environment if you are using it. Type "pyecog" into the prompt. The Gui should load.
---
### How to use - this needs to be updated
- note, some gui elements not implemented (open in jupyter notebook and low pass filter)
- [Loading ndf files] (https://github.com/jcornford/pyecog/blob/master/documentation_notebooks/demo_loading_ndfs_notebook.ipynb)
---
### Repository contents:
* NDF:           code is the current working directory.
* visualisation: contains a bunch of visualisation experiments
