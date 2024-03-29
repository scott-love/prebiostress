import os
import json
import fnmatch
import glob

tp="2" # number of the timepoint to organise?

### Defining and creating paths ###
toplvl = "/Volumes/data/prebiostress/data"
dcmdir = "/Volumes/data/prebiostress/data/sourcedata/dicom/timepoint"+tp
dcm2niidir = "/Applications/mri/MRIcroGL"

#Create nifti directory
niidir = toplvl + "/sourcedata/nifti"
os.makedirs(niidir,exist_ok=True)

# define function that lists all files except hidden files
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# create subject file structure
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    os.makedirs(niidir+"/sub-"+subj[1:]+"/ses-"+tp+"/anat",exist_ok=True)
    os.makedirs(niidir+"/sub-"+subj[1:]+"/ses-"+tp+"/dwi",exist_ok=True)
    os.makedirs(niidir+"/sub-"+subj[1:]+"/ses-"+tp+"/func",exist_ok=True)

    os.makedirs(toplvl+"/derivatives/sub-"+subj[1:]+"/ses-"+tp+"/anat",exist_ok=True)
    os.makedirs(toplvl+"/derivatives/sub-"+subj[1:]+"/ses-"+tp+"/dwi",exist_ok=True)
    os.makedirs(toplvl+"/derivatives/sub-"+subj[1:]+"/ses-"+tp+"/func",exist_ok=True)

### Anatomicals ###
# *****************************************************************************
# The result of the code below for SPC1 (run-1) were removed for subj-07 due to
# bad artifact. There is a run-2 and run-3 T2w. 
# *****************************************************************************

#MPR1
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T1_MPR1*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-1_T1w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

#MPR2
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T1_MPR2*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-2_T1w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

#MPR3 - only a few subjects have a third T1!
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T1_MPR3*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-3_T1w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

#SPC1
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T2_SPC1*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-1_T2w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

#SPC2
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T2_SPC2*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-2_T2w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

#SPC3 - only a few subjects have a third T2!
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/T2_SPC3*')
    datadir = ''.join(datadir[0:1])
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_run-3_T2w " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/anat " +datadir
    print(cmd)
    os.system(cmd)

### DWI ###
#RL
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/DWI_MB3_DIR64_RL_0*')
    datadir = ''.join(datadir)
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_acq-rl_dwi " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/dwi " +datadir
    print(cmd)
    os.system(cmd)
#LR
for fname in listdir_nohidden(dcmdir):
    subj = fname.split("_")[-3].split("_")[0]

    datadir = glob.glob(dcmdir+'/'+fname+'/*/DWI_MB3_DIR64_LR_0*')
    datadir = ''.join(datadir)
    cmd = "dcm2niix -z y -f sub-" +subj[1:] +"_ses-" +tp +"_acq-lr_dwi " \
        "-o " +niidir +"/sub-" +subj[1:] +"/ses-" +tp +"/dwi " +datadir
    print(cmd)
    os.system(cmd)
