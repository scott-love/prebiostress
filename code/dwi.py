import os

spath='/Volumes/data/prebiostress/data/sourcedata/nifti/sub-01/ses-1/dwi/'

# concatonate the RL and LR runs
cmd ="mrcat " +spath +"sub-01_ses-1_acq-lr_dwi.nii.gz " +spath +"sub-01_ses-1_acq-rl_dwi.nii.gz " +spath +"concat.nii.gz"
os.system(cmd)
