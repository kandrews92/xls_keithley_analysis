def get_FilePaths(directory, extension=['']):
    """
    /*-----------------------------------------------------*/
    description:
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
    /*-----------------------------------------------------*/
    args: 
        directory: current path that is to be searched
        extension(s): specific file extension to be found.
                    defaults to empty, which will give all files
                    found in tree
    returns:
        file_paths: list of strings with each absolute path
    /*----------------------------------------------------*/
    """
    import os 
    file_paths = [] # init of list of strings to be returned

    # walk the tree
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath 
            filepath = os.path.join(root, filename)
            # check the filepath's extension, if wanted then add to list
            # if arg:extension is blank, then all files found in tree
            # will be added
            for ext in extension:
                if filepath.lower().endswith(ext) and 'analyzed' not in filepath:
                    file_paths.append(filepath) # add it to the list.
    return file_paths # self-explanatory

def get_DataFrames(xls_file):
    """
    /*-----------------------------------------------------*/
    description:
    	This function takes an instance of a pandas excel 
    	file (ex: xls = pd.ExcelFile(filename) ) and returns
    	two data frames from it. 
    	This function is specific to the settings for the 
    	keithley s4200 writing structure. 
    	The xls file has, by default, three sheets.
    	1. Data (contains all the measurement data)
    	2. Calc (blank and is skipped by default)
    	3. Settings (contains the measurement settings)
    /*-----------------------------------------------------*/
    args: 
        xls_file: an instance of pd.ExcelFile(filename)
    returns:
        data frames for each individual shet
    /*----------------------------------------------------*/
    """
    df0 = xls_file.parse(xls_file.sheet_names[0])
    df2 = xls_file.parse(xls_file.sheet_names[2])
    return df0, df2

def get_TestName(settings_dataframe):
    """
    /*-----------------------------------------------------*/
    description:
        The function gets the headers from the xls settings
        and returns the measurement type from the settings
        file.
    /*-----------------------------------------------------*/
    args: 
        settings_dataframe: data frame containing the 
        measurement settings from xls file.
    returns:
        a string containing the measurement type. The 
        options are:
            -'vgs-id#1@1'
            -'vds-id#1@1'
            -'res2t#1@1'
    /*----------------------------------------------------*/
    """
    return list(settings_dataframe)[1]

def get_LastExecuted(df):
    """
    /*-----------------------------------------------------*/
    description:
        Get the timestamp of the measurement from the 
        settings xls sheet / dataframe. 
        Because of the setup of the xls sheet named:
        'settings' this function searches the first column
        of the sheet (e.g. list(df)[0] ) and finds the 
        index of the phrase 'Last Executed' and uses that 
        index to return the measurement type string.
    /*-----------------------------------------------------*/
    args: 
        df: dataframe to be searched
    returns:
        a string containing the measurement type. The 
        options are:
            -'vgs-id#1@1'
            -'vds-id#1@1'
            -'res2t#1@1'
    /*----------------------------------------------------*/
    """
    headers = list(df) # len = 4
    # ['Test Name', 'Measurement Type', 'Unnamed: 2', 'Unnamed: 3']
    # loop over the data frame's first column
    for i in range(len(df[headers[0]])):
        if df[headers[0]][i] == 'Last Executed': # search for time
            last_exec_idx = i # store index 
    return df[headers[1]][last_exec_idx]

def get_OnlyFname(fobj):
    """
    /*----------------------------------------------------*/
    description:
        returns the file name only, without absolute path
    /*----------------------------------------------------*/
    args:
        fobj: a file name with absolute path included

    returns:
        string with file name 
    /*----------------------------------------------------*/     
    """
    left_index = fobj.rfind("\\") # find the split for the last dir in path
    right_index = fobj.rfind(".") # find the split for file ext
    return fobj[left_index+1:right_index]

def get_SubDir(fobj, delimiter="\\"):
    """
    /*----------------------------------------------------*/
    description:
        returns the subdir of fobj with absolute path of 
        type string
    /*----------------------------------------------------*/
    args:
        fobj: a file name with absolute path included
        delimiter: character to break at. default value 
        is '\' (\\ = \ in python)

    returns:
        string with file name and file extension stripped 
        but last slash still remains
    /*----------------------------------------------------*/     
    """
    index = fobj.rfind(delimiter)
    return fobj[:index+1]

