
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

    savename = savename + 'linear-plot.png'
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

    savename = savename + '-logY-plot.png'
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

    savename= savename + "-norm-linear-plot.png" # plot will be saved as png
    plt.savefig( savename ) # save as png

def plot_AllSubplots_vgs_id(df):
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

def plot_DrainCurrent_vds_id(df):
    import matplotlib.pyplot as plt 
    headers = list(df) # get column headers

def plot_AbsDrainCurrent_vds_id(df):
    import matplotlib.pyplot as plt 
    header = list(df) # get column headers

def plot_DrainCurrent_res2t(df):
    import matplotlib.pyplot as plt 
    headers = list(df) # get column headers

