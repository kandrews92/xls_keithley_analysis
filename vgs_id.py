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
    # convert string to int
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

def plot_DrainCurrent_vgs_id(df):
    import matplotlib.pyplot as plt
    plt.clf()
    headers = list(df)
    for i in range( len(headers) ):
        if 'Idrain(uA)' in headers[i]:
            idx = i
    plt.plot(df['GateV'], df[headers[idx]], linewidth=4)
    if df['DrainI'].iloc[-1] > 0:
        plt.ylabel(r'$I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=18)
    else:
        plt.ylabel(r'$-I_\mathrm{ds}\,(\mu\mathrm{A})$', fontsize=18)
    plt.xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=18)
    #plt.show()

def plot_AbsDrainCurrent_vgs_id(df):
    import matplotlib.pyplot as plt
    plt.clf()
    headers = list(df)
    for i in range( len(headers) ):
        if 'abs(DrainI(A))' in headers[i]:
            idx = i
    plt.semilogy(df['GateV'], df[headers[idx]], linewidth=4)
    plt.ylabel(r'$I_\mathrm{ds}\,(\mathrm{A})$', fontsize=18)
    plt.xlabel(r'$V_\mathrm{bg}\,(\mathrm{V})$', fontsize=18)
    #plt.show()

def plot_DualAxisDrainCurrent_vgs_id(df):
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

def plot_LogYDrainCurrent_vgs_id(df):
    import matplotlib.pyplot as plt
    pass

def plot_NormDrainCurrent_vgs_id(df):
    import matplotlib.pyplot as plt
    pass

