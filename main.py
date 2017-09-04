if __name__=="__main__":
    import sys, os, io, datetime, numpy as np, matplotlib.pyplot as plt, pandas as pd

    from file_methods import get_FilePaths, get_DataFrames, get_TestName,\
                get_LastExecuted, get_OnlyFname, get_SubDir, DisplayFiles,\
                CreateNewXLS, PutAllPngToPdf, WriteDataFrameToQDA

    from res2t import get_VoltageBiasStart_res2t, get_VoltageBiasFinal_res2t,\
                get_NumPointsBias_res2t, get_DrainCurrent_res2t

    from vgs_id import get_VoltageBias_vgs_id, get_GateVoltageStart_vgs_id,\
                get_GateVoltageFinal_vgs_id, get_NumGatePoints_vgs_id,\
                get_DrainCurrent_vgs_id, get_OnOffRatio_vgs_id

    from vds_id import get_VoltageBiasStart_vds_id, get_VoltageBiasFinal_vds_id,\
                get_VoltageBiasNumPoints_vds_id, get_GateVoltageStart_vds_id,\
                get_GateVoltageFinal_vds_id, get_NumGatePoints_vds_id,\
                get_GateVoltageStep_vds_id, generate_GateVoltageList_vds_id,\
                get_DrainCurrent_vds_id

    from plotting import plot_DrainCurrent_vgs_id, plot_AbsDrainCurrent_vgs_id,\
                plot_DualAxisDrainCurrent_vgs_id, plot_NormDrainCurrent_vgs_id,\
                plot_AllSubplots_vgs_id, plot_DrainCurrent_vds_id,\
                plot_AbsDrainCurrent_vds_id, plot_NormDrainCurrent_vds_id
    
    from cmd import CommandLineArgs

    width, plot_flag = CommandLineArgs(sys.argv) # get cmd line args  

    log = open('log.txt', 'w') # open the log file for writing
    log.write("*"*50)
    log.write("\n\n\tScript name: %s\n\n" % sys.argv[0])
    log.write("\n\tRun at %s\n\n" % datetime.datetime.now())
    log.write("*"*50)      
    
    # three possible types of measurements
    measurement_types = ['res2t#1@1', 'vgs-id#1@1', 'vds-id#1@1']

    file_extensions = ['.xls'] # file extensions wanted
    for ext in file_extensions: log.write("\n\n###--->\tSearching for %s \n\n" % ext)
   
    cwd = os.path.dirname(os.path.abspath(__file__)) # absolute path

    # get all the files in the current working directory
    # if any subdirs exist it will also return those
    full_file_paths = get_FilePaths(cwd, file_extensions)
    log.write("\n\n###--->\tGetting file list in path: %s\n" % cwd)

    DisplayFiles(full_file_paths, cwd, log) # display file results

    # loop over all the files found 
    for fobj in full_file_paths:

        if 'analyzed' in fobj: # skip any already analyzed files
            continue
    	else:
            log.write("###--->\tOpening %s\n\n" % fobj)
            curr_xls = pd.ExcelFile(fobj) # open excel file 
            log.write("###--->\tOpened %s\n\n" % fobj)

            log.write("###--->\tConverting %s\n to dataframes" % fobj)
            data, settings = get_DataFrames(curr_xls) # convert xls to data
        
            measurement_name = get_TestName(settings) # get measurement type        
            timestamp = get_LastExecuted(settings) # timestamp of measurement

            subdir = get_SubDir(fobj) # subdir of current file
            fname = get_OnlyFname(fobj) # file name of file only
            new_xls = subdir+fname+"-analyzed"+file_extensions[0] # new xls name

            if measurement_name == measurement_types[0]: # res2t
                get_DrainCurrent_res2t(data)

            if measurement_name == measurement_types[1]: # vgs-id#1@1
                bias = get_VoltageBias_vgs_id(settings) # get bias voltage 
                get_DrainCurrent_vgs_id(data, bias, width) # convert the data sheet

                if plot_flag == True:
                    # vgs-id plotting methods
                    log.write("\n###<---\tCreating plots of vgs_id\n\n")
                    plot_DrainCurrent_vgs_id(data, bias, subdir+fname)
                    plot_AbsDrainCurrent_vgs_id(data, bias, subdir+fname)
                    plot_NormDrainCurrent_vgs_id(data, bias, subdir+fname)

            if measurement_name == measurement_types[2]: # vds-id#1@1
                vbg_start = get_GateVoltageStart_vds_id(settings)
                vbg_final = get_GateVoltageFinal_vds_id(settings)
                vbg_step = get_GateVoltageStep_vds_id(settings)
                get_DrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, width)

                if plot_flag == True:
                    log.write("\n###<---\tCreating plots of vgs_id\n\n")
                    plot_DrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)
                    plot_AbsDrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)
                    plot_NormDrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)

            log.write("\n###<---\tWriting computed data from %s to %s\n\n" %(fobj,new_xls))
            CreateNewXLS(data, new_xls) # write new xls file
    
    log.write("*"*50)
    log.write("\n\n\tEnd\n\n")
    log.write("*"*50)
    log.close() # close the log file
    print "\n\n***\tSuccess!\t***\n"
