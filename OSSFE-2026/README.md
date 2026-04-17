# TokaMaker Example as part of the Open Source Software for Fusion Energy (OSSFE) Conference (3/2026)

Notebooks for this workshop can be run in two ways:

1. Online on **Google Colab** (no setup needed, but must have a Google account)
  - [**Using TokaMaker to build a mesh for CUTE**](https://colab.research.google.com/github/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/blob/main/OSSFE-2026/CUTE_mesh_ex.ipynb)
  - [**Using TokaMaker to design a pulse in CUTE**](https://colab.research.google.com/github/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/blob/main/OSSFE-2026/CUTE_pulse_ex.ipynb)
  - [**Using TokaMaker to predict currents and forces induced during a CQ in ITER**](https://colab.research.google.com/github/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/blob/main/OSSFE-2026/ITER_disruption_forces.ipynb)

2. On a **local installation of Python** that includes Jupyter notebook. (Advanced)

Some functionality, like interactive plots, may not work on Google Colab. Instructions are included below for each option.


# Table of contents

1. [Running Examples on Google Colab](#installation_google_colab)
2. [Running Examples on Jupyter Notebook Locally](#installation_jupyter)
3. [Tips on Using Jupyter Notebook](#jupyter_tips)

# Running Examples on Google Colab <a name="installation_google_colab"></a>

## Opening the Notebooks

To open the notebooks on **Google Colab**, please open the links at the top of this README.

# Running Examples on Jupyter Notebook Locally (Jupyter required) <a name="installation_jupyter"></a>
1. Download the .ipynb file for the notebook(s)

   The notebooks can be downloaded from GitHub at the following links or by checking out the [OpenFUSIONToolkit-Tutorials](https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials) repo.

   - [**Using TokaMaker to build a mesh for CUTE**](https://raw.githubusercontent.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/main/OSSFE-2026/CUTE_mesh_ex.ipynb)
   - [**Using TokaMaker to design a pulse in CUTE**](https://raw.githubusercontent.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/main/OSSFE-2026/CUTE_pulse_ex.ipynb)
   - [**Using TokaMaker to predict currents and forces induced during a CQ in ITER**](https://raw.githubusercontent.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/main/OSSFE-2026/ITER_disruption_forces.ipynb)

2. Download and install [Open FUSION Toolkit](https://github.com/hansec/OpenFUSIONToolkit/releases/tag/v1.0.0-beta7) release for your platform

   Ensure `OFT_ROOTPATH` is set to a suitable value or the installation path is included in your `PYTHONPATH`.


# Tips on Using Jupyter Notebook <a name="jupyter_tips"></a>

- Select "Runtime>Run All" to run the entire notebook. 
- To run a single cell, select the cell with your mouse and then press "Shift+Enter"
- Create new cells using the "Insert" menu or the "+Code" button.
