from vds_id import generate_GateVoltageList_vds_id

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

    savename = 'python-'+savename + 'linear-plot.png'
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

    savename = 'python-'+savename + '-logY-plot.png'
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

    savename= 'python-'+savename + "-norm-linear-plot.png" # plot will be saved as png
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

    savename= 'python-'+savename+'-linear-plot.png' # set string for saving
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

    savename= 'python-'+savename+'-abs-logY-plot.png' # set string for saving
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

    savename= 'python-'+savename+'-norm-linear-plot.png' # set string for saving
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
    
    savename = 'python-' + savename + '-linear-plot.png'
    plt.savefig(savename) # save fig as png
