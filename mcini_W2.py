#CAOS EFU Model Parameter File
#timing and files

wd='.'                      #working_directory
precf='irr_testcase.dat'    #top_boundary_flux_precip
etf='etp.dat'               #top_boundary_flux_etp
inimf='moist_testcase.dat'  #initial_moisture
outdir='out'                #output_directory [not used while testing]
t_end=864                   #end_time[s] [not used while testing]
part_sizefac=50             #particle_sized_definition_factor
grid_sizefac=0.005          #grid_size_definition_factor [m]
subsfac=10                  #subsampling_rate [percent] [deprecated]
macscalefac=100             #scaling factor converting macropore space and particle size 
t_dini=5.                   #initial_time_step[s]
t_dmx=12.                   #maximal_time_step[s]
t_dmn=0.01                  #minimal_time_step[s]
refarea=1.                  #reference_area_of_obs[m2]
soildepth=-1.2              #depth_of_soil_column[m]
smooth=(6,6)                #smoothing window for thS calculations as no. of cells

#macropore 
macbf='macbase_H.dat'         #macropore definition file
macimg='mac_imW2.dat'         #macropore image list file
nomac=False                 #switch of macropores

#bromid tracer data
tracerbf='brprofileVI.dat'       #tracer base file
tracer_t_ex=1800.0          #time to excavation   
tracer_horgrid=0.05          #gridspacing horizontally   
tracer_vertgrid=0.05         #gridspacing vertically

tracer_site=97              #site ID of sprinkler experiment
tracer_CI=25.43             #
tracer_SD_CI=2.1            #
tracer_appl_Br=4.19595      #applied mass of bromide
tracer_SD_Br=0.3465         #
tracer_time=2.3             #
tracer_intensity=11.05652174#
tracer_c_br=0.165           #

#soil matrix properties
matrixbf='matrix.dat'       #matrix base file
matrixdeffi='matrixdef_W2.dat' #matrix definition file

#resolution BB stain image
stain_res=0.0005             #[m/px] 1px = 0.5mm
