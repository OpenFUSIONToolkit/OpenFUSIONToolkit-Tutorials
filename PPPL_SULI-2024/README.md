# TokaMaker Workshop at the SULI Summer School (6/2024)

Notebooks for this workshop can be run in two ways:

1. Online on **Google Colaboratory** (no setup needed, but must have a Google account)
  - [**Example 1: Fixed-boundary Equilibria**](https://colab.research.google.com/github/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/blob/main/PPPL_SULI-2024/ex1-fixed_boundary.ipynb)
  - [**Example 2: Free-boundary Equilibria**](https://colab.research.google.com/github/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/blob/main/PPPL_SULI-2024/ex2-free_boundary.ipynb)

2. On a **local installation of Python** that includes Jupyter notebook. (Advanced)

Some functionality, like interactive plots, may not work on Google Colaboratory. Instructions are included below for each option.


# Table of contents

1. [Running Examples on Google Colaboratory](#installation_google_colab)
2. [Running Examples on Jupyter Notebook Locally](#installation_anaconda)
3. [Tips on Using Jupyter Notebook](#jupyter_tips)

# Running Examples on Google Colaboratory <a name="installation_google_colab"></a>

## Opening the Notebooks

To open the notebooks on **Google Colab**, please open the links at the top of this README. 

## Running the Notebook

After opening each notebook, please execute the first two code cells by pressing "Shift + Enter" *twice* in order to install TokaMaker and required dependencies. After doing so, either click on the "Restart runtime" box in the output, or go to "Runtime" and select "Restart runtime":

![image](https://user-images.githubusercontent.com/32618747/162499118-ecdbe48d-06ed-49c7-9c76-ed0a8cc32255.png)

# Running Examples on Jupyter Notebook Locally (Jupyter required)
1. Download the .ipynb file for the notebook(s)

   The notebooks can be downloaded from GitHub at the following links or by checking out the [OpenFUSIONToolkit-Tutorials](https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials) repo.

   - [Example 1: Fixed-boundary Equilibria](https://raw.githubusercontent.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/main/PPPL_SULI-2024/ex1-fixed_boundary.ipynb)
   - [Example 2: Free-boundary Equilibria](https://raw.githubusercontent.com/OpenFUSIONToolkit/OpenFUSIONToolkit-Tutorials/main/PPPL_SULI-2024/ex2-free_boundary.ipynb)

2. Download and install [Open FUSION Toolkit](https://github.com/hansec/OpenFUSIONToolkit/releases/tag/v1.0.0-beta4) release for your platform

   Ensure `OFT_ROOTPATH` is set to a suitable value or the installation path is included in your `PYTHONPATH`.


# Tips on Using Jupyter Notebook <a name="jupyter_tips"></a>

- Select "Runtime>Run All" to run the entire notebook. 
- To run a single cell, select the cell with your mouse and then press "Shift+Enter"
- Create new cells using the "Insert" menu or the "+Code" button.
