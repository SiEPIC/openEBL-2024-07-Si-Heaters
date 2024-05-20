
# openEBL Design Submissions

- The Canadian Silicon Photonics Foundry, <a href="https://siepic.ca/fabrication/">SiEPICfab</a>, presents the open electron beam lithography (EBL) fabrication process, where former and current students of <a href="https://siepic.ca/education/">SiEPIC</a> workshops and courses can submit their design for manufacturing and testing.
- More details about <a href="https://siepic.ca/openEBL/">openEBL</a>.
- The previous submission was in [February 2024](https://github.com/SiEPIC/openEBL-2024-02-Si-Heaters).
- **Submission deadline: July 14, 2024**
- The previous submission was in [February 2024](https://github.com/SiEPIC/openEBL-2024-02-Si-Heaters). You can look at this previous designs for inspiration.

# Fabrication process: Passive Silicon + Heaters
## Technical summary:
- SOI wafer, 220 nm silicon
- Baseline process:
  - Single full etch, using a negative resist (HSQ)
  - Oxide cladding
  - TiW metal heater, and Au metal bond pads
- Details: [Slides](https://docs.google.com/presentation/d/1_ppHYec6LydML4RMRJdNI4DXHb0hgW7znToQCGgSF6M)
- Process Design Kit: [SiEPIC-EBeam-PDK](https://github.com/siepic/SiEPIC_EBeam_PDK) 

## Layer table
| Name            | Layer/datatype | Description                                                                          |
|-----------------|----------------|--------------------------------------------------------------------------------------|
| Si  | 1/99 | Layer to draw silicon geometries |
| M1_heater  | 11/0 | Layer to draw metal heater, TiW |
| M2_router  | 12/0 | Layer to draw metal routing, Au |
| Floorplan | 99/0 | Marks the layout design area |
| Text | 10/0 | Text labels for automated measurements |
| DevRec | 68/0 | Device recognition layer for component connectivity, netlist extraction, and verification|
| PinRec  | 1/10  | Port/pins recognition layer for component connectivity, netlist extraction, and verification|
| Waveguide | 1/99 | Virtual layer, guiding shape for waveguides |
| SEM | 200/0 | Requests for SEM images. Rectangles in a 4:3 aspect |


# Submission instructions:

The submission involves several steps. First, you need to create your design(s) using the process design kit (PDK) for this specific fabrication run. Then you need to create a Fork of this repository, commit your design(s), ensure that it passes the checks, and create a pull request. Once your pull request is approved, your design(s) will be merged into the layout for fabrication. You should verify that your design is correctly merged. Once the designs are fabricated, they will be tested, and the measurement results will be posted in this repository.

## Design software and PDK installation instructions:
 - Design tools and process design kit (SiEPIC-EBeam-PDK, KLayout implementation)<a href="https://github.com/siepic/SiEPIC_EBeam_PDK/wiki/Installation-instructions">installation instructions</a>. 
 - Automated measurement test routine is submitted as a YAML file that is created using the following utility:
 
pip install dreamcreator
from dreamcreator import sequencecreator as sc
sc.launch()

## Submission via GitHub
 
 - [Watch this video for a demonstration](https://kaltura.clemson.edu/media/t/1_iwysnxub)
 - Create an account on GitHub
 - Fork a copy of this GitHub repository into your own account:  <a href="../../fork">Create a new fork</a> 
 - Turn on the GitHub Actions on your forked repository: <a href="../../actions">Actions</a> (In your repository's page on GitHub, click on Actions in the top-menu bar, and Enable the workflows).
 - [Optional] Install GitHub Desktop (or git) on your computer, and Clone a local copy: <a href="x-github-client://openRepo/https://github.com/SiEPIC/openEBL-2024-07-Si-Heaters">Open with GitHub Desktop</a>
 - Create your design, and ensure that the filename contains your <a href="https://www.edx.org/learn/engineering/university-of-british-columbia-silicon-photonics-design-fabrication-and-data-ana">edX.org</a> username, and be formatted according to the course/workshop as follows:
   - EBeam_username.oas: for the <a href="https://www.edx.org/learn/engineering/university-of-british-columbia-silicon-photonics-design-fabrication-and-data-ana">edX Phot1x silicon photonics design course</a>
   - ELEC413_username.oas: for the <a href="https://ece.ubc.ca/courses/elec-413/">UBC ELEC 413 course</a>
   - SiEPIC_username.oas: for the <a href="https://www.cmc.ca/passive-silicon-photonics-fabrication-workshop-2023">CMC SiEPIC Passives silicon photonics workshop</a>
   - SiEPIC_username.oas: for the <a href="https://www.cmc.ca/active-silicon-photonics-fabrication-workshop-2024">CMC SiEPIC Actives silicon photonics workshop</a>
   - For example: EBeam_LukasChrostowski_rings.oas
 - Create your YAML test routines file, following the same filename requirements as above, but ending with extension .yaml.
 - Ensure that your fork is up to date with the main SiEPIC repository.  Click "Sync fork" <img width="671" alt="image" src="https://github.com/SiEPIC/openEBL-2024-05/assets/15843200/256c87dc-dd68-4606-8529-6c7f6ecf41fa">
 - Upload your design(s) into the "submissions" folder, as a binary file, namely a .gds (GDSII format) or .oas (OASIS format) file, and the YAML test routine file.
    - This can be done via the GitHub web page, by navigating to the <a href=../../tree/main/submissions>submissions folder</a>, then clicking on Add file, and Upload files. 
    - Click Commit changes, and wait for the verification to complete
    - If there are errors, please review and correct the errors
 -  Look for errors -- "All checks have failed" <img width="864" alt="image" src="https://github.com/SiEPIC/openEBL-2024-05/assets/15843200/d5689514-eca0-423f-9288-b20ec4fdd5e9">
    - Click on Details
    - In the main, window expand the "Run layout verification"; see if there is a text description of the problem
    - Look for the Artifact file; download it and open it in KLayout
  - After fixing the errors, you should have a green check mark as follows: <img width="488" alt="image" src="https://github.com/SiEPIC/openEBL-2024-05/assets/15843200/4c502cc4-16c1-4115-8ad7-7d5fdfe715d3">   
 - Alternatively upload your Python file, which will be compiled by a GitHub Action.  
   - For KLayout designs, use the "submissions/KLayout Python" folder, namely a .py (Python format) file.  e.g., EBeam_LukasChrostowski_MZI.py.  The Python file should save a gds or oas file into the parent "submissions" folder. The Python script needs to be executable in non-GUI mode, namely using "import klayout SiEPIC SiEPIC-EBeam-PDK"
 - Check below for the merged design, and ensure that your design is correctly included
 - Create a <a href="https://help.github.com/articles/using-pull-requests/">Pull Request</a> -- this will notify the team of your contribution, which we can aggregate into the main design file
 - Return to the main repository, and check for the merged design

<img width="1281" alt="image" src="https://github.com/SiEPIC/openEBL-2024-02/assets/15843200/e4785a27-b971-4a64-8796-1e351f30c00e">

## Black-box cells (IP Replacement)
- We perform IP replacement on several cells (grating couplers). We call these cells Black Box (BB), and you can identify them by _BB in the cell name, or the presence of the Blackbox layer 998/0 in the cell.
- You must not change the name of the cell, the contents, nor cell origins. Otherwise, the replacement will not work correctly.

## FYI – Automated GitHub Actions
The verification and merging is performed using GitHub actions. The repository implements the following:

1) Running the files in the "submissions/KLayout Python" folder, to generate the designs
2) Performing Manufacturing DRC verification on the designs in the "submissions" folder, and outputing the errors as an Artifact
3) Performing Functional verification on the designs in the "submissions" folder, and outputing the errors as an Artifact
4) Merging the designs from the "submissions" folder, and outputing merged layout as an Artifact

## Latest Merge Layout File

<!-- start-link -->
https://github.com/SiEPIC/openEBL-2024-07-Si-Heaters/actions/runs/9153712478/artifacts/1518056652
<!-- end-link -->
