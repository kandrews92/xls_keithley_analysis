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