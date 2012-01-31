crawlThis
=========

crawlThis was built on top of Twango and the below is true for crawlThis...
Take a look at the Twango project here. https://github.com/dagray/twango


Twango uses virtualenv and pip to facilitate easy and reliable setup of new projects
Some conventions used by twango that might not be obvious to those used to django:

To begin, Run 

  > source bootstrap.sh

This will set up your new virtual environment.  Once  
settings files are stored in the conf/ directory
and are loaded in alphabetical order. 

   g_generated_app_config.py is where new apps will automatically add configuration strings, its auto-generated, so you should probably avoid touching it if you can.

   a_base.py defines most of the basic settings that you will probably want int your project.  z_debug.py has the setting for turning debug mode on.  If you delete this file, it should disable debug mode.
