import os
import ants
import glob
import shutil
import subprocess
from bids.grabbids import BIDSLayout

derivatives = "/Volumes/data/prebiostress/data/derivatives"
layout = BIDSLayout(derivatives) # ignore warning here

for t1targ in layout.get(modality="anat",session="4",type="T1w",return_type='file'):
    print(t1targ)


os.makedirs(os.path.dirname(t1targ)+"/brainmask",exist_ok="TRUE")
os.chdir(os.path.dirname(t1targ)+"/brainmask/")

copyt1targ = os.path.dirname(t1targ)+"/brainmask/"+os.path.basename(t1targ)
shutil.copy(t1targ,copyt1targ)

# pad the target image
cmd = (f"""ImageMath 3 {copyt1targ} PadImage {copyt1targ} 20""")
subprocess.call(cmd,shell=True)

cmd = (f"""antsJointLabelFusion.sh \
-d 3 \
-t {copyt1targ} \
-o {os.path.dirname(t1targ)+"/brainmask/"} \
-p {os.path.dirname(t1targ)+"/brainmask"+"/Posteriors%04.nii.gz"} \
-g /Volumes/data/slove/Dropbox/Kahina/A1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/A1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/A2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/A2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/B1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/B1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/B2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/B2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/C1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/C1_J1_T13D_PSR_brainMask.nii.gz \
-c 2 \
-j 5 \
> {os.path.dirname(t1targ)+"/brainmask/log.txt"}""")
subprocess.call(cmd,shell=True)

cmd = (f"""antsJointLabelFusion.sh \
-d 3 \
-t {copyt1targ} \
-o {os.path.dirname(t1targ)+"/brainmask/"} \
-p {os.path.dirname(t1targ)+"/brainmask"+"/Posteriors%04.nii.gz"} \
-g /Volumes/data/slove/Dropbox/Kahina/A1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/A1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/A2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/A2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/B1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/B1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/B2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/B2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/C1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/C1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/C2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/C2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/D1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/D1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/D2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/D2_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/E1_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/E1_J1_T13D_PSR_brainMask.nii.gz \
-g /Volumes/data/slove/Dropbox/Kahina/E2_J1_T13D_PSR.nii.gz -l /Volumes/data/slove/Dropbox/Kahina/E2_J1_T13D_PSR_brainMask.nii.gz \
-c 2 \
-j 5 \
> {os.path.dirname(t1targ)+"/brainmask/log.txt"}""")
    subprocess.call(cmd,shell=True)