def DisplayFiles(file_list, currpath, log):
    """
    /*-----------------------------------------------------*/
    description:
        This function will prints the files found using the 
        function get_filepaths in ordered method
    /*-----------------------------------------------------*/
    args: 
        file_list: a list of strings containing absolute
                    paths.
        mypath: the current top path that the script is run 
                from
        log: file for output to be written to
    returns:
        None
    /*----------------------------------------------------*/
    """
    # count the number of files found in tree
    log.write("\n###--->\tFound %d files in %s\n" %(len(file_list), currpath))
    # loop and print the files found in sucessive order
    # and account for python's zero-indexing when outputting
    # the list. 
    for i in range(len(file_list)):
        log.write("\n###--->\t[%d] %s\n\n" %((i+1), file_list[i]))
    log.write("\n")

def CreateNewXLS(df, new_fame):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:
        
    /*----------------------------------------------------*/
    """
    import pandas as pd 
    writer = pd.ExcelWriter(new_fame) # open new xls to write df
    df.to_excel(writer, index=False) # write w/o indicies
    writer.save() # save file under new name

def CommandLineArgs(args):
    """
    /*-----------------------------------------------------*/
    description:
        Parse the command line arguments if any.
        Width = 1 and plot_flag are initially set to their
        default values
    /*-----------------------------------------------------*/
    args: 
        args: command line args passed from running python
                file
    returns:
        width: a floating point value if it exists
        plot_flag: boolean
    /*----------------------------------------------------*/
    """
    width = 1
    plot_flag = False
    if len(args) > 1:
        for val in args:
            try:
                width = float(val)
            except ValueError:
                if val == 'plot':
                    plot_flag = True
    return width, plot_flag

def plot_DrainCurrent_vgs_id(df, bias, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt
    plt.clf() # clear any figs in buffer
    headers = list(df) # get column headers
    for i in range( len(headers) ):
        if 'Idrain(uA)' in headers[i]:
            idx = i # store drainI idx

    plt.plot(df['GateV'], df[headers[idx]], linewidth=4, label=r'$V_\mathrm{ds}=$'+str(bias)+r'$\,\mathrm{V}$')

    # check whether labels should be > 0 or < 0
    if df['DrainI'].iloc[-1] > 0:
        plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=22)
    else:
        plt.ylabel(r'$-I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=22)
    plt.xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=22)

    plt.tick_params(labelsize=18) # make label size = 18
    plt.legend(loc='best') # set legend location
    plt.tight_layout() # tighten border edges

    savename = savename + '_python_linear-plot.png'
    plt.savefig( savename ) # save as png

def plot_AbsDrainCurrent_vgs_id(df, bias, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt
    plt.clf() # clear any figs in buffer
    headers = list(df) # get column headers
    for i in range( len(headers) ):
        if 'abs(DrainI(A))' in headers[i]:
            idx = i # store index of absDrainI
    # plot semilog y-axis
    plt.semilogy(df['GateV'], df[headers[idx]], linewidth=4, label=r'$V_\mathrm{ds}=$'+str(bias)+r'$\mathrm{V}$')

    plt.ylabel(r'$\left|I_\mathrm{ds}\right|\,(\mathrm{A})$', fontsize=18)
    plt.xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=18)

    plt.tick_params(labelsize=18) # set labels to size = 18
    plt.legend(loc='best') # set legend location
    plt.tight_layout() # tighten border edges

    savename = savename + '_python_logY-plot.png'
    plt.savefig( savename ) # save as png

def plot_DualAxisDrainCurrent_vgs_id(df, bias, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    #plt.clf()
    headers = list(df)
    for i in range( len(headers) ):
        if 'abs(DrainI(A))' in headers[i]:
            abs_idx = i 
        if 'Idrain(uA)' in headers[i]:
            ids_idx = i 
    fig, ax1 = plt.subplots()
    ax1.plot( df['GateV'], df[headers[ids_idx]], 'r', linewidth=4)
    ax1.set_xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=18)
    ax1.set_ylabel(r'$-I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=18)
    ax2 = ax1.twinx()
    ax2.semilogy( df['GateV'], df[headers[abs_idx]], 'k', linewidth=4)
    ax2.set_ylabel(r'$\left|I_\mathrm{ds}\right|\,(\mathrm{A})$', fontsize=18)
    plt.show()

def plot_NormDrainCurrent_vgs_id(df, bias, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt
    plt.clf() # clear any figs in buffer
    headers = list(df) # column headers as list
    for i in range( len(headers) ):
        if 'Idrain(uA/um)' in headers[i]:
            norm_idx = i # store idx of normIds

    plt.plot( df['GateV'], df[headers[norm_idx]], linewidth=4, label=r'$V_\mathrm{ds}=$'+str(bias)+r'$\,\mathrm{V}$')

    # check whether labels should be > 0 or < 0
    if df['DrainI'].iloc[-1] > 0:
        plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A}/\mu\mathrm{m})$', fontsize=22)
    else:
        plt.ylabel(r'$-I_\mathrm{ds}\,(\mu\mathrm{A}/\mu\mathrm{m})$', fontsize=22)
    plt.xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=22)

    plt.tick_params(labelsize=18) # make label size = 18
    plt.legend(loc='best') # set legend location
    plt.tight_layout() # tighten border edges

    savename= savename + "_python_norm-linear-plot.png" # plot will be saved as png
    plt.savefig( savename ) # save as png

def plot_AllSubplots_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    
    headers = list(df) # column headers as list
    for i in range( len(headers) ):
        if 'Idrain(uA)' in headers[i]:
            ids_idx = i
        if 'abs(DrainI(A))' in headers[i]:
            abs_idx = i
        if 'Idrain(uA/um)' in headers[i]:
            norm_idx = i

    fig, ax = plt.subplots(nrows=2, ncols=2)

    ax[0][0].plot( df['GateV'], df[headers[ids_idx]], linewidth=4 )
    plt.xlabel(r'$V_\mathrm{ds}\,(\mathrm{V})$')
    ax[0][1].semilogy( df['GateV'], df[headers[abs_idx]], linewidth=4 )
    ax[1][0].plot( df['GateV'], df[headers[norm_idx]], linewidth=4 )
    ax[1][1].plot( df['GateV'], df[headers[ids_idx]], linewidth=4 )
    ax[1][1].plot( df['GateV'], df[headers[norm_idx]], linewidth=4 )

    plt.show()

def plot_DrainCurrent_vds_id(df, gate_start, gate_final, gate_step, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    plt.clf()
    headers = list(df) # get column headers
    # get a list of gate values 
    gatevals = generate_GateVoltageList_vds_id(gate_start, gate_final, gate_step)
    idx = 1 # init an index. To be used for GateV(idx) or DrainV(idx)...
    # loop over all headers in an analyzed df
    for head in headers:
        # check to see if the correct string is found. 
        # for example the first search is for DrainI(1), then DrainI(2)
        # and so on.
        if 'DrainI'+'('+str(idx)+')' == head:
            # get the column index of the string
            col_idx = df.columns.get_loc(head)+2 # +2 because we want
            # the column ahead of it. The DrainI(uA) column
            # DrainI(uA) = col_idx +2
            # absDrainI(A) = col_idx +1
            # NormDrainI(uA/um) = col_idx +3

            # plot each column
            drainVdata = df['DrainV'+'('+str(idx)+')'] # Vds data
            plt.plot( drainVdata, df[headers[col_idx]], linewidth=4,\
                label=r'$V_\mathrm{bg}=$'+str(gatevals[idx-1])+\
                r'$\,\mathrm{V}$' )

            idx+=1 # increment the index searched for by 1

    plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=22)
    plt.xlabel(r'$V_\mathrm{ds}\,(\mathrm{V})$', fontsize=22)
    plt.tick_params(labelsize=18) # set labelsize = 18
    plt.legend(loc='best', prop={'size': 8} ) # set legend location
    plt.tight_layout() # tighten border edges

    savename= savename+'_python_linear-plot.png' # set string for saving
    plt.savefig( savename ) # save fig as png

def plot_AbsDrainCurrent_vds_id(df, gate_start, gate_final, gate_step, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    plt.clf()
    headers = list(df) # get column headers
    # get a list of gate values 
    gatevals = generate_GateVoltageList_vds_id(gate_start, gate_final, gate_step)
    idx = 1 # init an index. To be used for GateV(idx) or DrainV(idx)...
    # loop over all headers in an analyzed df
    for head in headers:
        # check to see if the correct string is found. 
        # for example the first search is for DrainI(1), then DrainI(2)
        # and so on.
        if 'DrainI'+'('+str(idx)+')' == head:
            # get the column index of the string
            col_idx = df.columns.get_loc(head)+1 # +2 because we want
            # the column ahead of it. The DrainI(uA) column
            # DrainI(uA) = col_idx +2
            # absDrainI(A) = col_idx +1
            # NormDrainI(uA/um) = col_idx +3

            # plot each column
            drainVdata = df['DrainV'+'('+str(idx)+')'] # Vds data
            plt.semilogy( drainVdata, df[headers[col_idx]], linewidth=4,\
                label=r'$V_\mathrm{bg}=$'+str(gatevals[idx-1])+\
                r'$\,\mathrm{V}$' )

            idx+=1 # increment the index searched for by 1

    plt.ylabel(r'$\left|I_\mathrm{ds}\right|\,(\mathrm{A})$', fontsize=22)
    plt.xlabel(r'$V_\mathrm{ds}\,(\mathrm{V})$', fontsize=22)
    plt.tick_params(labelsize=18) # set labelsize = 18
    plt.legend(loc='best', prop={'size': 8} ) # set legend location
    plt.tight_layout() # tighten border edges

    savename= savename+'_python_abs-logY-plot.png' # set string for saving
    plt.savefig( savename ) # save fig as png

def plot_NormDrainCurrent_vds_id(df, gate_start, gate_final, gate_step, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    plt.clf()
    headers = list(df) # get column headers
    # get a list of gate values 
    gatevals = generate_GateVoltageList_vds_id(gate_start, gate_final, gate_step)
    idx = 1 # init an index. To be used for GateV(idx) or DrainV(idx)...
    # loop over all headers in an analyzed df
    for head in headers:
        # check to see if the correct string is found. 
        # for example the first search is for DrainI(1), then DrainI(2)
        # and so on.
        if 'DrainI'+'('+str(idx)+')' == head:
            # get the column index of the string
            col_idx = df.columns.get_loc(head)+3 # +2 because we want
            # the column ahead of it. The DrainI(uA) column
            # DrainI(uA) = col_idx +2
            # absDrainI(A) = col_idx +1
            # NormDrainI(uA/um) = col_idx +3

            # plot each column
            drainVdata = df['DrainV'+'('+str(idx)+')'] # Vds data
            plt.plot( drainVdata, df[headers[col_idx]], linewidth=4,\
                label=r'$V_\mathrm{bg}=$'+str(gatevals[idx-1])+\
                r'$\,\mathrm{V}$' )

            idx+=1 # increment the index searched for by 1

    plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A}/\mu\mathrm{m})$', fontsize=22)
    plt.xlabel(r'$V_\mathrm{ds}\,(\mathrm{V})$', fontsize=22)
    plt.tick_params(labelsize=18) # set labelsize = 18
    plt.legend(loc='best', prop={'size': 8} ) # set legend location
    plt.tight_layout() # tighten border edges

    savename= savename+'_python_norm-linear-plot.png' # set string for saving
    plt.savefig( savename ) # save fig as png

def plot_DrainCurrent_res2t(df, savename):
    """
    /*-----------------------------------------------------*/
    description:
   
    /*-----------------------------------------------------*/
    args: 
        
    returns:
        None
    /*----------------------------------------------------*/
    """
    import matplotlib.pyplot as plt 
    plt.clf() # clear any figs in buffer
    headers = list(df) # get column headers

    for head in headers:
        if "Idrain(uA)" in head:
            col_idx = df.columns.get_loc(head)+2
    plt.plot( df['AV'], df[headers[col_idx]] ,linewidth=4)
    plt.xlabel(r'$V_\mathrm{ds}\,(\mathrm{V})$', fontsize=22)
    
    if df['AI'].iloc[-1] > 0: # if current is > 0
        plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=22)
    if df['AI'].iloc[-1] < 0: # if current is < 0
        plt.ylabel(r'$-I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=22)
    plt.tick_params(labelsize=18) # label size = 18
    plt.tight_layout() # tighten border layout
    
    savename =  savename + '_python_linear-plot.png'
    plt.savefig(savename) # save fig as png

def get_VoltageBiasStart_res2t(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the starting bias voltage value from settings
        xls sheet for the measurement res2t type     
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of bias voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Start/Level'
        if df[headers[0]][i] == 'Start/Level':
            start_idx = i # store index
    # convert string to int
    return float( df[headers[1]][start_idx] )

def get_VoltageBiasFinal_res2t(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the final bias voltage value from settings
        xls sheet for the measurement res2t type     
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of bias voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Stop'
        if df[headers[0]][i] == 'Stop':
            end_idx = i # store index
    # convert string to int
    return float( df[headers[1]][end_idx] )

def get_NumPointsBias_res2t(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the number of bias voltage points from settings
        xls sheet for the measurement res2t type     
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        int val of bias voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Number of Points'
        if df[headers[0]][i] == 'Number of Points':
            num_idx = i # store index
    # convert string to int
    return int( df[headers[1]][num_idx] )

def get_DrainCurrent_res2t(df, width=1):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 
        df: dataframe from data
    returns:
        
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for head in headers: # loop over headers in df

        if head == 'AI': # search for DrainI col

            # insert the new cols at head+1 loc
            df.insert( df.columns.get_loc(head)+1, 'abs(DrainI(A))',\
                abs( df[head] ) ) # abs DrainI col

            if df[head].iloc[-1] > 0: # keep as positive drain vals
                df.insert( df.columns.get_loc(head)+2, 'Idrain(uA)',\
                    df[head]*1e6 ) # microAmp DrainI col

                df.insert( df.columns.get_loc(head)+3, 'Idrain(uA/um) '+\
                    ' W='+str(width)+' um',\
                    df[head]*1e6/width ) # normalized DrainI col (uA/um)

            elif df[head].iloc[-1] < 0: # convert to positive drain vals
                df.insert( df.columns.get_loc(head)+2, '-Idrain(uA)',\
                    df[head]*-1e6 ) # microAmp -DrainI col

                df.insert( df.columns.get_loc(head)+3, '-Idrain(uA/um) '+\
                    ' W='+str(width)+' um',\
                    df[head]*-1e6/width ) # normalized -DrainI col (uA/um)

def get_VoltageBiasStart_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the starting bias voltage value from settings
        xls sheet for the measurement vds-id type     
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of bias voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Start/Level'
        if df[headers[0]][i] == 'Start/Level':
            start_idx = i # store index
    # convert string to int
    return float( df[headers[2]][start_idx] )

def get_VoltageBiasFinal_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the final bias voltage value from settings
        xls sheet for the measurement vds-id type     
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of bias voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Stop'
        if df[headers[0]][i] == 'Stop':
            end_idx = i # store index
    # convert string to int
    return float( df[headers[2]][end_idx] )

def get_VoltageBiasNumPoints_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the number bias voltage points from settings
        xls sheet for the measurement vds-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        int val of number of points
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Number of Points'
        if df[headers[0]][i] == 'Number of Points':
            num_idx = i # store index
    # convert string to int
    return int( df[headers[2]][num_idx] )

def get_GateVoltageStart_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the starting gate voltage value from settings
        xls sheet for the measurement vds-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of gate voltage 
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Start/Level'
        if df[headers[0]][i] == 'Start/Level':
            start_idx = i # store index
    # convert string to int
    return float( df[headers[3]][start_idx] )

def get_GateVoltageFinal_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the final gate voltage value from settings
        xls sheet for the measurement vds-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of gate voltage 
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Stop'
        if df[headers[0]][i] == 'Stop':
            end_idx = i # store index
    # convert string to int
    return float( df[headers[3]][end_idx] )

def get_NumGatePoints_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the number gate voltage points from settings
        xls sheet for the measurement vds-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        int val of number of points
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe 
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Number of Points'
        if df[headers[0]][i] == 'Number of Points':
            num_idx = i # store index
    # convert string to int
    return int( df[headers[3]][num_idx] )

def get_GateVoltageStep_vds_id(df):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:

    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of the dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Step'
        if df[headers[0]][i] == 'Step':
            step_idx = i # store index
    return float( df[headers[3]][step_idx] )

def generate_GateVoltageList_vds_id(gate_start, gate_final, gate_step):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:

    /*----------------------------------------------------*/
    """
    import numpy as np 
    return np.arange(gate_start, gate_final+gate_step, gate_step)

