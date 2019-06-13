import os
import glob
import shutil
from bids.grabbids import BIDSLayout

niftipath = '/Volumes/data/prebiostress/data/sourcedata/nifti'
derivatives = "/Volumes/data/prebiostress/data/derivatives"

layout = BIDSLayout(niftipath)

# do T1
for subj in layout.get_subjects(): # loop on number of subjects
    for ses in layout.get_sessions(): # loop on number of sessions
        targ = os.path.join(niftipath,"sub-"+subj,"ses-"+ses,"anat") # find path to anat folder for this subject and this session
        fpaths = glob.glob(targ+"/*T1w.nii.gz") # find all T1s
        outpath = os.path.join(derivatives,"sub-"+subj,"ses-"+ses,"anat")
        outpath = outpath+"/sub-"+subj+"_ses-"+ses+"_T1w.nii.gz"
        nT1s = len(fpaths)
        if nT1s > 1: # check there is more than one image to average
            # average all the T1s found
            cmd = "AverageImages 3 " +outpath + " 0 " +" ".join(fpaths)
            os.system(cmd)
        elif nT1s == 1: # if there was only 1 image then copy it to derivatives
            shutil.copy(" ".join(fpaths),outpath)
# Manual check of all averages:
# sub-01_ses-1, ses-2, ses-3, ses-4
# sub-02_ses-1, ses-2, ses-3***NOT GOOD***, ses-4
# sub-03_ses-*** NOT THE BEST - run 1 might be best***, ses-2, ses-3, ses-4
# sub-04_ses-1, ses-2, ses-3, ses-none
# sub-05_ses-1, ses-2, ses-3, ses-4
# sub-06_ses-1, ses-2, ses-3, ses-4
# sub-07_ses-1, ses-2, ses-3, ses-4
# sub-08_ses-1, ses-2, ses-3, ses-4
# sub-09_ses-1, ses-NONE, ses-3, ses-4
# sub-10_ses-1, ses-2, ses-3, ses-4
# sub-11_ses-1, ses-2, ses-3, ses-4
# sub-12_ses-1, ses-2**ODD**, ses-3, ses-4
# sub-13_ses-1, ses-2, ses-3, ses-4
# sub-14_ses-1, ses-2, ses-3, ses-4
# sub-15_ses-1, ses-2, ses-3, ses-4
# sub-16_ses-1, ses-2, ses-3, ses-4
# sub-17_ses-1, ses-2, ses-3, ses-4
# sub-18_ses-1, ses-2, ses-3, ses-4
# sub-19_ses-1, ses-2, ses-3, ses-none
# sub-20_ses-1, ses-2, ses-3, ses-none
# sub-21_ses-1, ses-2, ses-3, ses-4
# sub-22_ses-1, ses-2, ses-3, ses-4
# sub-23_ses-1, ses-2, ses-3, ses-4
# sub-24_ses-1, ses-2, ses-none, ses-none

# do T2
for subj in layout.get_subjects(): # loop on number of subjects
    for ses in layout.get_sessions(): # loop on number of sessions
        targ = os.path.join(niftipath,"sub-"+subj,"ses-"+ses,"anat") # find path to anat folder for this subject and this session
        fpaths = glob.glob(targ+"/*T2w.nii.gz") # find all T2s
        outpath = os.path.join(derivatives,"sub-"+subj,"ses-"+ses,"anat")
        outpath = outpath+"/sub-"+subj+"_ses-"+ses+"_T2w.nii.gz"
        nT2s = len(fpaths)
        if nT2s > 1: # check there is more than one image to average
            # average all the T1s found
            cmd = "AverageImages 3 " +outpath + " 0 " +" ".join(fpaths)
            os.system(cmd)
        elif nT1s == 1: # if there was only 1 image then copy it to derivatives
            shutil.copy(" ".join(fpaths),outpath)
# Manual check of all averages:
# sub-01_ses-1, ses-2, ses-3, ses-4
# sub-02_ses-1, ses-2, ses-3, ses-4
