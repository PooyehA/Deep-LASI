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
Please install Python with version 3.7-3.10 at "https://www.python.org/downloads/.
After installation you can check the MATLAB integration by typing the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
If no version or path information is shown, link the Python executable directy by typing: 
   .. code-block:: python
      pyversion 'your/path/to/python/python.exe'

      
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
