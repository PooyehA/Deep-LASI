
Workflow for analyzing Static 2c FRET Data
=====

.. _example:

The following section describes the workflow, when analyzing static, 2-color smFRET (single-molecule Förster Resonance Energy Tranfer) data, 
such as distance rulers based on double-stranded DNA labeled with two fluorophores. 

Deep-LASI provides a modular workflow for analysing the data, either manually or automatically. In the example below, we describe the workflow 
for two publicly available sample data sets published by from `Hellenkamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_
and `Götz et al., Nat. Meth (2022) <https://www.nature.com/articles/s41467-022-33023-3>`_. The examples start with localization and and trace extraction of fluorescent molecules between both channels, the categorization process, the determination of correction factors, the selection of time windows to be analyzed per single time trace, the kinetic analysis, and ends with a summary of the analyzed traces by calculating the distribution of the correction factors, the FRET and stoichiometry values.

Example Data
------------------
Static Double-Stranded DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first data set chosen in the multi-laboraory `benchmark study <https://www.nature.com/articles/s41592-018-0085-0>`_, enclode double-labeled DNA molecules. Two different samples with low (:numref:`Fig-DNA-2c-static` (left)) and intermediated FRET (:numref:`Fig-DNA-2c-static` (right)) were designed, where the attached fluorophore pairs are separated by 23 and 15 base pairs, respectively. 

.. image:: ./../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 800
   :alt: Static 2c DNA
   :align: center
   :name: Fig-DNA-2c-static
   
   Figure Caption 1. Double-Stranded DNA labeled with the donor dye Atto550 and acceptor dye Atto647N in 23 bp distance (left) and 15 bp separation (right).

Data set 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
