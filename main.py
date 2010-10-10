#-------------------------------------------------------------------------------
# Name:        Python-Facebook-Auto-Image-Uploader
# Purpose:
#
# Author:      Devon Badman
#
# Created:     10/10/2010
# Copyright:   (c) Devon Badman 2010
# Licence:      * This program is free software; you can redistribute it and/or modify
#               * it under the terms of the GNU General Public License as published by
#               * the Free Software Foundation; either version 2 of the License, or
#               * (at your option) any later version.
#               *
#               * This program is distributed in the hope that it will be useful, but
#               * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#               * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#               * for more details.
#               *
#               * You should have received a copy of the GNU General Public License along
#               * with this program; if not, write to the Free Software Foundation, Inc.,
#               * 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from time import clock, sleep, gmtime, strftime
import os, sys
import Image
import facebook
import time
import getopt
import mimetypes

# Hide the Warning displayed by facebook API
os.system("clear")

# Only files with the following mimetypes are uploaded
known_mimetypes_to_upload=["image/jpeg", "image/png", "image/gif"]

def function():
    if strftime("%H")==strftime("%M") and strftime("%H")==strftime("%S"):
        return "true"
    else:
        return "false"

def capture():
    from VideoCapture import Device
    cam = Device()
    im = cam.getImage()
    return im

def upload(file, time, timename, fb):
    file.save("%s.jpeg" % timename)
    #print "saved"
    fb.photos.upload("%s.jpeg" % timename,"pythonimages", time)

def waitLogin(fb):
        """ Wait the user to login. """
        session=None
        try:
                while not session:
                        try:
                                session = fb.auth.getSession()
                        except facebook.FacebookError:
                                time.sleep(3)   # Wait 3 seconds
        except KeyboardInterrupt:               # If the user press CTRL+C
                print "I was waiting for you to Login."
                raise


def Login():
    # Insert your appid and secretid here
    app_id=""
    app_sec=""

    # Create a facebook object
    fb = facebook.Facebook(app_id, app_sec)
    fb.auth.createToken()


    #Open the browser for user to login to facebook
    fb.login()

    # Wait until the user logs in
    waitLogin(fb)

    return fb



def main():
    fb = Login()
    while 1==1:
        if strftime("%H")==strftime("%M") and strftime("%H")==strftime("%S"):
            time=strftime("%H:%M:%S %d/%m/%y")
            timename=strftime("%H%M%S%d%m%y")
            file=capture()
            upload(file, time, timename, fb)

if __name__ == '__main__':
    main()