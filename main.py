if __name__=="__main__":
    import os, io, numpy as np, matplotlib.pyplot as plt, pandas as pd

    from file_methods import get_FilePaths, get_DataFrames, get_TestName,\
                get_LastExecuted, get_OnlyFname, get_SubDir, DisplayFiles,\
                CreateNewXLS, PutAllPngToPdf

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
                

    # three possible types of measurements
    measurement_types = ['res2t#1@1', 'vgs-id#1@1', 'vds-id#1@1']

    file_extensions = ['.xls'] # file extensions wanted
    cwd = os.path.dirname(os.path.abspath(__file__)) # absolute path

    # get all the files in the current working directory
    # if any subdirs exist it will also return those
    full_file_paths = get_FilePaths(cwd, file_extensions)

    DisplayFiles(full_file_paths, cwd) # display file results

    # loop over all the files found 
    for fobj in full_file_paths:

        if 'analyzed' in fobj: # skip any already analyzed files
            continue
    	else:
            curr_xls = pd.ExcelFile(fobj) # open excel file 

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
                get_DrainCurrent_vgs_id(data, bias) # convert the data sheet

                # vgs-id plotting methods
                #plot_DrainCurrent_vgs_id(data, bias, subdir+fname)
                #plot_AbsDrainCurrent_vgs_id(data, bias, subdir+fname)
                #plot_NormDrainCurrent_vgs_id(data, bias, subdir+fname)
                #plot_AllSubplots_vgs_id(data)

            if measurement_name == measurement_types[2]: # vds-id#1@1
                vbg_start = get_GateVoltageStart_vds_id(settings)
                vbg_final = get_GateVoltageFinal_vds_id(settings)
                vbg_step = get_GateVoltageStep_vds_id(settings)
                get_DrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step)

                plot_DrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)
                plot_AbsDrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)
                plot_NormDrainCurrent_vds_id(data, vbg_start, vbg_final, vbg_step, subdir+fname)

            CreateNewXLS(data, new_xls) # write new xls file
    #PutAllPngToPdf(cwd)

