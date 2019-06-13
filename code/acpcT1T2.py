import os
import ants
import glob
import shutil
from bids.grabbids import BIDSLayout
import time
from joblib import Parallel, delayed
import multiprocessing

derivatives = '/Volumes/data/prebiostress/data/derivatives'
layout = BIDSLayout(derivatives) # ignore the error here

# do T1
for subj in layout.get_subjects(): # loop on number of subjects
    print(subj)
    for ses in layout.get_sessions(): # loop on number of sessions
        targ = os.path.join(derivatives,"sub-"+subj,"ses-"+ses,"anat") # find path to anat folder for this subject and this session
        fpaths = glob.glob(targ+"/*T1w_dn.nii.gz") # find the T1
        fpaths = ''.join(fpaths)
        if len(fpaths) > 0:
            img = ants.image_read(fpaths)

####### TESTING ############
img = ants.image_read('/Volumes/data/prebiostress/data/derivatives/sub-01/ses-1/anat/sub-01_ses-1_T1w_dn.nii.gz',reorient='LSP')
img = ants.image_read('/Volumes/data/prebiostress/data/derivatives/sub-01/ses-1/anat/sub-01_ses-1_T1w_dn.nii.gz')
img = ants.reorient_image2(img,orientation='LSP')
ants.image_write(img,'output.nii')
img.get_sessions()

img = ants.registration.reorient_image(img,orientation='LSP')

ants.image_write(img,'/Volumes/data/prebiostress/data/derivatives/sub-01/ses-1/anat/sub-01_ses-1_T1w_dn_lspPy.nii.gz')
help(ants.image_write)
help(ants.reorient_image2)
help(ants.apply_ants_transform_to_image)

help(ants.viz.plot)
ants.registration.reorient_image()
