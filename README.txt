Pipeline:


Limitations / Problems:

README.txt files inside the sourcedata/dicom/<SUBJECT>/CRANE... directories outline problems
and associated changes to the protocol for that subject.

** time-point 1 **
For time-point 1 and subjects 01, 02, 03 T1w images were acquired in the Sagittal
plane. However, in an attempt to remove potential flow artifacts it was decided
to change to a Coronal plane. The decision to change to Coronal was made during
the acquisition of sub-04. For sub-04 we have 2 Coronal T1w images but both are
1NEX. From sub-05 we acquire one at 1NEX and one at 2NEX in Coronal. Unless
artifacts were detected, then a replacement was acquired.

It is possible that there was more head motion for lambs at 1 week than at other
time-points. The motion was due to respiration and thus included very small
repetitive movements. This type of motion existed at all time-points however
it was faster and arguably more noticeable at 1 week. Although this observation
is totally subjective.

** time-point 2 **
For time-point 1 MRI was performed using a custom built 24-channel coil.
However, due to a fault that developed in this coil we had to change to the
Siemens 4-channel Flex Coil (large) for time-points 2, 3 & 4.
A01_P02, A02_P02, A03_P02, A04_P02, A05_P02, A06_P02 were done with the 24-chan
however we re-ran these subjects (AXX_P02B) later with the Flex coil. The DWI, T1w and T2w
data from these sessions are not being used.
Note that we acquired some resting state data for A02_P02 and A04_P02. This data
is not part of this project, it was only collected to test resting state acquisitions
but the data should still be useable. This data can be found in sourcedata/dicom/timepoint2NOTUSING

** time-point 3 **
For sub-02_ses-3 there was a power cut during acquisition. There is no T1_2NEX. Also the quality of 
the run-1 T1 is not good. The only T1 used was run-2. It was also necessary to do a Rigid registration 
between the T1 and T2 rather than just a reslice-identity.

Changed number of slices from 54 to 57 for DWI?????

** time-point 4 **
No data for sub-04, sub-19, sub-20, sub-24.