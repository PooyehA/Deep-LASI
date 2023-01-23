Installation
=====

.. _installation:

Deep-LASI is a MATLAB program that uses deep learning for automated data analysis from Python libraries.
In order to use the automated data analysis with the pretrained deep neural networks make sure you installed the required software packages below.

System compatibility
------------

Deep-Lasi is compatible with Windows and Mac OS. It has been extensively tested for Mac OS x86 systems. For new Macs using the M1 or M2 CPUs, the deep learning features are not available until MathWorks releases a native MATLAB version for the M1 and M2 architectures.
Deep-LASI has not been installed on a Linux systems so far. If you encounter any problem, please
get in touch with us via the *Issue forum*.

*MATLAB Installation*
--------

... more details are coming soon ... 


Installation requirements for Mac
------------

.. image:: ./../figures/logos/mac.png
   :width: 50
   :alt: Mac OS Logo 

To run Deep-LASI on Mac OS, the following software packages are required:

* Python 3.7-3.10 (check https://de.mathworks.com/support/requirements/python-compatibility.html for MATLAB version compatibility)
* Xcode
* TensorFlow 2.8.0 (Python package)


Python installation for Mac
------------
Please install Python with version 3.7-3.10 at <a href="https://www.python.org/downloads/">download and install Python</a>. <a href="https://de.mathworks.com/support/requirements/python-compatibility.html">View this table</a> for compatibility of your MATLAB with Python versions.', newline, ...
            'After installation check the integration by typing "pyversion" into the MATLAB Command Window. ', ...
            'If no version or path information is shown, link the Python executable directy by typing: pyversion ''your/path/to/python/python.exe'' , ', newline, ...
            'For the following Python packages to work correctly please download and install Xcode (available in the App Store)', newline, ...
            'If successful, install the Python packages Tensorflow and h5py:', newline, ...
            'Open your Mac OS Terminal and enter: pip install tensorflow==2.8.0', newline, ...
            'Done!'
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