def get_DrainCurrent_vds_id(df, gate_start, gate_final, gate_step, width=1):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:

    /*----------------------------------------------------*/
    """
    headers = list(df) # get the headers of the dataframe
    gate_vals = generate_GateVoltageList_vds_id(gate_start, gate_final, gate_step)
    idx = 0 # init idx to zero
    for head in headers:
        if 'DrainI' in head:
            df.insert( df.columns.get_loc(head)+1, 'abs(DrainI(A)) '\
                +str(gate_vals[idx])+' V', abs( df[head] ) )

            df.insert( df.columns.get_loc(head)+2, 'DrainI(uA) '\
                +str(gate_vals[idx])+' V',  df[head]*1e6 )

            df.insert( df.columns.get_loc(head)+3, 'NormDrainI(uA/um) '\
                +str(gate_vals[idx])+' V W='+str(width)+' um',\
                df[head]*1e6/width ) 
            idx += 1 # increase for next loop 
def get_VoltageBias_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the voltage bias from the settings xls sheet
        for the measurement vgs-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of voltage bias
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[2]] ) ):
        # search col for string 'Voltage Bias'
        if df[headers[2]][i] == 'Voltage Bias':
            # convert string to int
            return float( df[headers[2]][i+2] )
    # if not found, then return none
    return None

def get_GateVoltageStart_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the starting gate voltage value from settings
        xls sheet for the measurement vgs-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of gate voltage 
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Start/Level'
        if df[headers[0]][i] == 'Start/Level':
            start_idx = i # store index
    # convert string to int
    return float( df[headers[3]][start_idx] )

def get_GateVoltageFinal_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the final gate voltage value from settings
        xls sheet for the measurement vgs-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        float val of gate voltage
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Stop' 
        if df[headers[0]][i] == 'Stop':
            end_idx = i # store index
    # convert string to float
    return float( df[headers[3]][end_idx] ) 

def get_NumGatePoints_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:
        Gets the number gate voltage points from settings
        xls sheet for the measurement vgs-id type
    /*-----------------------------------------------------*/
    args: 
        df: dataframe from settings
    returns:
        int val of number of points
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for i in range( len( df[headers[0]] ) ):
        # search col for string 'Number of Points'
        if df[headers[0]][i] == 'Number of Points':
            num_idx = i # store index
    # convert string to int
    return int( df[headers[3]][num_idx] )

def get_DrainCurrent_vgs_id(df, bias, width=1):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 
        df: dataframe from data
    returns:
        
    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for head in headers: # loop over headers in df

        if head == 'DrainI': # search for DrainI col
            # insert the new cols at head+1 loc
            df.insert( df.columns.get_loc(head)+1, 'abs(DrainI(A)) '+\
                str(bias)+'V',abs( df[head] ) ) # abs DrainI col

            if df[head].iloc[-1] > 0: # keep as positive drain vals
                df.insert( df.columns.get_loc(head)+2, 'Idrain(uA) '+\
                str(bias)+'V', df[head]*1e6 ) # microAmp DrainI col

                df.insert( df.columns.get_loc(head)+3, 'Idrain(uA/um) '+\
                str(bias)+'V '+'W= '+str(width)+' um',\
                df[head]*1e6/width ) # normalized DrainI col (uA/um)

            elif df[head].iloc[-1] < 0: # convert to positive drain vals
                df.insert( df.columns.get_loc(head)+2, '-Idrain(uA) '+\
                str(bias)+'V', df[head]*-1e6 ) # microAmp -DrainI col

                df.insert( df.columns.get_loc(head)+3, '-Idrain(uA/um) '+\
                str(bias)+'V '+'W= '+str(width)+' um',\
                df[head]*-1e6/width ) # normalized -DrainI col (uA/um)

def get_OnOffRatio_vgs_id(df):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 
        df: dataframe from data
    returns:

    /*----------------------------------------------------*/
    """
    headers = list(df) # get headers of dataframe
    for head in headers: # loop over headers in df
        if head == 'abs(DrainI(A))': # if col is absDrainI col
            maxVal = df[head].max() # store max value
            minVal = df[head].min() # store min value
            return maxVal/minVal
    return None

if __name__=="__main__":
    import sys, os, io, datetime, numpy as np, matplotlib.pyplot as plt, pandas as pd

    width, plot_flag = CommandLineArgs(sys.argv) # get cmd line args  

    log = open('log.txt', 'w') # open the log file for writing
    log.write("*"*50)
    log.write("\n\n\tScript name: %s\n\n" % sys.argv[0])
    log.write("\n\tCreated on %s\n\n" % datetime.datetime.now())
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
                get_DrainCurrent_res2t(data) # convert the data sheet
                if plot_flag == True:
                    # vgs-id plotting methods
                    log.write("\n###<---\tCreating plots of res2t\n\n")
                    plot_DrainCurrent_res2t(data, subdir+fname) 

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
