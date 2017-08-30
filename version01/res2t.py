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