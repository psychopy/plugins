About PsychoPy Plugins
=====================================

History
----------

Up until PsychoPy version 2023.1.x PsychoPy was a single, increasingly large package, that tried to supply all the things a scientist might need. That began to get unwieldy as the number of components grew, each bringin its own dependencies, not all of which would be avaiable everywhere.


Why Plugins?
-------------

Moving to a plugin system brings several advantages:

- users can find the features they need more easily without being overwhelmed by all the things they don't personally use
- contributors can add new features with a greater degree of independence on the core PsychoPy team


Installing plugins
---------------------

To install plugins in PsychoPy:

* Select the `Tools` tab
* Select `Plugin/packages Manager` from the menu

.. figure:: /images/PluginsAndPackagesManager.png

* Find the plugin that you want and select `Install`

If you would like to install a plugin from a file (e.g. a .whl file):

* In `Plugin/packages Manager`, select the `Packages` tab
* At the bottom left of the window, select `Install from file` and choose the relevant file to install, or select `Open PIP Terminal` and run a PIP install

.. figure:: /images/PackagesTab.png

Installing plugins on an offline machine
------------------------------------------

If you need to use plugins on a machine that is not connected to the internet, follow these steps:

#. Identify which plugin you would like to install:
            * Go on PsychoPy on a machine that is connected to the internet
            * Click on the `Tools` tab and select `Plugin/packages Manager`
            * Find the relevant plugin from the list 
#. Download the wheel (.whl) file on a networked computer:
            * Visit `Pypi.org<Pypi.org>`_ and search for your selected plugin using the search bar
            * Download the wheel (.whl) file
#. Transfer the wheel (.whl) file to an external storage device (e.g. a memory stick)
#. Connect the external storage device to the non-networked computer 
#. Install the plugin from the wheel (.whl) file:
            * In PsychoPy (on the non-networked computer) click on the `Tools` tab and select `Plugin/packages Manager`
            * Select the `Packages` tab
            * In the lower left of the window, click `Install from file` and select the downloaded wheel (.whl) file
