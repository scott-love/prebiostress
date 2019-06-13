# path to test subject
spath='/Volumes/data/prebiostress/data/sourcedata/nifti/sub-01/ses-1/dwi/'

cd $spath
# denoise LR
dwidenoise sub-01_ses-1_acq-lr_dwi.nii.gz sub-01_ses-1_acq-lr_dwi_dn.nii.gz -noise noise-lr.nii.gz -nthreads 12
# denoise RL
dwidenoise sub-01_ses-1_acq-rl_dwi.nii.gz sub-01_ses-1_acq-rl_dwi_dn.nii.gz -noise noise-rl.nii.gz -nthreads 12

# subtract denoised data from raw data and output as residuals
mrcalc sub-01_ses-1_acq-lr_dwi.nii.gz sub-01_ses-1_acq-lr_dwi_dn.nii.gz -subtract resid-lr.nii.gz
mrcalc sub-01_ses-1_acq-rl_dwi.nii.gz sub-01_ses-1_acq-rl_dwi_dn.nii.gz -subtract resid-rl.nii.gz

# remove Gibbs artifact
mrdegibbs sub-01_ses-1_acq-lr_dwi_dn.nii.gz sub-01_ses-1_acq-lr_dwi_dn_unr.nii.gz -axes 0,1 -nthreads 12
mrdegibbs sub-01_ses-1_acq-rl_dwi_dn.nii.gz sub-01_ses-1_acq-rl_dwi_dn_unr.nii.gz -axes 0,1 -nthreads 12

mrconvert sub-01_ses-1_acq-lr_dwi_dn_unr.nii.gz \
sub-01_ses-1_acq-lr_dwi_dn_unr.mif \
-fslgrad sub-01_ses-1_acq-lr_dwi.bvec sub-01_ses-1_acq-lr_dwi.bval \
-json_import sub-01_ses-1_acq-lr_dwi.json \
-datatype float32

mrconvert sub-01_ses-1_acq-rl_dwi_dn_unr.nii.gz \
sub-01_ses-1_acq-rl_dwi_dn_unr.mif \
-fslgrad sub-01_ses-1_acq-rl_dwi.bvec sub-01_ses-1_acq-rl_dwi.bval \
-json_import sub-01_ses-1_acq-rl_dwi.json \
-datatype float32

dwiextract sub-01_ses-1_acq-lr_dwi_dn_unr.mif - -bzero | mrmath - mean sub-01_ses-1_acq-lr_meanB0.mif -axis 3
dwiextract sub-01_ses-1_acq-rl_dwi_dn_unr.mif - -bzero | mrmath - mean sub-01_ses-1_acq-rl_meanB0.mif -axis 3


# test-sub24-ses1-imports
# dicom Version
mrcat \
/Volumes/data/prebiostress/data/sourcedata/dicom/timepoint1/OV2018RN1_A24_83503/CRANE_BREBIS_20180327_135159_796000/DWI_MB3_DIR64_RL_0003 \
/Volumes/data/prebiostress/data/sourcedata/dicom/timepoint1/OV2018RN1_A24_83503/CRANE_BREBIS_20180327_135159_796000/DWI_MB3_DIR64_LR_0009 \
all_dwis_dicom.mif \
-axis 3

mrconvert \
/Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-rl_dwi.nii.gz \
sub-24_ses-1_acq-rl_dwi.mif \
-fslgrad /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-rl_dwi.bvec /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-rl_dwi.bval \
-json_import /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-rl_dwi.json

mrconvert /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-lr_dwi.nii.gz \
sub-24_ses-1_acq-lr_dwi.mif \
-fslgrad /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-lr_dwi.bvec /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-lr_dwi.bval \
-json_import /Volumes/data/prebiostress/data/sourcedata/nifti/sub-24/ses-1/dwi/sub-24_ses-1_acq-lr_dwi.json

mrcat /Volumes/data/prebiostress/data/sourcedata/nifti/test-sub24-ses1-imports/sub-24_ses-1_acq-rl_dwi.mif \
/Volumes/data/prebiostress/data/sourcedata/nifti/test-sub24-ses1-imports/sub-24_ses-1_acq-lr_dwi.mif \
all_dwis_niiimport.mif \
-axis 3
