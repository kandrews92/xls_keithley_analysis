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