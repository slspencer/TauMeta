README2.txt
#
This file is part of the tau meta tau physica open source project
#
Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin
#
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. Attribution must be given in
all derived works.
#
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses>.
#


Troubleshooting:
1. Do not use reserved words as variable names:   as, id, if, in, is
2. If pattern encounters error, the  'Failed to load the requested file..." error message will appear.
    Inkscape will continue to open and show a blank document.
    Close Inkscape, and select 'Exit' when the TMTP menu reappears.
    Open a terminal, change to the tmtp/standalone directory.
    Run TMTP from the terminal:
              ./tmtp.sh
    Error messages will output to the terminal, and will contain the line number, function name, and file name where the error occurred.
    Most pattern functions are in the tmtp/standalone/pattern.py file.  Open this file ( recommended editor application: Eric editor ).
    Check syntax and values.  Feel free to insert print statements, but save to a backup file first (save to pattern.py.orig is good practice).
    To check the value of a point:
               print 'ad =', ad.x, ad.y, ad.name
    In some cases, there may be print statements which have been commented out.
    Uncomment these statements to see the values.  If anything prints with <   >  around some information about the object
    then, using the above example, you may have tried to print the object ad) instead of the attribute (ad.x):     print 'ad = ', ad

3. Sometimes strange results occur due to incorrect measurements.
    You can print out measurements in inches or centimeters.
   The measurements are stored in the client measurement .json file in either centimeters or inches, depending on which you prefer.
   The program reads this data into the CD object, converted to pixels. Convert the measurement back to centimeters or inches when printing.
   Example:
                print 'waist circumference =', CD.waist_circumference*CM
                print 'waist_circumference =', CD.waist_circumference*IN

4. Python does strange math.  Keep this in mind when you're programming a new pattern.
    All divisors should be float, not integer.
    Correct: 4/5.0
    Incorrect:  4/5, as python may return 0 integer value

5. To find a point in Inkscape you can look at the xml listing.
    Deselect everything in the pattern.
    Press ctrl-shift-x for the xml tree to appear.
    Click on the reference layer
    Scroll down until you find the variable name
    Highlight that variable name, and drag the xml dialog to the side
    The pattern piece, text, point or other object that your selected in the xml dialog should be selected in the svg canvas.
    To zoom in or out, press shift+ or shift-


Printing:
      Unwanted plotting behaviors occur depending on the linux/printer driver combination.
      Example: Some linux distributions don't pass the long paper length flag to certain plotter drivers, so output past 54" length is truncated.

Printing from Inkscape:
1. Select File/Document Properties.
      For Plotters:
              Enter roll width for roll paper plotters  - change dialog to use to inches or centimeters.
              Or select paper size for cut-sheet plotters.
      For Printers:
              Select paper size for your printer.
      Input border amounts recommended for the printer or plotter.
      Click on Resize Document.
      Rearrange pattern pieces if needed to fit on the paper size.  For plotters, the pieces can extend below bottom of page.
      Resize again & rearrange until all pieces fit on paper.
      For plotters, write down final document width & height.
2. Save as a PDF file. File will be saved to the customer's directory by default.
3. Select File/Print . The default printing dialog should appear.
      Choose the correct paper size, or input the document width and height.
      Click on Print.
If you can't print from Inkscape properly, try printing from GIMP.

Printing from GIMP:
  Open the PDF in GIMP & printing.
  Select File/Print. In the print dialog, try printing from each of the drivers listed and record which driver worked best.
  If this does not work, try printing directly from linux.

Printing from linux:
1.Right click on the PDF file from a linux file applications (like Nautilus). The print dialog will appear.
      Adjust paper size to match your notes. Select Print.

Printing from Adobe v10+ (requires v10+ for extra long paper size, etc.)
  1. Right click on the file from a linux file application. Select 'Open with' and select Adobe 10.
      Adjust paper size to match your notes. Print.

Printing from a 3rd party printing utility:
1. Download a 3rd party linux printing utility - I have not done this and have no recommendations.  Contact TMTP with your results.

If printing problems are unresolved:
 Write down the version of your operating system, the make & model of your printer or plotter, the paper size if it's unusual, and the printer driver version from your operating system.
1. File a bug with your linux distribution.
2. Contact the linux print working group.  They want to know about problems with linux printing.
3. Contact TMTP with problem & results so it can be included in documentation.


Contributing to Tau Meta Tau Physica:
  Tau Meta Tau Physica will be used a teaching tool for students in early adolescence.
  The code is written as simply as possible, which is why it is written in python.
  The math functions use the lowest level of complexity required to get the job done.
  The teaching code will eventually be on its own branch, and
  lib2geom will be used for curve calculations in the public branch.
  The code can be converted from python to C++ at that time.
