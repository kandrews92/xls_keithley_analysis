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
