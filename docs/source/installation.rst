Installation
=====

.. _installation:

Deep-LASI is a MATLAB program that uses neural networks for automated data analysis from Python libraries.
In order to use an automated data analysis make sure you installed the required software packages below.

System compatibility
------------

Deep-Lasi is compatible with Windows and Mac OS, and has been extensively tested on Mac OS systems. 
So far, we have not tested Deep-Lasi as extensively on Windows. If you encounter any problem, please
get in touch with us via the *Issue forum*.

Installation requirements for Mac
------------

.. image:: ./../figures/logos/mac.png
   :width: 50
   :alt: Mac OS Logo 

To run Deep-LASI on your local Mac OS please follow the 
installation process in the following order:

#. Install Python

#. Install Xcode

#. Install Matlab


*Python Installation*
--------

To run Deep-LASI on Mac OS, the following Python packages are required:

* Python 3.6.8
* numpy
* scipy
* pandas 
* Xcode
* tensorflow 2.8.0
* h5py

The following packages are useful and recommended for plotting results:

* matplotlib
* jupyterlab

The installation can either be done using an Xterm environment, or using an easier way by installing all dependencies using `Anaconda <https://www.anaconda.com/distribution/>`_.

.. note::
   Note: for new Macs using an M1 or M2 architecture, please make sure, that you use a *native* Python distribution. 
   You may want to use the command

   .. code-block:: python
   
      python3 -c "import platform; print(platform.machine())"

   to see your installed architecture. It should be ``arm64`` when using an M-series Mac.

#. Check your Python installation (make sure you have Python 3.6 or newer):

   .. code-block:: python
   
      python3 --version
      
   If this command does not yield any result, check whether python is already installed and troubleshoot your installation. Potentially, your ``$PATH`` environment variable is not properly set.

#. Update your installation via ``pip`` and install the optional dependencies by running the following commands:

   .. code-block:: python
   
      python3 -m pip install -U pip
      python3 -m pip install -U matplotlib jupyterlab
      python3 -m pip install -U Xcode h5py
      python3 -m pip install -U tensorflow==2.8.0'

Alternatively, you may install python via `Anaconda <https://www.anaconda.com/distribution/>`_ by replacing the commands above with:

   .. code-block:: python
   
      conda install --update-all pip matplotlib jupyterlab Xcode tensorflow==2.8.0' h5py
      
If this command leads to errors, please check whether python is already installed and troubleshoot your Anaconda installation. You may check whether your ``$PATH`` environment variable is properly set.


*MATLAB Installation*
--------

... more details are coming soon ... 

Installation requirements for Windows
------------
.. image:: ./../figures/logos/windows.png
   :width: 50
   :alt: Windows Logo

To run Deep-LASI on your local computer please follow the 
installation process in the following order:

#. Install Python

#. Install Microsoft Visual C++

#. Install MATLAB


... more details are coming soon ... 
