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
    
