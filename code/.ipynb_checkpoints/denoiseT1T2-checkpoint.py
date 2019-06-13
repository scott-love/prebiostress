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
        fpaths = glob.glob(targ+"/*T1w.nii.gz") # find the T1
        fpaths = ''.join(fpaths)
        if len(fpaths) > 0:
            img = ants.image_read(fpaths)
            mask  = ants.get_mask(img)
            dn = ants.denoise_image(img,mask,noise_model='Gaussian')
            ants.image_write(dn,fpaths[0:-7]+'_dn.nii.gz',)

# do T2
def runeachsess(subj,ses):
        targ = os.path.join(derivatives,"sub-"+subj,"ses-"+ses,"anat") # find path to anat folder for this subject and this session
        fpaths = glob.glob(targ+"/*T2w.nii.gz") # find the T1
        fpaths = ''.join(fpaths)
        if len(fpaths) > 0:
            img = ants.image_read(fpaths)
            mask  = ants.get_mask(img)
            dn = ants.denoise_image(img,mask,noise_model='Rician')
            ants.image_write(dn,fpaths[0:-7]+'_dn.nii.gz',)

for subj in layout.get_subjects():
    Parallel(n_jobs=2)(delayed(runeachsess)(subj,ses)for ses in layout.get_sessions()) # loop on number of subjects
